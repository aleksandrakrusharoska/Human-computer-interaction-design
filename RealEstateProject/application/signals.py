from django.db.models.signals import pre_save
from django.dispatch import receiver

from application.models import *


# Кога еден недвижнина ќе се означи како продадена,
# потребно е сите агенти поврзани со неа да ја инкрементираат својата продажба.
@receiver(pre_save, sender=RealEstate)
def handle_saving_house(sender, instance, **kwargs):
    old_instance = sender.objects.filter(pk=instance.pk).first()
    if old_instance:
        if old_instance.sold != instance.sold:
            agents_real_estate = AgentRealEstate.objects.filter(real_estate=old_instance).all()
            for agent_real_estate in agents_real_estate:
                agent = agent_real_estate.agent
                agent.total_sales += 1
                agent.save()
