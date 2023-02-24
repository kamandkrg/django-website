from django.contrib.auth import get_user_model
from django.test import TestCase

class UsersTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user('kamand', 'kamandkargar@gmail.com', '+989123456789', '1234')
        self.assertEqual(user.email, 'kamandkargar@gmail.com')
        self.assertEqual(user.username, 'kamand')
        self.assertEqual(user.phone, '+989123456789')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNotNone(user.username)
            self.assertIsNotNone(user.email)
            self.assertIsNotNone(user.phone)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(TypeError):
            User.objects.create_user(email='kamandkargar@gmail.com', username='')
        with self.assertRaises(TypeError):
            User.objects.create_user(email='kamandkargar@gmail.com', username='kamand', phone='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', username='kamandkrg', phone='+989123456789', password='12345')
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email='kamandkrg@gmail.com', username='kamandkrg', phone='+7894523025487523', password='12345'
            )

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email="super@user.com", username='kamand', phone="+989123456789", password='1234'
        )
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNotNone(admin_user.username)
            self.assertIsNotNone(admin_user.email)
            self.assertIsNotNone(admin_user.phone)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", username='kamand', phone='+989123456789', password="1234", is_superuser=False)