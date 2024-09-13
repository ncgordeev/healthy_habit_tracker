from django.urls import reverse

from rest_framework import status

from rest_framework.test import APITestCase

from habits.models import Habit

from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create(name="Тест",
                                        email="testuser@example.com",
                                        telegram_chat_id=1234567,
                                        is_active=True)

        self.user.set_password('test123')

        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(user=self.user,
                                          place="Спортзал",
                                          time="15:00",
                                          action="Жим штанги",
                                          periodicity="2",
                                          reward="Выпить протеин",
                                          duration_time=120)

    def test_habit_create(self):

        data = {
            "place": "Парк",
            "time": "18:00",
            "action": "Пробежка",
            "periodicity": "2",
            "reward": "Встретиться с девушкой",
            "duration_time": 120
        }

        response = self.client.post(reverse('habits:habit_create'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_list(self):

        response = self.client.get(reverse('habits:habit_list'))

        data = response.json()

        result = {
            'count':
            1,
            'next':
            None,
            'previous':
            None,
            'results': [{
                'id': self.habit.pk,
                'duration_time': 120,
                'periodicity': '2',
                'place': 'Спортзал',
                'time': '15:00:00',
                'action': 'Жим штанги',
                'is_nice_habit': False,
                'reward': 'Выпить протеин',
                'is_published': True,
                'next_date': None,
                'user': self.user.pk,
                'related_habit': None
            }]
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data, result)

    def test_habit_owner_list(self):

        response = self.client.get(reverse('habits:habit_user_list'))

        data = response.json()

        result = {
            'count':
            1,
            'next':
            None,
            'previous':
            None,
            'results': [{
                'id': self.habit.pk,
                'duration_time': 120,
                'periodicity': '2',
                'place': 'Спортзал',
                'time': '15:00:00',
                'action': 'Жим штанги',
                'is_nice_habit': False,
                'reward': 'Выпить протеин',
                'is_published': True,
                'next_date': None,
                'user': self.user.pk,
                'related_habit': None
            }]
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data, result)

    def test_habit_retrieve(self):

        response = self.client.get(
            reverse('habits:habit_detail', args=(self.habit.pk, )))

        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data["place"], self.habit.place)

        self.assertEqual(str(Habit.objects.get(user=self.user.pk)),
                         "Жим штанги")

    def test_habit_update(self):

        field = {"reward": "Сходить в душ"}

        response = self.client.patch(
            reverse('habits:habit_update', args=(self.habit.pk, )), field)

        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data["reward"], "Сходить в душ")

    def test_habit_destroy(self):

        response = self.client.delete(
            reverse('habits:habit_delete', args=(self.habit.pk, )))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_validators(self):

        data = {"duration_time": 200}

        response = self.client.patch(
            reverse('habits:habit_update', args=(self.habit.pk, )), data)

        self.assertEqual(
            response.json()["duration_time"],
            ['Время выполнения привычки должно быть не более 120 секунд!'])

        data = {"duration_time": 0}

        response = self.client.patch(
            reverse('habits:habit_update', args=(self.habit.pk, )), data)

        self.assertEqual(
            response.json()["duration_time"],
            ['Время выполнения привычки не может равняться нулю!'])

        data = {"periodicity": 10}

        response = self.client.patch(
            reverse('habits:habit_update', args=(self.habit.pk, )), data)

        self.assertEqual(
            response.json()["periodicity"],
            ['Нельзя выполнять привычку реже, чем 1 раз в 7 дней!'])

        data = {"periodicity": 0}

        response = self.client.patch(
            reverse('habits:habit_update', args=(self.habit.pk, )), data)

        self.assertEqual(
            response.json()["periodicity"],
            ['Периодичность выполнения не может быть меньше или равна нулю!'])

    def test_habit_validator(self):

        data = {
            "place": "Тест",
            "time": "12:00",
            "action": "Тест валидатора",
            "periodicity": "1",
            "reward": "Сдать тест",
            "duration_time": 60
        }

        response = self.client.post(reverse('habits:habit_create'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = {"related_habit": self.habit.pk, "reward": "Отдохнуть"}

        response = self.client.patch(
            reverse('habits:habit_update', args=(self.habit.pk, )), data)

        self.assertEqual(response.json()['non_field_errors'], [
            'Нельзя одновременно выбрать связанную привычку и вознаграждение'
        ])

        data = {"related_habit": self.habit.pk, "is_nice_habit": False}

        response = self.client.patch(
            reverse('habits:habit_update', args=(self.habit.pk, )), data)

        self.assertEqual(response.json()['non_field_errors'], [
            'В связанные привычки могут попадать только привычки с признаком приятной привычки'
        ])

        data = {"is_nice_habit": True, "reward": "Отдохнуть"}

        response = self.client.patch(
            reverse('habits:habit_update', args=(self.habit.pk, )), data)

        self.assertEqual(response.json()['non_field_errors'], [
            'У приятной привычки не может быть связанной привычки или вознаграждения'
        ])
