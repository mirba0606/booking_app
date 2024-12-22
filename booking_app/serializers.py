from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name',]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name',]


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_images']


class RoomListSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_status', 'room_type', 'room_price','room_images']


class RoomDetailSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True)


    class Meta:
        model = Room
        fields = [ 'room_number', 'room_status', 'room_type', 'room_price', 'all_inclusive',
                   'room_description', 'room_images']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user_name = UserProfileSimpleSerializer()
    class Meta:
        model = Review
        fields = ['id','user_name', 'text', 'parent', 'stars']


class HotelListSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'city', 'hotel_address', 'hotel_stars', 'hotel_images', 'avg_rating', 'count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
         return obj.get_count_people()


class CountryDetailSerializersAPIView(serializers.ModelSerializer):
    hotels = HotelListSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['country_name', 'hotels']


class HotelDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    owner = UserProfileSimpleSerializer()
    created_date = serializers.DateField(format('%d-%m-%Y'))
    hotel_images = HotelImageSerializer(many=True,read_only=True)
    rooms = RoomListSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True,read_only=True)

    class Meta:
        model = Hotel
        fields = [ 'hotel_name', 'description', 'country','city', 'hotel_images',
                   'hotel_video','owner','hotel_address', 'hotel_stars','created_date', 'rooms', 'reviews']


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

