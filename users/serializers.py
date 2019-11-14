# from rest_framework import serializers
# from .models import User
#
#
# class UserProfileUser(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=('url','email','first_name','last_name','password')
#         extra_kwargs={'password':{'write_only':True}}
#
#         def create(self,validated_data):
#             password=validated_data.pop('password')
#             user=User(**validated_data)
#             user.username=validated_data.get('email')
#             user.set_password(password)
#             user.save()
#             return user
#
