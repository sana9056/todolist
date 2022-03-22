from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import todoapp, todolist
from .serializers import todoappModelSerializer, todolistModelSerializer
from .paginations import todoappPageNumberPagination, todolistPageNumberPagination


class todoappModelViewSet(ModelViewSet):
    queryset = todoapp.objects.all()
    serializer_class = todoappModelSerializer
    pagination_class = todoappPageNumberPagination

    def get_queryset(self):
        name = self.request.query_params.get('name', '')

        if name:
            self.queryset = self.queryset.filter(name__contains=name)
        return self.queryset


class todolistModelViewSet(ModelViewSet):
    queryset = todolist.objects.all()
    serializer_class = todolistModelSerializer
    pagination_class = todolistPageNumberPagination

    def get_queryset(self):
        todoapp = self.request.query_params.get('todoapp', '')
        date_qt = self.request.query_params.get('date_qt', '')
        date_lt = self.request.query_params.get('date_lt', '')
        if todoapp:
            self.queryset = self.queryset.filter(todoapp__name=todoapp)
        if date_qt and date_lt:
            self.queryset = self.queryset.filter(created__gt=date_qt, created__lt=date_lt)

        return self.queryset

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)