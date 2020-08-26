from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .m_download_convert import download
def index(request):
     if request.method == 'POST':
          youtube_link=request.POST['name']
          print(f"response posted {youtube_link}")

          download.download(youtube_link)

     #return HttpResponse("Test now")
     return render(request,'pages/index.html')


