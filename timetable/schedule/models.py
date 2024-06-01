from django.db import models

k
class Schedule(models.Model):
    staff_id = models.BigIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    recurring = models.CharField(max_length=30, default='No')
    status = models.CharField(max_length=30, default='Scheduled')

    def __str__(self):
        return f"({self.start_time} - {self.end_time})"
