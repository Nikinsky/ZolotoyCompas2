from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets, status, generics, permissions
from rest_framework.views import APIView
from .serializers import *
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter





class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        return Response({
            'user': {
                'email': user.email,
                'username': user.username,
                'token': str(token.access_token),
            }
        }, status=status.HTTP_201_CREATED)


# class CustomLoginView(TokenObtainPairView):
#     serializer_class = LoginSerializers
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         try:
#             serializer.is_valid(raise_exception=True)
#         except Exception:
#             return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)
#
#         user = serializer.valdated_dataa
#         refresh = RefreshToken.for_user(user)
#         response = HttpResponseRedirect(reverse('places_list'))
#         response.set_cookie('token', str(refresh.access_token))
#         return response

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Получаем пользователя после валидации
        user = serializer.validated_data['user']

        # Генерируем JWT токен
        token = RefreshToken.for_user(user)

        return Response({
            'email': user.email,
            'username': user.username,
            'token': str(token.access_token),
        }, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)







class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializers
    queryset1 = Address.objects.all()

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# class UserProfileView(viewsets.ModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializers


class AddressView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = AddressSerializer















class RegionView(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializers


class RegionPhotosView(viewsets.ModelViewSet):
    queryset = RegionPhotos.objects.all()
    serializer_class = RegionPhotosSerializers


class RegionFoodView(viewsets.ModelViewSet):
    queryset = RegionFood.objects.all()
    serializer_class = RegionFoodSerializers







class PlacesViewSet(viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializers



class PlacesPhotosView(viewsets.ModelViewSet):
    queryset = PlacesPhotos.objects.all()
    serializer_class = PlacesPhotosSerializers

class PlacesListView(viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlacesListSerializers
    filterset_class = PlacesFilter

class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_class = ReviewPlacesFilter









class AttractionsView(viewsets.ModelViewSet):
    queryset = Attractions.objects.all()
    serializer_class = AttractionSerializers
    filterset_class = AttractionFilter


class ReviewAttractionView(viewsets.ModelViewSet):
    queryset = ReviewAttraction.objects.all()
    serializer_class = ReviewAttractionSerializer
    filterset_class = ReviewAttractionFilter


class AttractionListView(viewsets.ModelViewSet):
    queryset = Attractions.objects.all()
    serializer_class = AttractionListSerializers
    filterset_class = AttractionFilter


class AttractionSimpleListView(viewsets.ModelViewSet):
    queryset = Attractions.objects.all()
    serializer_class = AttractionSimpleListSerializers
    filterset_class = AttractionFilter






class HotelView(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers


class ReviewHotelView(viewsets.ModelViewSet):
    queryset = ReviewHotel.objects.all()
    serializer_class = ReviewHotelSerializer
    filterset_class = ReviewHotelFilter

class HotelListView(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializers
    filterset_class = HotelFilter







class KitchenView(viewsets.ModelViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenSerializers

class ReviewKitchenView(viewsets.ModelViewSet):
    queryset = ReviewKitchen.objects.all()
    serializer_class = ReviewKitchenSerializers
    filterset_class = ReviewKitchenFilter

class KitchenListView(viewsets.ModelViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenListSerializers
    filterset_class = KitchenFilter












class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers

class CartItemsView(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializers












class CultureView(viewsets.ModelViewSet):
    queryset = Culture.objects.all()
    serializer_class = CultureSerializers


class GamesView(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializers


class NationalClothesView(viewsets.ModelViewSet):
    queryset = NationalClothes.objects.all()
    serializer_class = NationalClothesSerializers


class HandCraftSerializers(viewsets.ModelViewSet):
    queryset = HandCrafts.objects.all()
    serializer_class = HandCraftsSerializers


class CurrencyView(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializers


class NationalInstrumentsView(viewsets.ModelViewSet):
    queryset = NationalInstruments.objects.all()
    serializer_class = NationalInstrumentsSerializers

class NationalFoodView(viewsets.ModelViewSet):
    queryset = NationalFood.objects.all()
    serializer_class = NationalFoodSerializers