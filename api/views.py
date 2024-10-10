from django.shortcuts import render, get_object_or_404
from .models import Group, Faculty, Theme, Practise
from .serializers import GroupSerializer, FacultySerializer, ThemeSerializer, PractiseSerializer, PractiseUpdateSerializer, GetOnlyPdfSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView


class CreatePractiseView(CreateAPIView):
    queryset = Practise.objects.all()
    serializer_class = PractiseSerializer

class UpdatePractiseView(RetrieveUpdateAPIView):
    queryset = Practise.objects.all()
    serializer_class = PractiseUpdateSerializer

class GetPractiseView(RetrieveUpdateAPIView):
    queryset = Practise.objects.all()
    serializer_class = PractiseSerializer

class GroupView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class FacultyView(ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class ThemeView(ListAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

class GetOnlyPdf(RetrieveAPIView):
    queryset = Practise.objects.all()
    serializer_class = GetOnlyPdfSerializer

def practise_detail(request, id):
    practise_data = get_object_or_404(Practise, id=id)

    text = f'{practise_data.author} {practise_data.theme}'

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    text = text.lower()
    key = 'sodiq'
    
    encrypted = ''.join(
        alphabet[(alphabet.index(t) + alphabet.index(key[i % len(key)])) % len(alphabet)] 
        if t in alphabet else t
        for i, t in enumerate(text)
    )

    context = {
        'data': practise_data,
        'camera_pdf_url': practise_data.camera_pdf.url,
        'cipher_text': encrypted
    }

    return render(request, 'detail.html', context)

def check_file(request):
    return render(request, 'decyrpt.html')