from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.serializers import ValidationError

from posts.models import Follow, Group, Comment, Post, User


class UsernameRelatedPk(serializers.Field):
    def to_representation(self, value):
        return value.username

    def to_internal_value(self, data):
        data = get_object_or_404(User, username=data)
        if data == self.context.get('request').user:
            raise ValidationError('You can\'t subscribe to yourself')
        return data


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.CharField()

    class Meta:
        model = Follow
        fields = ('user', 'following')

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='The subscription must be unique'
            )
        ]

    def validate_following(self, value):
        value = get_object_or_404(User, username=value)
        if value == self.context.get('request').user:
            raise ValidationError('You can\'t subscribe to yourself')
        return value


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)
