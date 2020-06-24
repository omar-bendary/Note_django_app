from django.shortcuts import redirect, render
from .models import Note
from .form import NoteForm


def index(request):
    notes = Note.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'index.html', context)


def add_note(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:index')

    context = {

        'form': form

    }
    return render(request, 'add_note.html', context)


def update_note(request, pk):
    note = Note.objects.get(id=pk)
    form = NoteForm(instance=note)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:index')

    context = {

        'form': form

    }
    return render(request, 'update_note.html', context)


def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('notes:index')

    context = {

        'note': note

    }

    return render(request, 'delete_note.html', context)
