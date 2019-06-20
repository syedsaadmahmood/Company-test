from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, db_index=True, related_name="customer_user", on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=256, null=True)
    cover_letter = models.FileField(null=True, blank=True, default=None)
    resume = models.FileField(null=True, blank=True, default=None)
    is_removed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    modified_on = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return str(self.user.id)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)