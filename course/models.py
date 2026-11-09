from django.db import models

class TimeStampeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Student(TimeStampeModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=18)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Teacher(TimeStampeModel):
    jins = (
        ('erkak', 'erkak'),
        ('ayol', 'ayol'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    sertifikat = models.BooleanField(default=False)
    jins = models.CharField(choices=jins, max_length=100)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Subject(TimeStampeModel):
    subject = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    ball = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f'{self.subject} {self.teacher} {self.ball}'
