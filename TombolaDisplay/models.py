from django.db import models
from datetime import date

class Participant(models.Model):
    name = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)  # attention à la faute
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Tombola(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(default=date.today)
    finished_at = models.DateField(default=date.today)
    is_open = models.BooleanField(default=True)
    owner = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    number = models.AutoField(primary_key=True)
    price = models.FloatField(default= 2.00)
    date = models.DateField(default=date.today)
    owner = models.ForeignKey(Participant, on_delete=models.CASCADE)
    is_winner = models.BooleanField(default=False)
    tombola = models.ForeignKey(Tombola, on_delete=models.CASCADE, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.number)


