from rest_framework import serializers
from .models import *
from oauth2_provider.models import AccessToken


class CustomerTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class CustomerProfileSerializer(serializers.ModelSerializer):

    contact_number = serializers.SerializerMethodField()

    @staticmethod
    def get_contact_number(obj):
        q = Profile.objects.filter(user=obj).last()
        if q:
            return q.contact_number
        else:
            return '-'

    cover_letter = serializers.SerializerMethodField()

    @staticmethod
    def get_cover_letter(obj):
        q = Profile.objects.filter(user=obj).last()
        if q:
            if q.cover_letter:
                return q.cover_letter.url
            else:
                return '-'
        else:
            return '-'

    resume = serializers.SerializerMethodField()

    @staticmethod
    def get_resume(obj):
        q = Profile.objects.filter(user=obj).last()
        if q:
            if q.resume:
                return q.resume.url
            else:
                return '-'
        else:
            return '-'

    class Meta:
        model = User
        fields = ('id', 'first_name', 'username', 'email', 'contact_number', 'cover_letter', 'resume')
