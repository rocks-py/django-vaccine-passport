from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=200)
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Desease(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Заболевание"
        verbose_name_plural = "Заболевания"
        
class Vaccine(models.Model):
    name = models.CharField(max_length=200, verbose_name="название")
    manufacturer = models.CharField(max_length=200, default=None, blank=True, null=True, verbose_name="производитель")
    desease = models.ForeignKey(Desease, on_delete=models.CASCADE, default=None, blank=True, null=True, verbose_name="заболевание")
    protection_period = models.DateField(default=None, blank=True, null=True, verbose_name="срок действия")
    administration_schedule = models.TextField(default=None, blank=True, null=True, verbose_name="схема введения")
    age = models.IntegerField(default=None, blank=True, null=True, verbose_name="возраст")
    efficiency_percent = models.IntegerField(default=None, blank=True, null=True, verbose_name="эффективность")
    side_effects = models.TextField(default=None, blank=True, null=True, verbose_name="побочные эффекты")
    price = models.IntegerField(default=None, blank=True, null=True, verbose_name="цена")
    CURRENCY_TYPE = (
        ('RUB', 'Ruble'),
        ('EUR', 'Euro'),
        ('USD', 'US Dollar')
    )
    currency_type = models.CharField(max_length=10, choices=CURRENCY_TYPE, default=CURRENCY_TYPE[1], verbose_name="тип валюты")
    comments = models.TextField(default=None, blank=True, null=True, verbose_name="комментарий")
    is_hidden = models.BooleanField(default=False, blank=True, null=True)
    is_produced = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вакцина"
        verbose_name_plural = "Вакцины"

class Collection(models.Model):
    name = models.CharField(max_length=200)
    vaccines = models.ManyToManyField(Vaccine)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"


class Person(models.Model):
    name = models.CharField(max_length=200, verbose_name="имя человека")
    # age = models.IntegerField(verbose_name="возраст")
    dateofbirth = models.DateField(verbose_name="дата рождения")
    SEX = (
        ('M', 'MALE'),
        ('F', 'FEMALE')
    )
    sex = models.CharField(max_length=1, choices=SEX)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vaccines = models.ManyToManyField(Vaccine, blank=True, null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"

# class UserVaccine(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
#     date_expire = models.DateField(null=True)

class UserPerson(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PersonVaccine(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    date_expire = models.DateField(null=True)
