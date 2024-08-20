from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserProfile


class TestUserProfileModel(TestCase):
    def test_user_profile_got_created(self):
        user = get_user_model().objects.create(username="dummee")
        self.assertTrue(UserProfile.objects.filter(user=user).exists())
