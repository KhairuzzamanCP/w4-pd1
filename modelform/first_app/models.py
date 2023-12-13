from django.db import models

# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField(primary_key= True)
    email_field = models.EmailField(default= 'Rana gmail.com')
    address = models.TextField(default="Dhaka")
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    duration_field = models.DurationField()
    float_field = models.FloatField()

    def __str__(self):
        return f"Roll: {self.roll} Name: {self.name}"
    

