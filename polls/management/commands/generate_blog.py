from django.core.management.base import BaseCommand
from faker import Faker

from polls.models import Blog


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("questions", type=int)

    def handle(
            self,
            *args,
            questions,
            **options,
    ):
        fake = Faker()
        fake.name()
        for _ in range(questions):
            for _ in range(5):
                fake = Faker()
                q = Blog.objects.create(title=str(fake.text()).split(' ')[0],
                                        content=str(fake.text()), updated_at=str(fake.iso8601()).replace('T', ' '))
                self.stdout.write(
                    self.style.SUCCESS('Successfully created blog with ID "%s"' % q.id)
                )
