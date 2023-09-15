
from .models import Video
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from pytube import YouTube
from django.http import FileResponse
import os

def index(request):
    videos = Video.objects.all()
    return render(request, 'videos/index.html', {'videos': videos})


def dnldr(request):
    return render(request, 'dnldr.html')

def yt(request):
    return render(request, 'yt.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dnldr')  
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def download(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_link')
        download_path = request.POST.get('download_path')  

        try:
            yt = YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            output_path = os.path.join('media', 'downloads', download_path)  
            os.makedirs(output_path, exist_ok=True)
            stream.download(output_path=output_path)
            file_path = os.path.join(output_path, yt.title + '.mp4')
            video_embed_url = f"https://www.youtube.com/embed/{yt.video_id}"

            return render(request, 'yt.html', {'video_url': file_path, 'video_embed_url': video_embed_url})

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'yt.html', {'error_message': error_message})

    return render(request, 'yt.html')