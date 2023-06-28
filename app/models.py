from django.db import models

# Create your models here.
class confidential(models.Model):
    employee=models.CharField(max_length=50)
    img=models.ImageField(upload_to="images/")
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employee