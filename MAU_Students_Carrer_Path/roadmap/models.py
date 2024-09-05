# models.py
from django.db import models
from django.contrib.auth.models import User

class Roadmap(models.Model):
    career_path = models.CharField(max_length=100)  # e.g., 'Software Engineer'
    description = models.TextField()
    image = models.ImageField(upload_to='roadmaps/', null=True, blank=True)  # Optional image field
    pdf = models.FileField(upload_to='roadmaps/pdfs/', null=True, blank=True)  # New PDF field for file uploads

    def __str__(self):
        return self.career_path



class Course(models.Model):
    roadmap = models.ForeignKey(Roadmap, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  # e.g., 'Python for Beginners'``
    platform = models.CharField(max_length=100)  # e.g., 'Coursera', 'Udemy'
    url = models.URLField()  # URL to the course

    def __str__(self):
        return self.title
