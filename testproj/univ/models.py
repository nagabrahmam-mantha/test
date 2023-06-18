from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.CharField(max_length=100, null=True, blank=True)

    objects = models.Manager()  # our default django manager

    def __str__(self):
        """String for representing the Model object."""
        return str(self.first_name)