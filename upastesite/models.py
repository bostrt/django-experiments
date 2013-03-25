from django.db import models

class Group(models.Model):
    name = models.TextField()
    added = models.DateTimeField(auto_now_add=True)

    def __unicode(self):
        return self.name

class Paste(models.Model):
    code = models.TextField()
    email = models.EmailField()
    group = models.ForeignKey(Group)
    added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.code
