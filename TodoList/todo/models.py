from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=100) #할 일
    completed=models.BooleanField(default=False) #완료 여부
    created_at=models.DateTimeField(auto_now=True) #등록 시간


    def __str__(self):
        return self.title

