from django.db import models

# Create your models here.
class Headline(models.Model):
    leaning = models.TextField()
    title = models.TextField()
    img = models.URLField(max_length=1000, null=True, blank=True)
    mins_ago = models.IntegerField(default=1440)
    time_ago_str = models.TextField(null=True)
    url = models.URLField(max_length=1000)

    def __str__(self):
        return str(self.title)