from django.db import models

# Create your models here.
class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y")
    def _str_(self):
        return self.caption