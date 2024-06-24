from django.contrib import admin
from .models import Topic, Newspaper, Redactor


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("title",)


@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    search_fields = ("username",)
    list_filter = ("username",)