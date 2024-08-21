from django.contrib import admin
from .models import Car, Comment

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'average_rating', 'summary')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('car', 'rating')
    list_filter = ('car',)