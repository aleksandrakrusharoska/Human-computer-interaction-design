from datetime import datetime

from django.contrib import admin

from application.models import *


# Register your models here.
class AgentAdmin(admin.ModelAdmin):
    # Агентите се прикажани со нивното име.
    list_display = ("name", "email",)

    # Агенти може да бидат додадени само од супер-корисници.
    def has_add_permission(self, request):
        return request.user.is_superuser


class CharacteristicAdmin(admin.ModelAdmin):
    # Карактеристиките се прикажани со нивното име.
    list_display = ("name", "value",)

    # Карактеристики може да бидат додадени само од супер-корисници.
    def has_add_permission(self, request):
        return request.user.is_superuser


class AgentRealEstateInline(admin.StackedInline):
    model = AgentRealEstate
    extra = 0


class CharacteristicRealEstateInline(admin.StackedInline):
    model = CharacteristicRealEstate
    extra = 0


class RealEstateAdmin(admin.ModelAdmin):
    # Недвижностите се прикажани со нивното име, површина и опис.
    list_display = ("name", "description", "area",)

    inlines = (CharacteristicRealEstateInline, AgentRealEstateInline,)

    # Огласи за продажба може да бидат додадени само од агенти.
    def has_add_permission(self, request):
        return Agent.objects.filter(user=request.user).exists()

    # Огласите можат да бидат менувани само од агенти кои се задолжени за продажба на тој оглас.
    def has_change_permission(self, request, obj=None):
        return obj and AgentRealEstate.objects.filter(real_estate=obj, agent__user=request.user).exists()

    # Oстанатите агенги може само да ги гледаат тие огласи.
    def has_view_permission(self, request, obj=None):
        return Agent.objects.filter(user=request.user).exists()

    # Еден оглас може да биде избришан само ако нема додадено ниту една карактеристика која го опишува.
    def has_delete_permission(self, request, obj=None):
        return not CharacteristicRealEstate.objects.filter(real_estate=obj).exists()

    # По автоматизам агентот кој додава оглас е еден од задолжените за продажба на таа недвижност.
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            agent = Agent.objects.filter(user=request.user).first()
            AgentRealEstate.objects.create(real_estate=obj, agent=agent)

    # На супер-корисниците во Админ панелот им се прикажуваат само огласите кои се објавени на денешен датум
    def get_queryset(self, request):
        if request.user.is_superuser:
            return RealEstate.objects.filter(date=datetime.now().date())


admin.site.register(RealEstate, RealEstateAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(Agent, AgentAdmin)
