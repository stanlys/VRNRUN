from django.db import models

# Create your models here.

class Post(models.Model):
    date = models.DateField()
    postcaption = models.CharField(max_length=256)
    posttext = models.TextField()
    photo = models.FileField(null=False,blank=True)

    def __str__(self):
        return '{} - {}'.format(self.date,self.postcaption[:50])

    class Meta:
        ordering = ['-date']
