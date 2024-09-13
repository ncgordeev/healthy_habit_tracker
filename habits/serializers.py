from rest_framework import serializers
from habits.models import Habit
from habits.validators import time_limit, periodicity_limit, HabitValidator


class HabitSerializer(serializers.ModelSerializer):
    duration_time = serializers.IntegerField(validators=[time_limit])
    periodicity = serializers.CharField(validators=[periodicity_limit])

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            HabitValidator(
                is_nice_habit="is_nice_habit",
                related_habit="related_habit",
                reward="reward",
            )
        ]
