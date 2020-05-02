from django.contrib import admin

from .models import *
from faction.models import Faction
from yata.handy import timestampToDate


class KeyInline(admin.TabularInline):
    model = Key
    extra = 0


class KeyAdmin(admin.ModelAdmin):
    list_display = ['player', 'useFact', 'useSelf']
    search_fields = ['player__name', 'tId']
    readonly_fields = ['player', ]

class PlayerAdmin(admin.ModelAdmin):
    class Media:
        css = {'all': ('perso/css/admin.css',)}

    list_display = ['tId', 'name', 'botPerm', 'active', 'validKey', 'dId']
    search_fields = ['name', 'tId']
    list_filter = ['active', 'validKey']
    inlines = [KeyInline]
    exclude = ['apikey', 'bazaarJson', 'awardsJson', 'stocksJson']

    def last_update(self, instance):
        return timestampToDate(instance.lastUpdateTS)

    def last_action(self, instance):
        return timestampToDate(instance.lastActionTS)

# class NewsAdmin(admin.ModelAdmin):
#     list_display = ['__str__', 'date', 'type', 'authorName', 'authorId', 'read']
#     filter_horizontal = ('player',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'date', 'section', 'authorName', 'authorId']


class DonationAdmin(admin.ModelAdmin):
    list_display = ['__str__']


class PlayerDataAdmin(admin.ModelAdmin):
    list_display = ['__str__']


class ErrorAdmin(admin.ModelAdmin):
    list_display = ['player', 'short_error', 'timestamp', 'date']
    readonly_fields = ['player', ]

    def date(self, instance):
        return timestampToDate(instance.timestamp)


class SpinnerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'factionId', 'faction', 'spinner']

    def faction(self, instance):
        return Faction.objects.filter(tId=instance.factionId).first()


class TrainFullAdmin(admin.ModelAdmin):
    list_display = ['pk', 'timestamp', 'id_key']


admin.site.register(Error, ErrorAdmin)
admin.site.register(TrainFull, TrainFullAdmin)
admin.site.register(Spinner, SpinnerAdmin)
admin.site.register(Key, KeyAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Message, MessageAdmin)
# admin.site.register(News, NewsAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(PlayerData, PlayerDataAdmin)
