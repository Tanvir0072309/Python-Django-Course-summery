from django.contrib import admin
from data.models import Catch  # Ensure the import is correct

# Register your model to be accessible in the Django Admin
admin.site.register(Catch)