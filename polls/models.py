from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=500, null=True)
    updated_at = models.CharField(max_length=500, null=True)
