from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Company, CompanyProfile, Accessibility, GuideLine
from activity.models import ActivityProfile, Difficulty
from accounts.serializers import MyUserCustomSerializer, MyUserSerializer
from gallery.serializers import GallerySerializers


# Serializers for Company model
class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"



class CompanySafeSerializer(ModelSerializer):
    user = MyUserSerializer()

    class Meta:
        model = Company
        fields = "__all__"



# Serializers for CompanyProfile model
class CompanyProfileSerializer(ModelSerializer):

    class Meta:
        model = CompanyProfile
        fields = "__all__"



class CompanyProfileSafeSerializer(ModelSerializer):
    company = CompanySerializer()
    profile_image = GallerySerializers()
    cover_image = GallerySerializers()

    class Meta:
        model = CompanyProfile
        fields = "__all__"


# Serializers for Accessibility model
class AccessibilitySerializer(ModelSerializer):
    
    class Meta:
        model = Accessibility
        fields = "__all__"

# Serializers for GuideLine model
class GuideLineSerializer(ModelSerializer):

    class Meta:
        model = GuideLine
        fields = "__all__"


# Custom Serializers for CompanyProfile model
class DifficultyCustomSerializer(ModelSerializer):

    class Meta:
        model = Difficulty
        fields = ["title"]


class GalleryCustomSerializer(serializers.Serializer):
    image = serializers.ImageField()

class ActivityThemeCustomSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)

class ActivityTypeCustomSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)


class ActivityProfileSerializer(serializers.Serializer):
        main_image =  GalleryCustomSerializer()
        minimum_participant = serializers.IntegerField()
        maximum_participant = serializers.IntegerField()
        duration = serializers.IntegerField()
        difficulty = DifficultyCustomSerializer()
        mimimum_age = serializers.IntegerField()
        title = serializers.CharField(max_length=200)
        short_description = serializers.CharField(max_length=150)
        price = serializers.DecimalField(max_digits=7, decimal_places=2)
        activity_theme = ActivityThemeCustomSerializer(many=True)
        activity_type = ActivityTypeCustomSerializer()

class CompanyDetailsSerializer(ModelSerializer):
    
    activity_profiles  = ActivityProfileSerializer(source='getActivities.activity_profiles', many=True)
    available_escape_game  = serializers.IntegerField(source='getActivities.total_activities')
    lowest_age  = serializers.IntegerField(source='getActivities.lowest_age')
    average_minimum_participant  = serializers.IntegerField(source='getActivities.average_minimum_participant')
    average_maximum_participant  = serializers.IntegerField(source='getActivities.average_maximum_participant')
    highest_accompany_age  = serializers.IntegerField(source='getActivities.highest_accompany_age')
    average_game_duration  = serializers.IntegerField(source='getActivities.average_game_duration')
    gallery = GallerySerializers(source='getAllRelatedGalleryItems', many=True)
    profile_image = GallerySerializers()
    cover_image = GallerySerializers()

    class Meta:
        model = CompanyProfile
        fields = [
            'id',
            'city', 
            'state', 
            'title', 
            'cover_image',
            'profile_image',
            'available_escape_game',
            'about',
            'address_line',
            'website_url',
            'phone_number', 
            'lowest_age',
            'average_game_duration',
            'highest_accompany_age',
            'average_maximum_participant',
            'average_minimum_participant',
            'activity_profiles', 
            'gallery',
        ]


# Custom Serializers for CompanyProfile model

