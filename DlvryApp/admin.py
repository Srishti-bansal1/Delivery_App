from django.contrib import admin

# Register your models here.
from .models import Organization, Item, Pricing, SignUpModel

admin.site.register(Organization)
admin.site.register(Item)
admin.site.register(Pricing)
admin.site.register(SignUpModel)