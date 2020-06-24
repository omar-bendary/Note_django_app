from django.shortcuts import redirect, render
from .models import Note
from .form import NoteForm
from django.urls import reverse


def index(request):
    notes = Note.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'index.html', context)


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:index')

    else:
        form = NoteForm()

    context = {

        'form': form

    }
    return render(request, 'add_note.html', context)
