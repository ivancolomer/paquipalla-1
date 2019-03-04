from django.contrib import admin

# Register your models here.
from .models import Envelope, Company

# Register your models here.
admin.site.register(Envelope)
admin.site.register(Company)
