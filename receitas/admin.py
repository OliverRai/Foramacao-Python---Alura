from django.contrib import admin
from .models import Receita

admin.site.register(Receita)


# criar usuario admin
# python manage.py createsuperuser