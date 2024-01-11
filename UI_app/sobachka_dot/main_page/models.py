from django.db import models

class Breed(models.Model):
    id_breed = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    info = models.TextField()
    image = models.ImageField(null=True, blank=True)

    # def __str__(self):
    #     return self.name

class User(models.Model):
    id_user = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=200)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

class Dogs(models.Model):
    id_dog = models.AutoField(primary_key=True, unique=True)
    id_breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mark = models.CharField(max_length=100)
    chip = models.CharField(max_length=100)
    birthdate = models.CharField(max_length=100) #change to DateField
    deathdate = models.CharField(max_length=100) #change to DateField
    color = models.CharField(max_length=100)
    id_dad = models.ForeignKey('self', on_delete=models.CASCADE,  related_name='daddog')
    id_mom = models.ForeignKey('self', on_delete=models.CASCADE,  related_name='momdog')
    kennel = models.CharField(max_length=100)
    id_breeder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='breeder')
    id_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    photo = models.CharField(max_length=100) #link --> change to UrlField

