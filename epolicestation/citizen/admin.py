from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(citizen)
admin.site.register(law)
admin.site.register(crime_category)
admin.site.register(Sub_crime)
admin.site.register(complaint)

# Register your models here.
