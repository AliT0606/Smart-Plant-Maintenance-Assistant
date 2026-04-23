import os
import django
import sys
from datetime import timedelta
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "akilli_bahce.settings")
django.setup()

from django.contrib.auth.models import User
from bahce.models import Plant, Task, Note

def populate_dummy_data():
    user = User.objects.first()
    if not user:
        # Create a default user if none exists
        user = User.objects.create_user('testuser', 'test@example.com', 'password123')
        user.first_name = "Ahmet"
        user.save()
        print("Test kullanıcısı oluşturuldu.")

    # Check if plants already exist
    if Plant.objects.filter(user=user).exists():
        print(f"{user.username} kullanıcısının zaten bitkileri var. Temizleniyor...")
        Plant.objects.filter(user=user).delete()

    print(f"{user.username} kullanıcısına bitkiler ekleniyor...")

    # Create plants
    plant1 = Plant.objects.create(
        user=user,
        name="Barış Çiçeği",
        species="Spathiphyllum",
        plant_type="salon",
        location="Oturma Odası",
        water_frequency="3_gunde",
        light_need="dolayli",
        is_healthy=True,
        last_watered=timezone.now() - timedelta(days=2),
        last_fertilized=timezone.now() - timedelta(days=20)
    )

    plant2 = Plant.objects.create(
        user=user,
        name="Deve Tabanı",
        species="Monstera Deliciosa",
        plant_type="tropikal",
        location="Yatak Odası",
        water_frequency="haftada",
        light_need="yari_golge",
        is_healthy=True,
        last_watered=timezone.now() - timedelta(days=5),
        last_fertilized=timezone.now() - timedelta(days=10)
    )

    plant3 = Plant.objects.create(
        user=user,
        name="Paşa Kılıcı",
        species="Sansevieria",
        plant_type="sukulent",
        location="Balkon",
        water_frequency="2_haftada",
        light_need="tam_gunes",
        is_healthy=False,
        last_watered=timezone.now() - timedelta(days=15),
        last_fertilized=timezone.now() - timedelta(days=40)
    )

    # Create tasks
    today = timezone.now().date()
    tomorrow = today + timedelta(days=1)
    
    Task.objects.create(plant=plant1, task_type='water', due_date=today)
    Task.objects.create(plant=plant2, task_type='clean', due_date=today)
    Task.objects.create(plant=plant3, task_type='water', due_date=tomorrow)
    Task.objects.create(plant=plant1, task_type='fertilize', due_date=today + timedelta(days=3))
    
    # Create notes
    Note.objects.create(plant=plant1, content="Yeni yapraklar veriyor, büyümesi harika!")
    Note.objects.create(plant=plant3, content="Toprağı çok kurumuş, saksısını değiştirmem gerekebilir.")

    print("Veriler başarıyla eklendi!")

if __name__ == "__main__":
    populate_dummy_data()
