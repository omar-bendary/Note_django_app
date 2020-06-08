from django.shortcuts import render
from .models import Note

def index(request):
    notes = Note.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'index.html', context)



