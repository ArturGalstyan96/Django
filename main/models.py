from django.db import models

# Create your models here.

class Tour(models.Model):
    model = models.CharField('Tour', max_length=30)
    img = models.ImageField('Tour Image',  upload_to='images')
    price = models.PositiveBigIntegerField('Tour Price')

    def __str__(self) -> str:
        return self.model


class About(models.Model):
    about = models.TextField('About Us')

    def __str__(self) -> str:
        return self.about
    

class Contact(models.Model):
    userName = models.CharField('User Name:', max_length=30)
    userEmail = models.EmailField('User Email:', unique=True)
    userPhone = models.CharField('User Phone:', max_length=30)
    userRewiew = models.TextField('User Rewiew: ')

    def __str__(self):
        return self.userName

