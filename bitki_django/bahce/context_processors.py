from django.utils import timezone
from .models import Task

def notifications(request):
    if request.user.is_authenticated:
        # Get tasks that are due today or overdue and not completed
        today = timezone.now().date()
        due_tasks = Task.objects.filter(
            plant__user=request.user, 
            completed=False, 
            due_date__lte=today
        ).order_by('-due_date')[:5]
        
        return {
            'notifications': due_tasks,
            'notif_count': due_tasks.count()
        }
    return {'notifications': [], 'notif_count': 0}
