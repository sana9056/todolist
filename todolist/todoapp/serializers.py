from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import todoapp, todolist
from userapp.serializers import UserSerializer


class todoappModelSerializer(HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(many=True)

    class Meta:
        model = todoapp
        # fields = '__all__'
        fields = ['id', 'url', 'name', 'repository', 'users']


class todolistModelSerializer(HyperlinkedModelSerializer):
    active = serializers.BooleanField(read_only=True)

    class Meta:
        model = todolist
        fields = '__all__'


class todoappModelSerializerGET(HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = todoapp
        # fields = '__all__'
        fields = ['id', 'url', 'name', 'repository', 'users']