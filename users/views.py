from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import User
# from rest_framework.response import Response
# from .serializers import UserProfileUser
# from rest_framework import viewsets
# from rest_framework.permissions import (AllowAny,IsAuthenticated)
# from rest_framework.views import APIView
# from .permissions import IsLoggedInUserOrAdmin,IsAdminUser


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserProfileUser
#     def get_permissions(self):
#         permission_classes=[]
#         if self.action=='create':
#             permission_classes={AllowAny}
#         elif self.action=='retrive' or self.action== 'update' or self.action=='delete':
#             permission_classes=[IsLoggedInUserOrAdmin]
#
#         elif self.action=='list' or self.action=='destroy':
#             permission_classes=[IsAdminUser]
#
#         return [permission() for permission in permission_classes]







def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


