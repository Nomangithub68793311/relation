from rest_framework import serializers
from Signup.models import User
from django.contrib.auth.hashers import make_password

class Adddataserializer(serializers.ModelSerializer):
       class Meta:
        model = User
        fields = "__all__"
       # validate_password = make_password
       # def create(self, validated_data):
       #  password = validated_data.pop('password', None)
       #  instance = self.Meta.model(**validated_data)
       #  if password is not None:
       #      User.make_password(password)
       #  User.save()
       #  return instance