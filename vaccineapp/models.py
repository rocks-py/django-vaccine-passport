from django.db import models
from django.urls import reverse

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=200)
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        
class Vaccine(models.Model):
    name = models.CharField(max_length=200, verbose_name="название")
    manufacturer = models.CharField(max_length=200, default=None, blank=True, null=True, verbose_name="производитель")
    protection_period = models.IntegerField(default=None, blank=True, null=True, verbose_name="срок действия (мес)")
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
    is_produced = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вакцина"
        verbose_name_plural = "Вакцины"

class Disease(models.Model):
    name = models.CharField(max_length=200)
    vaccines = models.ManyToManyField(Vaccine, verbose_name="вакцины", blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Заболевание"
        verbose_name_plural = "Заболевания"

class Collection(models.Model):
    name = models.CharField(max_length=200)
    diseases = models.ManyToManyField(Disease, verbose_name="заболевания", blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"

    def get_absolute_url(self):
        return reverse("collection-detail", kwargs={"pk": self.pk})

class Person(models.Model):
    name = models.CharField(max_length=200, verbose_name="имя человека")
    # age = models.IntegerField(verbose_name="возраст")
    dateofbirth = models.DateField(verbose_name="дата рождения")
    SEX = (
        ('M', 'MALE'),
        ('F', 'FEMALE')
    )
    sex = models.CharField(max_length=1, choices=SEX, verbose_name="пол", default='M')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"


class PersonVaccine(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, verbose_name="человек")
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, null=True, verbose_name="заболевание")
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE, null=True, verbose_name="вакцина")
    date_expire = models.DateField(null=True, verbose_name="Срок действия (до)")
    
    class Meta:
        verbose_name = "Вакцины человека"
        verbose_name_plural = "Вакцины человека"

# TODO: можно заменить через ManyToManyField
class UserPerson(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)