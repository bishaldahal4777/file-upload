# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadForm
from .models import Upload
from django.contrib import messages

@login_required
def upload_create(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.save()
            messages.success(request, "Uploaded successfully.")
            return redirect("upload_list")
        else:
            messages.error(request, "There was an error. Fix and try again.")
    else:
        form = UploadForm()
    return render(request, "myapp/upload_form.html", {"form": form})

@login_required
def upload_list(request):
    uploads = Upload.objects.filter(user=request.user).order_by("-uploaded_at")
    return render(request, "myapp/upload_list.html", {"uploads": uploads})
