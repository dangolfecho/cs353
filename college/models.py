from django.db import models

# Create your models here.

class Courses(models.Model):
    course_id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=200)
    dept_id = models.IntegerField()
    credits = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        db_table = 'courses'
