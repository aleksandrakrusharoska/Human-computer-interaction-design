import random

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from application.models import Baker, Cake


# Кога се брише пекарот, неговите торти по случаен избор се додаваат на останатите пекари.
@receiver(pre_delete, sender=Baker)
def my_handler(sender, instance, **kwargs):
    cakes = Cake.objects.filter(baker=instance)

    other_bakers = Baker.objects.exclude(id=instance.id).all()

    for cake in cakes:
        new_baker = random.choice(other_bakers)
        cake.baker = new_baker
        cake.save()


