from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE
    )
    photo = models.ImageField(
        upload_to="profile/",
        max_length=255,
        null=True,
        blank=True,
    )
    phone = models.CharField(max_length=20, blank=True, default="")
    bio = models.TextField()

    class Meta:
        permissions = [
            ("add_user", "Can add user"),
            ("change_user", "Can change user"),
            ("delete_user", "Can remove a user"),
        ]

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()


class CustomGroup(Group):

    class Meta:
        proxy = True
        permissions = [
            ("add_group", "Can add group"),
            ("change_group", "Can change group"),
            ("delete_group", "Can remove a group"),
        ]
