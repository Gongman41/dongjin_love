from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.contrib.auth import update_session_auth_hash, get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer

class UserRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=20)
    # 다른 추가 필드도 여기에 추가할 수 있음
    def custom_signup(self, request, user):
        user.nickname = self.validated_data.get('nickname', '')
        # 추가 필드에 대한 처리도 여기에 추가할 수 있음
        user.save(update_fields=['nickname'])

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        # 추가 필드에 대한 처리도 여기에 추가할 수 있음
        return data_dict

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
