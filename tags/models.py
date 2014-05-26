from django.db import models

# Create your models here.
MAX_LEN = 200

class App(models.Model):
    app_name = models.CharField(max_length=MAX_LEN,
                               unique=True)
    def __str__(self):
        return self.app_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=MAX_LEN, 
                                unique=True)
    tag_type = models.CharField(max_length=MAX_LEN)
    def __str__(self):
        return self.tag_name

class AppTag(models.Model):
    app = models.ForeignKey(App)
    tag = models.ForeignKey(Tag)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.app.app_name + ':' + self.tag.tag_name
