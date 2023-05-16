from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="")

class Servicepage(models.Model):
    image = models.ImageField(upload_to='')


class Events(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="", null=True)

class Mainpage(models.Model):
    image = models.ImageField(upload_to='')


class About(models.Model):
    name = models.CharField(max_length=100)
    job = models.TextField()
    image = models.ImageField(upload_to="")

class Aboutpage(models.Model):
    image = models.ImageField(upload_to='')




class Orderpage(models.Model):
    imagephone = models.ImageField(upload_to='')
    number = models.TextField()
    address = models.TextField(null=True)
    text = models.TextField()


class Form(models.Model):
    ORDER = (
        ("In our hall", "In our hall"),
        ("Catering", "Catering"),
        ("Stylized holidays", "Stylized holidays"),
    )
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=13)
    order = models.CharField(max_length=100, choices=ORDER)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

