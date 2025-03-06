from django.db import models
from django.contrib.auth.models import User

class Action(models.Model):
    id = models.AutoField(primary_key=True)
    action = models.BooleanField()
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Action by {self.user} on {self.date} at {self.time}"
