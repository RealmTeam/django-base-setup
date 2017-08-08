# -*- coding: utf-8 -*-

"""This modules should contain all your serializable objects to build an api"""

from .models import MyModel
from rest_framework import serializers


# class MyModelSerializer(serializers.ModelSerializer):
#    num_amc = serializers.Field(source="amc_numero")
#    nom_amc = serializers.Field(source="amc_nom")

#    class Meta:
#        model = MyModel
#        fields = ("num_amc", "nom_amc", )
