from curses import def_shell_mode
from email.policy import default
from pydoc import describe
from django.db import models

# Create your models here.
class Resturant(models.Model):
    name = models.CharField(max_lenght=30)
    description = models.TextField(default='')
    op_time = models.TimeField()
    cl_time = models.TimeField()
    cr_time = models.DateTimeField(auto_now_add=True)


