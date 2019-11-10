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

    id = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, primary_key=True, blank=True)

    def __str__(self):
        return self.get_id_display()


class Permission(models.Model):
    '''
    The Permission entries are managed by the role cateory in the roles class.
    '''

    class Meta:
        permissions = [
            ("add_user_staff", "Can add a staff Member"),
            ("delete_user_staff", "Can remove a staff Member"),
            ("update_user_staff", "Can update a staff Member"),
            ("add_manager_staff", "Can add a Line Manager"),
            ("delete_manager_staff", "Can remove a Line Manager"),
            ("update_manager_staff", "Can update a Line Manager"),
            ("add_admin_staff", "Can add an Admin"),
            ("delete_admin_staff", "Can remove an Admin"),
            ("update_admin_staff", "Can update an Admin"),
            ("add_department", "Can add a Departnment"),
            ("delete_department", "Can remove a Departnment"),
            ("update_department", "Can update a Departnment"),
            ("assign_manager_department", "Can assign a manager for a Departnment"),
            ("remover_manager_departmet", "Can remove a manager from a Department"),
            ("add_review_area", "Can add an area for the employee review"),

            ("edit_review_area", "Can edit an area for the employee review"),
            ("delete_review_area", "Can delete an area for the employee review"),
            ("add_indicator_item", "Can add an indicator for the employee review"),
            ("edit_indicator_item",
             "Can edit an indicatorindicator for the employee review"),
            ("delete_indicator_item", "Can delete an indicator for the employee review"),
            ("close_task", "Can remove a task by setting its status as closed"),
        ]


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

    @receiver(post_save, sender=User)
    def create_profile(instance, sender, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        instance.profile.save()
