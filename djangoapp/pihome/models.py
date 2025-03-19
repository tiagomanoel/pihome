from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Action(models.Model):
    id = models.AutoField(primary_key=True)
    action = models.TextField(null=True, blank=True)  # Permitir valores nulos
    date = models.DateField()
    time = models.TimeField()
    topic = models.TextField(null=True, blank=True)  # Permitir valores nulos

    def clean(self):
        if self.action not in ["ON", "OFF"]:
            raise ValidationError("Action must be 'ON' or 'OFF'")

    def __str__(self):
        return f"Action on {self.date} at {self.time} with action: {self.action} on topic: {self.topic}"
