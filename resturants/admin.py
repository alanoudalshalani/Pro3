from django.contrib import admin
from .models import Resturant

# Register your models here.
@admin.register(Resturant)
class ResturantAdmin(admin.ModelAdmin):
    # fields = ("name" , "op_time" )
    exclude = ("description",)
    list_display = ("id" , "name", "op_time")




admin.site.register(Resturant)

