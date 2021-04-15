from django.shortcuts import render, redirect
from .models import Buku
from .forms import BookCreate
from django.http import HttpResponse

def index(request):
    shelf = Buku.objects.all()
    return render(request, 'buku/library.html', {'shelf': shelf})

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""form salah, reload di <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'buku/upload_form.html', {'upload_form':upload})

def update_buku(request, buku_id):
    buku_id = int(buku_id)
    try:
        buku_sel = Buku.objects.get(id = buku_id)
    except Buku.DoesNotExist:
        return redirect('index')
    buku_form = BookCreate(request.POST or None, instance = buku_sel)
    if buku_form.is_valid():
       buku_form.save()
       return redirect('index')
    return render(request, 'buku/upload_form.html', {'upload_form':buku_form})

def delete_buku(request, buku_id):
    buku_id = int(buku_id)
    try:
        buku_sel = Buku.objects.get(id = buku_id)
    except Buku.DoesNotExist:
        return redirect('index')
    buku_sel.delete()
    return redirect('index')
