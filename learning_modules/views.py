from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Module, Lesson, UserProgress


def module_list(request):
    modules = Module.objects.prefetch_related('lessons').all()
    return render(request, 'learning_modules/module_list.html', {'modules': modules})


def lesson_detail(request, module_slug, lesson_slug):
    lesson = get_object_or_404(Lesson, module__slug=module_slug, slug=lesson_slug)
    
    user_progress = None
    if request.user.is_authenticated:
        user_progress = UserProgress.objects.filter(user=request.user, lesson=lesson).first()
    
    # Get previous and next lessons
    all_lessons = lesson.module.lessons.all().order_by('order')
    prev_lesson = all_lessons.filter(order__lt=lesson.order).last()
    next_lesson = all_lessons.filter(order__gt=lesson.order).first()
    
    context = {
        'lesson': lesson,
        'module': lesson.module,
        'user_progress': user_progress,
        'prev_lesson': prev_lesson,
        'next_lesson': next_lesson,
    }
    return render(request, 'learning_modules/lesson_detail.html', context)


@login_required
def mark_complete(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    progress, created = UserProgress.objects.get_or_create(
        user=request.user,
        lesson=lesson
    )
    progress.completed = True
    progress.completed_at = timezone.now()
    progress.save()
    
    return redirect('lesson_detail', module_slug=lesson.module.slug, lesson_slug=lesson.slug)
