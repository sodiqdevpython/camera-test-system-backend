from django.db import models
from utils.models import BaseModel

class Group(BaseModel):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Gurux"
        verbose_name_plural = "Guruxlar"
        ordering = ['name']

class Faculty(BaseModel):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Fakultet"
        verbose_name_plural = "Fakultetlar"
        ordering = ['name']

class Theme(BaseModel):
    name = models.CharField(max_length=1024, unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Mavzu"
        verbose_name_plural = "Mavzular"
        ordering = ['name']

class Practise(BaseModel):
    faculty = models.ForeignKey('api.Faculty', on_delete=models.CASCADE, null=True, blank=True)
    theme = models.ForeignKey('api.Theme', on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey('api.Group', on_delete=models.CASCADE, null=True, blank=True)
    author = models.CharField(max_length=128, null=True, blank=True)
    camera_pdf = models.FileField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    pdf = models.FileField(null=True, blank=True)
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author}'
    
    class Meta:
        verbose_name = "Amaliyot"
        verbose_name_plural = "Amaliyotlar"
