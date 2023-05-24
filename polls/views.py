import time

from django.conf import settings
from django.core.cache import cache
from django.http import HttpRequest
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.cache import get_cache_key
from django.views.decorators.cache import cache_page

from polls.forms import BlogForm
from .models import Blog


def start(request):
    if request.method == "GET":
        return HttpResponse('/get/...your number exceed id in this db, put number less ')


@cache_page(30 * 15, cache='default')
def get(request, id: int):
    try:
        if request.method == "GET":
            blog = Blog.objects.get(id=id)
            time.sleep(5)
            return render(request, "index.html", {'con': blog})
    except Blog.DoesNotExist:
        return HttpResponseRedirect(reverse("start"))


def expire_view_cache(request, view_name, args=None, key_prefix=None):
    request_meta = {'SERVER_NAME': request.get_host().split(":")[0], 'SERVER_PORT': request.get_host().split(":")[1]}
    request = HttpRequest()
    request.method = 'GET'
    request.META = request_meta
    request.path = reverse(view_name, args=args)
    if settings.USE_I18N:
        request.LANGUAGE_CODE = settings.LANGUAGE_CODE
        cache_key = get_cache_key(request, key_prefix=key_prefix)
        if cache_key:
            if cache.has_key(cache_key):
                cache.delete(cache_key)
                return (True, 'Successfully invalidated')
            else:
                return (False, 'Cache_key does not exist in cache')
        else:
            raise ValueError('Failed to create cache_key')


def blog_edit(request, id: int):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "GET":
        form = BlogForm(instance=blog)
        context = {"form": form}
        return render(request, "edit.html", context)
    elif request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog.save()
            expire_view_cache(request, get, args=[id])
            return redirect('get', id=id)
