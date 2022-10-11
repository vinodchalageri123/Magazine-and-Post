from django.db import models


# Create your models here.
class MyClubUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Magazines(models.Model):
    magazine_name = models.CharField('Magazine_Name', max_length=50, blank=True)
    published_at = models.DateField(blank=True)
    magazine_copy = models.FileField('Magazine_Copy', upload_to='upload/', blank=True, null=True)
    uploaded_by = models.ManyToManyField(MyClubUser, blank=True, null=True)

    def __str__(self):
        return self.magazine_name
