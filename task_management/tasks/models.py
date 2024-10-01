from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models. TextField(blank=True, null=True)
    due_date = models.DateField()
    priority_level = models.CharField(max_length=10, choices=[('low','Low'),('medium','Medium'),('high','High')])
    status = models.CharField(max_length=10, default='pending')
    def save(self, *args, **kwargs):
        if self.due_date < datetime.date.today():
            self.status = 'completed'
        super().save(*args, **kwargs)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)  # Timestamp for completion

    def mark_as_complete(self):

        #Mark task as complete and set the timestamp
        self.is_complete = True
        self.completed_at = timezone.now()
        self.save()

    def mark_as_incomplete(self):
        #Mark task as incomplete and reset the timestamp
        self.is_complete = False
        self.completed_at = None
        self.save()
