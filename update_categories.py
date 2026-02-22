import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from gallery.models import Category

# Renames map: Old Name -> New Name
renames = {
    'Soldier': 'Hava Kuvvetleri',
    'Gendarme': 'Jandarma',
    'Police': 'Polis'
}

# Deletes list
deletes = ['Souvenirs', 'Materials', 'Admin']

# Apply Renames
for old, new in renames.items():
    try:
        cat = Category.objects.get(name=old)
        cat.name = new
        cat.slug = slugify(new)
        cat.save()
        print(f"Renamed '{old}' to '{new}'")
    except Category.DoesNotExist:
        print(f"Category '{old}' not found (skipping rename)")

# Apply Deletes
for name in deletes:
    try:
        cat = Category.objects.get(name=name)
        cat.delete()
        print(f"Deleted category '{name}'")
    except Category.DoesNotExist:
        print(f"Category '{name}' not found (skipping delete)")

print("Category updates completed.")
