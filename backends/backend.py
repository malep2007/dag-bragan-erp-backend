from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class Backend(object):
    def authenticate(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get_user(username=username)
        if user is not None:
            return True
        else:
            return False
