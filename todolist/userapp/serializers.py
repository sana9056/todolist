from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email',
                  'password', 'is_staff']
