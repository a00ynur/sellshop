from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from account.api.serializers import UserSerializer

USER = get_user_model()


class UserProfileAPIView(RetrieveAPIView):
    queryset = USER.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user