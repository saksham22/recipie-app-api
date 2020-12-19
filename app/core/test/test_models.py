from django.test import TestCase

from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    def test_create_user_with_email_sucessful(self):
        """ Test Creating a new user with an email is sucessfull"""
        email = "test@gmail.com"
        password = "Testpass123"
        user = get_user_model().object.create_user(email=email,password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_email_normalized(self):
        """ Test the email for a new user is normalized"""
        email = "test@gmail.com"
        user = get_user_model().object.create_user(email,'test123')
        self.assertTrue(user.email ,email.lower())


    def test_new_user_invalid_email(self):
        """ Test the email for a new user is validated"""
        with self.assertRaises(ValueError):
            get_user_model().object.create_user(None,'test123')

    def test_create_new_superuser(self):
        """ Test the email for create new super user"""
        user = get_user_model().object.create_superuser('test@gmail.com','test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
