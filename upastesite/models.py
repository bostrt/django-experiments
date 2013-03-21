from django.db import models

class Group(models.Model):
    name = models.TextField()

class Paste(models.Model):
    code = models.TextField()
    email = models.EmailField()
    group = models.ForeignKey(Group)


    
