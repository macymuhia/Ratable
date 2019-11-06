from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Role(models.Model):
    '''
    The Role entries are managed by the admin and define the role a user takes.
    '''
    ADMIN = 1
    MANAGER = 2
    STAFF = 3
    ROLE_CHOICES = (
      (MANAGER, 'staff'),
      (STAFF, 'staff'),
      (ADMIN, 'admin'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True, blank=True)

    def __str__(self):
      return self.get_id_display()
      
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

      def __str__(self):
        return self.user.username

    @receiver(post_save, sender = User) 
    def create_profile(instance,sender,created, **kwargs):
        if created:
            Profile.objects.create(user = instance)

    @receiver(post_save, sender= User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        instance.profile.save()
