from django.http import response
from django.test import TestCase 
from django.urls import reverse
from django.contrib.auth import get_user_model, login
from .models import CustomUser
# Create your tests here.

class costum_user_tests(TestCase):


    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="am",
            email = 'am@gmail.com',
            password = '0000'
        )
    
    def test_sighnUp(self):
        
        response = self.client.post(reverse("signup"),
            {
            'email' : 'am@gmail.com',
           'password' :'0000'
            })
        self.assertEqual(response.status_code, 200)  


    def test_login(self):
        url = reverse('login')
        actual_status_code = self.client.get(url).status_code
        self.assertEqual(actual_status_code, 200)

