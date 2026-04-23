from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
import datetime

from .models import Plant, Note, Task
from .forms import PlantForm, NoteForm, CustomRegisterForm, CustomLoginForm


# ─── Landing Page ───────────────────────────────────────────────
def landing(request):
    if request.user.is_authenticated:
        return redirect('panel')
    return redirect('giris')


# ─── Auth Views ──────────────────────────────────────────────────
def giris(request):
    if request.user.is_authenticated:
        return redirect('panel')
    form = CustomLoginForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('panel')
    return render(request, 'auth/giris.html', {'form': form})


def kayit(request):
    if request.user.is_authenticated:
        return redirect('panel')
    form = CustomRegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Hoş geldiniz! Bahçenize ilk bitkiyi ekleyebilirsiniz.')
        return redirect('panel')
    return render(request, 'auth/kayit.html', {'form': form})


def cikis(request):
    logout(request)
    return redirect('landing')


# ─── Dashboard (Panel) ───────────────────────────────────────────
@login_required
def panel(request):
    plants = Plant.objects.filter(user=request.user)
    today = timezone.now().date()
    tasks_today = Task.objects.filter(plant__user=request.user, due_date=today, completed=False)
    featured_plant = plants.first()
    featured_note = featured_plant.notes.first() if featured_plant else None

    # Yeni bitki ekle (modal form)
    if request.method == 'POST':
        plant_form = PlantForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant = plant_form.save(commit=False)
            plant.user = request.user
            plant.save()
            messages.success(request, f'"{plant.name}" bahçenize eklendi!')
            return redirect('panel')
    else:
        plant_form = PlantForm()

    context = {
        'plants': plants,
        'plant_count': plants.count(),
        'tasks_today': tasks_today,
        'tasks_today_count': tasks_today.count(),
        'featured_plant': featured_plant,
        'featured_note': featured_note,
        'plant_form': plant_form,
    }
    return render(request, 'dashboard/panel.html', context)


# ─── Sulama ──────────────────────────────────────────────────────
@login_required
@require_POST
def sula(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id, user=request.user)
    plant.last_watered = timezone.now()
    plant.save()
    return JsonResponse({
        'success': True,
        'watered_at': plant.last_watered.strftime('%H:%M')
    })


# ─── Not güncelle ────────────────────────────────────────────────
@login_required
@require_POST
def not_guncelle(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id, user=request.user)
    data = json.loads(request.body)
    content = data.get('content', '').strip()
    note, created = Note.objects.get_or_create(plant=plant, defaults={'content': content})
    if not created:
        note.content = content
        note.save()
    return JsonResponse({'success': True, 'content': note.content})


# ─── Kütüphane ───────────────────────────────────────────────────
@login_required
def kutuphane(request):
    LIBRARY_PLANTS = [
        {'name': 'Barış Çiçeği', 'species': 'Spathiphyllum wallisii', 'type': 'Salon Bitkisi', 'water': 'Orta', 'light': 'Dolaylı Güneş', 'difficulty': 'Kolay', 'icon': 'eco', 'toxic': False, 'air_purifier': True, 'image_url': 'https://images.unsplash.com/photo-1593691509543-c55fb32e7355?auto=format&fit=crop&w=400&q=80'},
        {'name': 'Deve Tabanı', 'species': 'Monstera deliciosa', 'type': 'Tropikal', 'water': 'Orta', 'light': 'Dolaylı Güneş', 'difficulty': 'Orta', 'icon': 'energy_savings_leaf', 'toxic': True, 'air_purifier': True, 'image_url': 'https://images.unsplash.com/photo-1614594975525-e45190c55d0b?auto=format&fit=crop&w=400&q=80'},
        {'name': 'Paşa Kılıcı', 'species': 'Sansevieria trifasciata', 'type': 'Sukulent', 'water': 'Az', 'light': 'Yarı Gölge', 'difficulty': 'Çok Kolay', 'icon': 'grass', 'toxic': True, 'air_purifier': True, 'image_url': 'https://images.unsplash.com/photo-1595066929944-935df68b0e77?auto=format&fit=crop&w=400&q=80'},
        {'name': 'Aloe Vera', 'species': 'Aloe barbadensis', 'type': 'Sukulent', 'water': 'Az', 'light': 'Tam Güneş', 'difficulty': 'Kolay', 'icon': 'local_florist', 'toxic': False, 'air_purifier': False, 'image_url': 'https://images.unsplash.com/photo-1596547610738-9cb5ee5db9ee?auto=format&fit=crop&w=400&q=80'},
        {'name': 'Aşk Merdiveni', 'species': 'Epipremnum aureum', 'type': 'Eğrelti Otu', 'water': 'Orta', 'light': 'Yarı Gölge', 'difficulty': 'Çok Kolay', 'icon': 'psychiatry', 'toxic': True, 'air_purifier': True, 'image_url': 'https://images.unsplash.com/photo-1604928019313-2d57e3f8ec47?auto=format&fit=crop&w=400&q=80'},
        {'name': 'Kurdele Çiçeği', 'species': 'Chlorophytum comosum', 'type': 'Salon Bitkisi', 'water': 'Orta', 'light': 'Dolaylı Güneş', 'difficulty': 'Kolay', 'icon': 'potted_plant', 'toxic': False, 'air_purifier': True, 'image_url': 'https://images.unsplash.com/photo-1512428813834-c702c7702b78?auto=format&fit=crop&w=400&q=80'},
        {'name': 'Orkide', 'species': 'Phalaenopsis', 'type': 'Çiçekli Bitki', 'water': 'Az', 'light': 'Dolaylı Güneş', 'difficulty': 'Zor', 'icon': 'local_florist', 'toxic': False, 'air_purifier': False, 'image_url': 'https://images.unsplash.com/photo-1566440263-6c8ea23fcc32?auto=format&fit=crop&w=400&q=80'},
        {'name': 'Canlı Taş', 'species': 'Lithops sp.', 'type': 'Sukulent', 'water': 'Çok Az', 'light': 'Tam Güneş', 'difficulty': 'Orta', 'icon': 'landscape', 'toxic': False, 'air_purifier': False, 'image_url': 'https://images.unsplash.com/photo-1620023402773-cb9378c52d8b?auto=format&fit=crop&w=400&q=80'},
    ]
    query = request.GET.get('q', '').lower()
    if query:
        LIBRARY_PLANTS = [p for p in LIBRARY_PLANTS if query in p['name'].lower() or query in p['species'].lower()]
    return render(request, 'dashboard/kutuphane.html', {'library_plants': LIBRARY_PLANTS, 'query': query})


