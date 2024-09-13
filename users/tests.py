from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            name="Тест",
            email="testuser@example.com",
            telegram_chat_id=1234567,
            is_active=True,
        )
        self.user.set_password('test123')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        data = {
            "name": "Тест2",
            "email": "testuser2@example.com",
            "telegram_chat_id": 7654321,
            "password": '123test'
        }
        response = self.client.post(reverse('users:user_create'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)

    def test_user_update(self):
        field = {"name": "ТестХ", "password": 'test12345'}
        response = self.client.patch(
            reverse('users:user_update', args=(self.user.pk, )), field)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "ТестХ")

    def test_user_retrieve(self):
        response = self.client.get(
            reverse('users:user_detail', args=(self.user.pk, )))
        data = response.json()
        result = {
            'id': self.user.pk,
            'name': 'Тест',
            'email': 'testuser@example.com',
            'is_active': True,
            'telegram_chat_id': '1234567',
            'avatar': 'http://testserver/media/users/no_avatar.png'
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
        self.assertEqual(str(User.objects.get(email="testuser@example.com")),
                         "testuser@example.com")

    def test_user_destroy(self):
        response = self.client.delete(
            reverse('users:user_delete', args=(self.user.pk, )))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 0)
