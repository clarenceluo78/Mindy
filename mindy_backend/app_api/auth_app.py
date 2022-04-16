from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import *


class AppAuth(BaseAuthentication):
    '''自定义认证类'''

    def authenticate(self, request):
        token = request.query_params.get('token')
        # print(token)
        if token:
            # 如果请求url中携带有token参数
            user_obj = AppUserToken.objects.filter(token=token).first()
            if user_obj:
                # print("ok")
                # token 是有效的，返回一个元组
                return user_obj.user, token  # request.user, request.auth
            else:
                # raise AuthenticationFailed('无效的token')
                return None
        else:
            # raise AuthenticationFailed('请求的URL中必须携带token参数')
            return None


class AppMustAuth(BaseAuthentication):
    '''自定义认证类'''

    def authenticate(self, request):
        token = request.query_params.get('token')
        # print(token)
        if token:
            # 如果请求url中携带有token参数
            user_obj = AppUserToken.objects.filter(token=token).first()
            if user_obj:
                # print("ok")
                # token 是有效的，返回一个元组
                return user_obj.user, token  # request.user, request.auth
            else:
                raise AuthenticationFailed(_('无效的token'))
                # return None
        else:
            raise AuthenticationFailed(_('请求的URL中必须携带token参数'))
            # return None