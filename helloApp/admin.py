from django.contrib import admin
# Register your models here.
from helloApp.models import Category, Page, UserProfile
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)