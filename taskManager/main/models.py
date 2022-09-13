from django.db import models


class Task(models.Model):
    title = models.CharField('Title', max_length=60)
    task = models.TextField('Task')
    create_on = models.DateTimeField('Create on', auto_now_add=True)
    author = models.CharField('Author', max_length=40)

    def __str__(self):
        return self.title
