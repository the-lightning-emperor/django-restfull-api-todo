from pyexpat import model
from attr import fields
from rest_framework import serializers
import attr
from attr import fields

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
