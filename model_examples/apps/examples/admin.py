from django.contrib import admin
from .models import Simple,DateExample,NullExample,Language,Framework

# Register your models here.

admin.site.register(Simple)
admin.site.register(DateExample)
admin.site.register(NullExample)
admin.site.register(Language)
admin.site.register(Framework)