from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from home.customer import Customer  # Importing Customer model

@receiver(post_save, sender=User)
def create_or_update_customer_profile(sender, instance, created, **kwargs):
    if created:
        # Create a Customer profile for new users
        Customer.objects.create(user=instance)
    else:
        # Save the existing Customer profile if it exists
        if hasattr(instance, "customer"):
            instance.customer.save()
