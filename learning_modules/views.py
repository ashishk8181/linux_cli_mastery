from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Module, Lesson, UserProgress


def module_list(request):
    modules = Module.objects.prefetch_related('lessons').all()
    return render(request, 'lessons/module_list.html', {'modules': modules})


def lesson_detail(request, module_slug, lesson_slug):
    lesson = get_object_or_404(Lesson, module__slug=module_slug, slug=lesson_slug)
    
    user_progress = None
    user_progress_dict = {}
    if request.user.is_authenticated:
        user_progress = UserProgress.objects.filter(user=request.user, lesson=lesson).first()
        # Get all user progress for sidebar
        all_progress = UserProgress.objects.filter(user=request.user, completed=True).values_list('lesson_id', flat=True)
        user_progress_dict = {lesson_id: True for lesson_id in all_progress}
    
    # Get all modules with lessons
    all_modules = Module.objects.prefetch_related('lessons').all()
    
    # Get previous and next lessons
    all_lessons = lesson.module.lessons.all().order_by('order')
    prev_lesson = all_lessons.filter(order__lt=lesson.order).last()
    next_lesson = all_lessons.filter(order__gt=lesson.order).first()
    
    context = {
        'lesson': lesson,
        'module': lesson.module,
        'all_modules': all_modules,
        'user_progress': user_progress,
        'user_progress_dict': user_progress_dict,
        'prev_lesson': prev_lesson,
        'next_lesson': next_lesson,
    }
    return render(request, 'lessons/lesson_detail.html', context)


@login_required
def mark_complete(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    progress, created = UserProgress.objects.get_or_create(
        user=request.user,
        lesson=lesson
    )
    
    # Toggle completion status
    if progress.completed:
        progress.completed = False
        progress.completed_at = None
    else:
        progress.completed = True
        progress.completed_at = timezone.now()
    
    progress.save()
    
    return redirect('lesson_detail', module_slug=lesson.module.slug, lesson_slug=lesson.slug)
