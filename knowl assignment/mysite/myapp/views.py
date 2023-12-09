
from django.shortcuts import render, redirect
from .models import UploadedFile

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        filename = file.name
        uploaded_file = UploadedFile.objects.create(user=request.user, file=file, filename=filename)
        return redirect('file_list')
    return render(request, 'upload_file.html')

def file_list(request):
    uploaded_files = UploadedFile.objects.filter(user=request.user)
    context = {'uploaded_files': uploaded_files}
    return render(request, 'file_list.html', context)
