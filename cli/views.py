from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def terminal(request):
    return render(request, 'cli/terminal.html')
