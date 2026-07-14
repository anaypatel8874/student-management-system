from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=100)

    roll_no = models.CharField(max_length=20, unique=True)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    branch = models.CharField(max_length=50)

    semester = models.IntegerField()

    photo = models.ImageField(
        upload_to="students/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
