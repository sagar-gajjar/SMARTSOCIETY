from django.contrib import admin
from .models import *
from watchman.models import *

# Register your models here.
admin.site.register(MemberDetails)
admin.site.register(Chairman)
admin.site.register(Member)
admin.site.register(Notice)
admin.site.register(Gallary)
admin.site.register(VideoGallary)
admin.site.register(Event)
admin.site.register(Watchman)
admin.site.register(Maintenance)
admin.site.register(Complaint)
admin.site.register(Visitor)