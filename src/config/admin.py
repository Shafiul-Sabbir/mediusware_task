from django.contrib import admin
from . import g_model

admin.site.register(g_model.TimeStampMixin)