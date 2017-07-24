from django.db import models

# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True)
    fax_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.upper()


class Contact(models.Model):
    name = models.CharField(max_length=255, blank=True)

    organization = models.ForeignKey(Organization, related_name='contacts')
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)