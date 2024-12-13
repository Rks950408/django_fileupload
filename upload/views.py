from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FileUpload

def upload_file(request):
    if request.method == 'POST' and request.FILES:
        uploaded_file = request.FILES.get('file')
        uploaded_image = request.FILES.get('image')
        description = request.POST.get('description')

        FileUpload.objects.create(
            file=uploaded_file,
            image=uploaded_image,
            description=description
        )
        return redirect('view_files')  
    return render(request, 'upload/upload.html')

def view_files(request):
    files = FileUpload.objects.all()  
    return render(request, 'upload/view_files.html', {'files': files})
