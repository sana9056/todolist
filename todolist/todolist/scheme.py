import graphene
from graphene_django import DjangoObjectType
from users.models import User
from project.models import todoapp, todolist


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class TodoappType(DjangoObjectType):
    class Meta:
        model = todoapp
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = todolist
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_todoapp = graphene.List(TodoappType)
    all_todolist = graphene.List(TodoType)

    def resolve_all_users(self, info):
        return User.objects.all()

    def resolve_all_todoapp(self, info):
        return todoapp.objects.all()

    def resolve_all_todolist(self, info):
        return todolist.objects.all()


scheme = graphene.Scheme(query=Query)
#Для 10 урока