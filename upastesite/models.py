from django.db import models

class Paste(models.Model):
    code = models.TextField()
    email = models.EmailField()
    added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.code
