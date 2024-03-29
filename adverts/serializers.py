from rest_framework import serializers
from .models import Advert
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from save.models import Save
from profiles.models import Profile
from django.contrib.humanize.templatetags.humanize import naturaltime


class AdvertSerializer(TaggitSerializer, serializers.ModelSerializer):
    '''
    Advert model Serializer, all fields serialized
    owner is read only, is_owner returns true/false -
    to check if the requesting user is/is not object owner.
    Get page views function- increments page views for each object
    with the help of hitcount
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    tags = TagListSerializerField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_image.url')
    page_views = serializers.SerializerMethodField()
    save_id = serializers.SerializerMethodField()
    active = serializers.ReadOnlyField()
    profile_location = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    save_count = serializers.ReadOnlyField()

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def get_profile_location(self, obj):
        try:
            return obj.owner.profile.location or "Profile's location unknown"
        except AttributeError:
            return "Profile's location unknown"

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_page_views(self, obj):
        try:
            return obj.hit_count.hits
        except AttributeError:
            pass

    def get_save_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            save = Save.objects.filter(
                owner=user, advert=obj
            ).first()
            return save.id if save else None
        return None

    # this function fully copied from CI walkthrough
    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    class Meta:
        model = Advert
        fields = '__all__'
