from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(default="", blank=True)
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        profile = UserProfile(user=instance)
        profile.full_clean()
        profile.save()


post_save.connect(create_user_profile, sender=get_user_model())
