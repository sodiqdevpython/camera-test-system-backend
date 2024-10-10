from django.urls import path
from .views import CreatePractiseView, GroupView, FacultyView, ThemeView, UpdatePractiseView, GetPractiseView, practise_detail, GetOnlyPdf, check_file

urlpatterns = [
    path('create-practise/', CreatePractiseView.as_view()),
    path('update/<str:pk>/', UpdatePractiseView.as_view()),
    path('practise/<str:pk>/', GetPractiseView.as_view()),
    path('group/', GroupView.as_view()),
    path('faculty/', FacultyView.as_view()),
    path('theme/', ThemeView.as_view()),
    path('pdf/<str:pk>/', GetOnlyPdf.as_view()),
    path('<str:id>/', practise_detail, name='practise'),
    path('', check_file, name='file')
]