# ─── Bakım Takvimi ───────────────────────────────────────────────
@login_required
def takvim(request):
    from .models import DailyNote
    today = timezone.now().date()
    tomorrow = today + datetime.timedelta(days=1)
    week_end = today + datetime.timedelta(days=7)

    tasks_today = Task.objects.filter(plant__user=request.user, due_date=today)
    tasks_tomorrow = Task.objects.filter(plant__user=request.user, due_date=tomorrow)
    tasks_week = Task.objects.filter(plant__user=request.user, due_date__gt=tomorrow, due_date__lte=week_end)

    # İşlem yakalama
    if request.method == 'POST':
        if 'task_id' in request.POST:
            task_id = request.POST.get('task_id')
            task = get_object_or_404(Task, id=task_id, plant__user=request.user)
            task.completed = not task.completed
            task.completed_at = timezone.now() if task.completed else None
            task.save()
        elif 'note_date' in request.POST:
            note_date_str = request.POST.get('note_date')
            content = request.POST.get('content', '').strip()
            note_date = datetime.datetime.strptime(note_date_str, '%Y-%m-%d').date()
            note, created = DailyNote.objects.get_or_create(user=request.user, date=note_date)
            note.content = content
            note.save()
        return redirect('takvim')

    # Notları getir
    start_date = today - datetime.timedelta(days=today.weekday())
    end_date = start_date + datetime.timedelta(days=6)
    daily_notes = DailyNote.objects.filter(user=request.user, date__range=[start_date, end_date])
    notes_dict = {note.date: note.content for note in daily_notes}

    # Hafta günleri
    week_days = []
    for i in range(7):
        d = start_date + datetime.timedelta(days=i)
        week_days.append({
            'date': d, 
            'is_today': d == today,
            'note': notes_dict.get(d, '')
        })

    task_groups = {
        'Bugün': tasks_today,
        'Yarın': tasks_tomorrow,
        'Bu Hafta': tasks_week
    }

    context = {
        'task_groups': task_groups,
        'week_days': week_days,
        'today': today,
        'has_tasks': tasks_today.exists() or tasks_tomorrow.exists() or tasks_week.exists()
    }
    return render(request, 'dashboard/takvim.html', context)


# ─── İstatistikler ───────────────────────────────────────────────
@login_required
def istatistik(request):
    plants = Plant.objects.filter(user=request.user)
    total_plants = plants.count()
    healthy_plants = plants.filter(is_healthy=True).count()
    completed_tasks = Task.objects.filter(plant__user=request.user, completed=True).count()
    health_score = int((healthy_plants / total_plants * 100)) if total_plants > 0 else 0

    context = {
        'total_plants': total_plants,
        'healthy_plants': healthy_plants,
        'rescued_plants': plants.filter(is_healthy=False).count(),
        'completed_tasks': completed_tasks,
        'health_score': health_score,
        'health_circumference': 251.2,
        'health_offset': 251.2 * (1 - health_score / 100),
    }
    return render(request, 'dashboard/istatistik.html', context)


# ─── AI Teşhis ───────────────────────────────────────────────────
@login_required
def ai_teshis(request):
    return render(request, 'dashboard/ai_teshis.html')


# ─── Yardım & Gizlilik ───────────────────────────────────────────
@login_required
def yardim(request):
    return render(request, 'info/yardim.html')


@login_required
def gizlilik(request):
    return render(request, 'info/gizlilik.html')


# ─── Profil ve Ayarlar ───────────────────────────────────────────
@login_required
def profil(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        messages.success(request, 'Profil başarıyla güncellendi.')
        return redirect('profil')
        
    return render(request, 'dashboard/profil.html')
