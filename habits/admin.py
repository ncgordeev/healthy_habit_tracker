from django.contrib import admin
from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
        "place",
        "time",
        "action",
        "periodicity",
        "is_published",
    )
    list_filter = (
        "user",
        "is_published",
    )
    search_fields = ("user",)
