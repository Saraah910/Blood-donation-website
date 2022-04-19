from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=20)
    message = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.name