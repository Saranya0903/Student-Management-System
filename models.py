from django.db import models

class Student(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    register_number = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    batch = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Achievement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # DROPDOWN
    date = models.DateField()
    proof = models.FileField(upload_to='proofs/', null=True, blank=True)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return self.title
