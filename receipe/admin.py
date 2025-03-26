from django.contrib import admin

# Register your models here.
from receipe.models import *
admin.site.register(Food)  
admin.site.register(Orders)