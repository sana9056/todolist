from django.contrib.auth import get_user_model
import json
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from mixer.backend.django import mixer

from userapp.models import User
from .viewsets import todoappModelViewSet
from .models import todoapp


class TesttodoappViewSetTestCase(TestCase):
    def setUp(self):
        self.super_user = get_user_model().objects.create_superuser(
            username='sana9056', email='sana9056@mail.ru', password='90569056'
        )
        self.user = get_user_model().objects.create_user(
            username='user1', email='user1@mail.ru', password='1'
        )
        self.project = {'users': ['http://127.0.0.1:8000/api/users/1/', 'http://127.0.0.1:8000/api/users/2/'],
                        'name': 'x',
                        'repository': 'https://repo.com'}

    # Тесты для  'rest_framework.permissions.IsAuthenticated'
    def test_get_list_quest(self):
        factory = APIRequestFactory()
        request = factory.get('/api/todoapp/')
        view = todoappModelViewSet.as_view({'get': 'list'})
        response = view(request)
        # print(response.render().content)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_user(self):
        factory = APIRequestFactory()
        request = factory.get('/api/todoapp/')
        force_authenticate(request, user=self.user)
        view = todoappModelViewSet.as_view({'get': 'list'})
        response = view(request)
        # print(dir(response))
        # print(response.render().content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_quest(self):
        project_data = {'name': 'todoapp', 'repository': 'Repo'}
        factory = APIRequestFactory()
        request = factory.post('api/todoapp', project_data, format='json')
        view = todoappModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        todoapp = mixer.blend(todoapp)
        factory = APIRequestFactory()
        request = factory.post('/api/todoapp', self.project, format='json')
        force_authenticate(request, user=self.super_user)
        view = todoappModelViewSet.as_view({'post': 'create'})
        response = view(request)
        print(response.render().content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user(self):
        factory = APIRequestFactory()
        request = factory.post('/api/todoapp', self.project, format='json')
        force_authenticate(request, user=self.user)
        view = todoappModelViewSet.as_view({'post': 'create'})
        response = view(request)
        print(response.render().content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TesttodoappModelViewSetAPIClient(TestCase):
    def setUp(self):
        self.super_user = get_user_model().objects.create_superuser(
            username='sana9056', email='sana9056@mail.ru', password='90569056'
        )
        self.user = get_user_model().objects.create_user(
            username='user1', email='user1@mail.ru', password='1'
        )
        self.project = {'users': ['http://127.0.0.1:8000/api/users/1/', 'http://127.0.0.1:8000/api/users/2/'],
                        'name': 'x',
                        'repository': 'https://repo.com'}

    def test_get_list_quest(self):
        client = APIClient()
        response = client.get('/api/todoapp/')
        print(response.render().content)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_user(self):
        # self.client.login(username=self.user.username,password=self.user.password)  # выдает 401
        # token = Token.objects.get(user__username=self.super_user.username)
        # client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        client = APIClient()
        client.force_authenticate(user=self.super_user)
        response = client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TesttodoappModelViewSetAPITestCase(APITestCase):
    def setUp(self):
        self.super_user = get_user_model().objects.create_superuser(
            username='sana9056', email='sana9056@mail.ru', password='90569056'
        )
        self.user = get_user_model().objects.create_user(
            username='user1', email='user1@mail.ru', password='1'
        )
        self.project = {'users': ['http://127.0.0.1:8000/api/users/1/', 'http://127.0.0.1:8000/api/users/2/'],
                        'name': 'x',
                        'repository': 'https://repo.com'}

    def test_get_list_quest(self):
        response = self.client.get('/api/todoapp/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_user(self):
        # self.client.login(username=self.user.username,password=self.user.password) # выдает 401
        self.client.force_login(self.super_user)
        response = self.client.get('/api/todoapp/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_quest(self):
        response = self.client.post('/api/todoapp/', self.project)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_user(self):
        # self.client.force_login(self.super_user)  # вроде работает, но ...
        self.client.login(username='sana9056', password='90569056')
        response = self.client.post('/api/todoapp/', self.project)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_mixer(self):   # не работает
        project = mixer.blend(todoapp)
        print(todoapp.name)
        print(todoapp.repository)
        print(todoapp.users.username)  # не работает

