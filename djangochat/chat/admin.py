from django.contrib import admin
from .models import Room, Message

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id',)
    search_fields = ('id','name')
    list_editable = ('name',)

admin.site.register(Room, RoomAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','value','user','room')
    list_display_links = ('id','room')
    search_fields = ('id','value','room')
    list_editable = ('value',)

admin.site.register(Message, MessageAdmin)