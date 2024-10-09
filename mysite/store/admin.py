from django.contrib import admin
from .models import *

# Register your models here.

class RegionPhotosInline(admin.TabularInline):
    model = RegionPhotos
    extra = 1

class RegionPhotosAdmin(admin.ModelAdmin):
    inlines = [RegionPhotosInline]

class PlacesPhotosInline(admin.TabularInline):
    model = PlacesPhotos
    extra = 1

class PlacesPhotosAdmin(admin.ModelAdmin):
    inlines = [PlacesPhotosInline]

class ReviewPhotosInline(admin.TabularInline):
    model = PhotosReview
    extra = 1

class ReviewPhotosAdmin(admin.ModelAdmin):
    inlines = [ReviewPhotosInline]



class AttractionPhotosInline(admin.TabularInline):
    model = AttractionsPhotos
    extra = 1

class AttractionPhotosAdmin(admin.ModelAdmin):
    inlines = [AttractionPhotosInline]

class KitchenPhotosInline(admin.TabularInline):
    model = KitchenPhotos
    extra = 1

class KitchenPhotosAdmin(admin.ModelAdmin):
    inlines = [KitchenPhotosInline]

class ReviewAttractionsPhotosInline(admin.TabularInline):
    model = PhotosReviewAttraction
    extra = 1

class ReviewAttractionsPhotosAdmin(admin.ModelAdmin):
    inlines = [ReviewAttractionsPhotosInline]


class ReviewKitchenPhotosInline(admin.TabularInline):
    model = PhotosReviewKitchen
    extra = 1

class ReviewKitchenPhotosAdmin(admin.ModelAdmin):
    inlines = [ReviewKitchenPhotosInline]

class ReviewHotelPhotosInline(admin.TabularInline):
    model = PhotosReviewHotel
    extra = 1

class ReviewHotelPhotosAdmin(admin.ModelAdmin):
    inlines = [ReviewHotelPhotosInline]

class ConditionsInline(admin.TabularInline):
    model = Conditions
    extra = 1

class OfferedAmenitiesInline(admin.TabularInline):
    model = Offered_amenities
    extra = 1

class SafetyInline(admin.TabularInline):
    model = Safety_and_hydigene
    extra =1

class HotelPhotosInline(admin.TabularInline):
    model = HotelPhotos
    extra = 1

class HotelListAdmin(admin.ModelAdmin):
    inlines = [ConditionsInline, OfferedAmenitiesInline, SafetyInline, HotelPhotosInline]


# class HotelPhotosAdmin(admin.ModelAdmin):
#     inlines = [HotelPhotosInline]
#
admin.site.register(Hotel, HotelListAdmin)


admin.site.register(Region, RegionPhotosAdmin)
admin.site.register(UserProfile)
admin.site.register(RegionFood)
admin.site.register(Places, PlacesPhotosAdmin)
# admin.site.register(Hotel, HotelPhotosAdmin)
admin.site.register(Kitchen, KitchenPhotosAdmin)
admin.site.register(Attractions, AttractionPhotosAdmin)
admin.site.register(Culture)
admin.site.register(Games)
admin.site.register(NationalFood)
admin.site.register(HandCrafts)
admin.site.register(Currency)
admin.site.register(NationalInstruments)
admin.site.register(NationalClothes)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Review, ReviewPhotosAdmin)
admin.site.register(ReviewHotel, ReviewHotelPhotosAdmin)
admin.site.register(ReviewKitchen, ReviewKitchenPhotosAdmin)
admin.site.register(ReviewAttraction, ReviewAttractionsPhotosAdmin)
admin.site.register(Address)


