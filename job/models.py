from django.db import models
from django.db.models import CharField
# Create your models here.

 
JOB_TYBE = (
    ("full Time","Full Time"),
    ("Part Time","Part Time"),  
)


class job(models.Model):
    title = models.CharField(max_length=100)
    JOB_TYBE = models.CharField(max_length=15, choices=JOB_TYBE)
    Description = models.TextField(max_length=1000)
    Published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    Salary = models.IntegerField(default=0)
    Experience = models.IntegerField(default=0)

    def __str__(self):
        return self.title


