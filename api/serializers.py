from rest_framework.serializers import ModelSerializer
from .models import Group, Faculty, Theme, Practise

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']

class FacultySerializer(ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id','name']

class ThemeSerializer(ModelSerializer):
    class Meta:
        model = Theme
        fields = ['id','name']

class PractiseSerializer(ModelSerializer):
    class Meta:
        model = Practise
        fields = '__all__'

class GetOnlyPdfSerializer(ModelSerializer):
    class Meta:
        model = Practise
        fields = ['camera_pdf']

class PractiseUpdateSerializer(ModelSerializer):
    class Meta:
        model = Practise
        fields = ['camera_pdf', 'body', 'is_valid', 'pdf']