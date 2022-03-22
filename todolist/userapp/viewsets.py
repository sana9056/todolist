from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins

from .models import User
from .serializers import UserSerializer



class UserGenericViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]