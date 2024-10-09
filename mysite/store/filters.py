from django_filters import FilterSet
from .models import *


class PlacesFilter(FilterSet):
    class Meta:
        model = Places
        fields = {
            'region_places': ['exact'],
            'places_name': ['exact'],
        }


class ReviewPlacesFilter(FilterSet):
    class Meta:
        model = Review
        fields = {
            'places': ['exact'],
        }





class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'places': ['exact'],
            'hotel_name': ['exact'],
        }


class ReviewHotelFilter(FilterSet):
    class Meta:
        model = ReviewHotel
        fields = {
            'hotel': ['exact']
        }






class KitchenFilter(FilterSet):
    class Meta:
        model = Kitchen
        fields = {
            'places': ['exact'],
            'name_kitchen': ['exact'],
        }


class ReviewKitchenFilter(FilterSet):
    class Meta:
        model = ReviewKitchen
        fields = {
            'kitchen': ['exact'],
        }







class AttractionFilter(FilterSet):
    class Meta:
        model = Attractions
        fields = {
            'att_region': ['exact'],
            'at_name': ['exact'],
        }

class ReviewAttractionFilter(FilterSet):
    class Meta:
        model = ReviewAttraction
        fields = {
            'attractions': ['exact'],
        }