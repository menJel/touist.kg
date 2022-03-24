from re import search
from django.contrib import admin
from .models import Post,Comment,Category

# Register your models here.

#admin.site.register(Post) #обычный способ настройки админки 

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","category","author","created","is_active"]
    list_filter = ("created",
        "author__username",
        "category","is_active",
        )
    search_fields = ["title","id","text","created"]
    list_editable = ["category","is_active"]


@admin.register(Category) #второй  способ настройки админки через класс
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","slug","id"] #настраиваем списки
    prepopulated_fields = {"slug":("name",)}
