from django.urls import path
from habits.apps import HabitsConfig
from habits.views import (
    HabitListAPIView,
    HabitOwnerListAPIView,
    HabitCreateAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("", HabitListAPIView.as_view(), name="habit_list"),
    path("my_habits/", HabitOwnerListAPIView.as_view(), name="habit_user_list"),
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("detail/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_detail"),
    path("update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit_delete"),
]
