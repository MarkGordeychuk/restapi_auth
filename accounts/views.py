from django.contrib.auth import login

from rest_framework.permissions import AllowAny
from rest_framework.generics import get_object_or_404, RetrieveAPIView
from knox.views import LoginView as KnoxLoginView

from .models import User
from .serializers import UserSerializer, LoginSerializer


class RegisterView(KnoxLoginView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        login(request, serializer.save())
        return super().post(request, format=None)


class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super().post(request, format=None)


class UserView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        user_id = self.request.query_params.get('id', None)
        obj = get_object_or_404(queryset, id=user_id)

        self.check_object_permissions(self.request, obj)

        return obj

