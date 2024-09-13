from datetime import datetime, timedelta
from celery import shared_task
from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def check_habits_for_action():
    habits = Habit.objects.all()
    now_time = datetime.now().time()
    now_date = datetime.now().date()
    for habit in habits:
        if not habit.next_date:
            if habit.time < now_time:
                send_telegram_message(habit)
                habit.next_date = now_date + timedelta(days=int(habit.periodicity))
                habit.save()
        elif habit.next_date <= now_date:
            send_telegram_message(habit)
            habit.next_date = now_date + timedelta(days=int(habit.periodicity))
            habit.save()
