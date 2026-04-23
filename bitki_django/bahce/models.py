from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Plant(models.Model):
    """Bitki modeli"""
    WATER_CHOICES = [
        ('her_gun', 'Her Gün'),
        ('2_gunde', '2 Günde Bir'),
        ('3_gunde', '3 Günde Bir'),
        ('haftada', 'Haftada Bir'),
        ('2_haftada', '2 Haftada Bir'),
        ('ayda', 'Ayda Bir'),
    ]
    LIGHT_CHOICES = [
        ('tam_gunes', 'Tam Güneş'),
        ('dolayli', 'Dolaylı Güneş'),
        ('yari_golge', 'Yarı Gölge'),
        ('tam_golge', 'Tam Gölge'),
    ]
    TYPE_CHOICES = [
        ('salon', 'Salon Bitkisi'),
        ('sukulent', 'Sukulent'),
        ('kaktus', 'Kaktüs'),
        ('tropikal', 'Tropikal'),
        ('erelti', 'Eğrelti Otu'),
        ('orkide', 'Orkide'),
        ('diger', 'Diğer'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plants')
    name = models.CharField('Bitki Adı', max_length=100)
    species = models.CharField('Bilimsel Ad', max_length=100, blank=True)
    plant_type = models.CharField('Tür', max_length=20, choices=TYPE_CHOICES, default='salon')
    location = models.CharField('Konum', max_length=100, blank=True, default='Salon')
    water_frequency = models.CharField('Sulama Sıklığı', max_length=20, choices=WATER_CHOICES, default='3_gunde')
    light_need = models.CharField('Işık İhtiyacı', max_length=20, choices=LIGHT_CHOICES, default='dolayli')
    image = models.ImageField('Fotoğraf', upload_to='plants/', blank=True, null=True)
    is_healthy = models.BooleanField('Sağlıklı mı?', default=True)
    last_watered = models.DateTimeField('Son Sulama', null=True, blank=True)
    last_fertilized = models.DateTimeField('Son Gübreleme', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Bitki'
        verbose_name_plural = 'Bitkiler'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def water_now(self):
        self.last_watered = timezone.now()
        self.save()


class Note(models.Model):
    """Bitki notu modeli"""
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField('Not')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Not'
        verbose_name_plural = 'Notlar'
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.plant.name} - {self.created_at.strftime('%d.%m.%Y')}"


class Task(models.Model):
    """Bakım görevi modeli"""
    TASK_TYPES = [
        ('water', 'Sulama'),
        ('fertilize', 'Gübreleme'),
        ('repot', 'Saksı Değişimi'),
        ('clean', 'Yaprak Temizliği'),
        ('prune', 'Budama'),
    ]

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='tasks')
    task_type = models.CharField('Görev Türü', max_length=20, choices=TASK_TYPES)
    due_date = models.DateField('Görev Tarihi')
    completed = models.BooleanField('Tamamlandı', default=False)
    completed_at = models.DateTimeField('Tamamlanma Zamanı', null=True, blank=True)

    class Meta:
        verbose_name = 'Görev'
        verbose_name_plural = 'Görevler'
        ordering = ['due_date']

    def __str__(self):
        return f"{self.plant.name} - {self.get_task_type_display()}"


class DailyNote(models.Model):
    """Takvimdeki belirli bir güne ait kullanıcı notu"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily_notes')
    date = models.DateField('Tarih')
    content = models.TextField('Not', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Günlük Not'
        verbose_name_plural = 'Günlük Notlar'
        unique_together = ('user', 'date')
        ordering = ['date']

    def __str__(self):
        return f"{self.user.username} - {self.date} Notu"
