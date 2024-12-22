from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1


@admin.register(Room)
class RoomAdmin(TranslationAdmin):
    inlines = [RoomImageInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Hotel)
class HotelAdmin(TranslationAdmin):
    inlines = [HotelImageInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
admin.site.register(Review)
admin.site.register(Booking)
admin.site.register(Country)
