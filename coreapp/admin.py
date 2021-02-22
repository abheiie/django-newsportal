from django.contrib import admin

# Register your models here.
from .models import Article, UserTag, TopFeatured

admin.site.register(Article)
admin.site.register(UserTag)
admin.site.register(TopFeatured)

