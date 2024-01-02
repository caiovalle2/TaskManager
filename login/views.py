from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .forms import CreateUserForm

# Create your views here.
def loginview(request):
    return render(request, 'login.html')

def createuserview(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Token.objects.get_or_create(user=user)
            return redirect('/login')
    form = CreateUserForm()
    return render(request, 'criar.html', {'form': form})


class LoginApiView(APIView):
    queryset = User.objects.all()
    def post(self, request):
        data = request.data
        user = self.queryset.filter(username=data['username']).first()
        if user and user.check_password(data['password']):
            token = Token.objects.get(user=user)
            return Response({'token': token.key})
        return Response(status=status.HTTP_403_FORBIDDEN)

