from django.db import models

# Create your models here.
class Headline(models.Model):
    leaning = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    img = models.URLField(null=True, blank=True)
    mins_ago = models.IntegerField(default=1440)
    time_ago_str = models.CharField(max_length=200, null=True)
    url = models.URLField()

    def __str__(self):
        return str(self.title)