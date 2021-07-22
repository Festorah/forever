from django.contrib import admin
from .models import Contact

admin.site.site_header = "MJoy"
admin.site.site_title = "MJoy Admin Area"
admin.site.index_title = "Welcome to MJoy Admin area"


admin.site.register(Contact)