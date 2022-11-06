from django.contrib import admin

# Register your models here.
from .models import nculture
admin.site.register(nculture)

from .models import order
admin.site.register(order)