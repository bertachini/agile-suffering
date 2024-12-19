from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginViewTest(TestCase):
    def setUp(self):
        # Cria um usuário para testes
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_login_get(self):
        # Testa a requisição GET na página de login
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_post_valid(self):
        # Testa o login com credenciais válidas
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': '12345'})
        self.assertRedirects(response, reverse('lead_list'))

    def test_login_post_invalid(self):
        # Testa o login com credenciais inválidas
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertFormError(response, 'form', None, 'Invalid username or password')

