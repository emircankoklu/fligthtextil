import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from gallery.models import Category

categories = ['Soldier', 'Police', 'Gendarme', 'Souvenirs', 'Materials']

for cat_name in categories:
    slug = slugify(cat_name)
    Category.objects.get_or_create(name=cat_name, slug=slug)
    print(f"Ensured category: {cat_name}")
