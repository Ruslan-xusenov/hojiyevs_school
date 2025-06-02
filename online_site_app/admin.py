from django.contrib import admin
from .models import Category, News, Contact

admin.site.register(Category)
admin.site.register(News)
admin.site.register(Contact)