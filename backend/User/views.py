from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from django.contrib.auth.hashers import make_password, check_password
import requests
from myProject.settings import client_Id, client_secret
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# @csrf_exempt
class CustomerProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = CustomerProfileSerializer

    def list(self, request, *args, **kwargs):

        users = User.objects.exclude(is_superuser=True)

        dataCustomer = CustomerProfileSerializer(users, many=True, context={"request": request}).data

        return Response(dataCustomer, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):

        def checkUsername(uname):
            if User.objects.filter(username=uname).exists():
                return True
            else:
                return False

        def checkEmail(e):
            if User.objects.filter(email=e).exists():
                return True
            else:
                return False

        username = request.data.get('username')
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        contact_number = request.data.get('contact_number')
        cover_letter = request.data.get('cover_letter')
        resume = request.data.get('resume')

        if username is None or username == '':
            message = "username should not be empty"
            return Response({"status": "error", "message": message, "error_code": 1},
                            status=status.HTTP_400_BAD_REQUEST)

        elif password is None or password == '':
            message = "password should be at-least 8 characters long"
            return Response({"status": "error", "message": message, "error_code": 1},
                            status=status.HTTP_400_BAD_REQUEST)

        elif len(password) < 8:
            message = "password should be at-least 8 characters long"
            return Response({"status": "error", "message": message, "error_code": 2},
                            status=status.HTTP_400_BAD_REQUEST)

        # elif validate_email(email)==False:
        #     message = "not a valid email address"
        #     return Response({"status": "error" , "message": message, "error_code": 2},
        #                     status=status.HTTP_400_BAD_REQUEST)

        elif checkUsername(username) == True:
            message = "username is already reserved"
            return Response({"status": "error", "message": message, "error_code": 2},
                            status=status.HTTP_400_BAD_REQUEST)

        elif checkEmail(email) == True:
            message = "email is already reserved"
            return Response({"status": "error", "message": message, "error_code": 2},
                            status=status.HTTP_400_BAD_REQUEST)
        else:

            user = User.objects.create(username=username, password=make_password(password), email=email,
                                       first_name=name)

            profile = Profile.objects.get(user=user)
            profile.contact_number = contact_number
            profile.cover_letter = cover_letter
            profile.resume = resume
            profile.save()

            params = dict()

            params['grant_type'] = 'password'
            params['client_id'] = client_Id
            params['client_secret'] = client_secret
            params['username'] = username
            params['password'] = password

            url = request.build_absolute_uri('/auth/token/')
            response = requests.post(url, data=params)  # , headers=headers

            if response.status_code == status.HTTP_200_OK:

                dictionary = response.json()
                token = dictionary['access_token']

                dataCustomer = CustomerTokenSerializer(user, many=False,
                                                       context={"request": request, "username": user.username}).data
                return Response(dataCustomer, status=status.HTTP_200_OK)

            else:
                message = "token could not be created"
                return Response({"status": "failure", "message": message, "error_code": 2}
                                , status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a particular CustomerProfile

        """
        return super(CustomerProfileViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update a particular CustomerProfile

        """
        return super(CustomerProfileViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partial Update a particular CustomerProfile

        """
        return super(CustomerProfileViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a particular CustomerProfile

        """
        return super(CustomerProfileViewSet, self).destroy(request, *args, **kwargs)
