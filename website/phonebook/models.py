from django.db import models
from django.urls import reverse


class Person(models.Model):
    firstName = models.CharField(max_length=50, verbose_name="Imię")
    lastName = models.CharField(max_length=50, verbose_name="Nazwisko")

    class Meta:
        unique_together = [['firstName', 'lastName']]

    def get_absolute_url(self):
        return reverse('phonebook:person_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class PhoneNumber(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT, editable=False)
    number = models.CharField(max_length=50, verbose_name="Numer telefonu")

    def get_absolute_url(self):
        return reverse('phonebook:person_detail', kwargs={'pk': self.person.pk})

    def __str__(self):
        return self.number


class Email(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT, editable=False)
    email = models.EmailField()

    def get_absolute_url(self):
        return reverse('phonebook:person_detail', kwargs={'pk': self.person.pk})

    def __str__(self):
        return self.email