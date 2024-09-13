from django.db import models
from config import settings
from django.utils.translation import gettext as _

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):

    class PeriodicityOfHabit(models.TextChoices):
        ONE = '1', _('Ежедневно')
        TWO = '2', _('Раз в 2 дня')
        THREE = '3', _('Раз в 3 дня')
        FOUR = '4', _('Раз в 4 дня')
        FIVE = '5', _('Раз в 5 дней')
        SIX = '6', _('Раз в 6 дней')
        SEVEN = '7', _('Раз в 7 дней')

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             **NULLABLE,
                             verbose_name='Пользователь',
                             help_text='Создатель привычки')
    place = models.CharField(max_length=160,
                             verbose_name='Место',
                             help_text='Где необходимо выполнять привычку')
    time = models.DateTimeField(
        verbose_name='Время', help_text='Когда необходимо выполнять привычку')
    action = models.CharField(max_length=160,
                              verbose_name='Действие',
                              help_text='Действие представляющее привычку')
    is_nice_habit = models.BooleanField(
        default=True,
        verbose_name='Признак приятной привычки',
        help_text='Приятная привычка')
    related_habit = models.ForeignKey(
        'Habit',
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='связанная привычка',
        help_text=
        'Привычка, которая связана с другой привычкой, указывается для полезной'
    )
    periodicity = models.CharField(
        default=PeriodicityOfHabit.ONE,
        choices=PeriodicityOfHabit.choices,
        verbose_name='Периодичность',
        help_text='Напоминание о выполнении привычки')
    reward = models.CharField(
        max_length=200,
        verbose_name='Вознаграждение',
        **NULLABLE,
        help_text='Вознаграждение после выполнения привычки')
    duration_time = models.PositiveIntegerField(
        default=120,
        verbose_name='Время на выполнение (сек)',
        help_text='Необходимое время пользователю на выполнение привычки')
    is_published = models.BooleanField(
        default=True,
        verbose_name='Признак публичности привычки',
        help_text='Публичный доступ для других пользователей')
    next_date = models.DateField(
        **NULLABLE,
        verbose_name="Дата следующего выполнения привычки",
        help_text='Выполнить привычку в этот день')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
