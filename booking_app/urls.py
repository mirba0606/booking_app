from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'booking', BookingViewSet,  basename='booking'),
urlpatterns = [
   path('', include(router.urls)),
   path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
   path('hotels/', HotelListAPIView.as_view(), name='hotel_list'),
   path('hotels/<int:pk>/',  HotelDetailAPIView.as_view(), name='hotel_detail'),
   path('hotels/create/', HotelCreateIPIView.as_view(), name='hotel_create'),
   path('hotels/create/<int:pk>', HotelEDITAPIView.as_view(), name='hotel_edit'),
   path('rooms/',  RoomListAPIView.as_view(), name='room_list'),
   path('rooms/<int:pk>/',  RoomDetailAPIView.as_view(), name='room_detail'),
   path('rooms/create', RoomCreateAPIView.as_view(), name='room_create'),
   path('country/', CountryListAPIView.as_view(), name='country_list'),
   path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
   path('user/', UserProfileListAPIView.as_view(), name='user_list'),
   path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
   path('review/', ReviewListAPIView.as_view(), name='review_list'),
   path('review/<int:pk>/', ReviewDetailAPIView.as_view(), name='review_detail')
 ]



