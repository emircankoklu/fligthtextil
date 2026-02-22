#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py shell -c "
from django.contrib.auth.models import User
import os
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@flighttextile.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'Superuser {username} created.')
else:
    print(f'Superuser {username} already exists.')
"

# Populate categories if empty
python manage.py shell -c "
from gallery.models import Category
if Category.objects.count() == 0:
    categories = [
        ('Hava Kuvvetleri', 'hava-kuvvetleri'),
        ('Polis', 'polis'),
        ('Jandarma', 'jandarma'),
        ('Kara Kuvvetleri', 'kara-kuvvetleri'),
        ('Deniz Kuvvetleri', 'deniz-kuvvetleri'),
        ('DİGER', 'diger'),
    ]
    for name, slug in categories:
        Category.objects.create(name=name, slug=slug)
    print('Categories populated.')
else:
    print('Categories already exist.')
"
