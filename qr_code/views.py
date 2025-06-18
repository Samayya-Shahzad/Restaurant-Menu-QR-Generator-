from django.shortcuts import render
from .forms import QRcodeform
import qrcode
import os 
from django.conf import settings

def generate_qr_code(request):

    if request.method == 'POST':
        form = QRcodeform(request.POST)
        if form.is_valid():
            rest_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']
            
            qr = qrcode.make(url)
            filename = rest_name.replace(" ","_").lower()+'_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT, filename)
            qr.save(file_path)

            # create image url
            qr_url = os.path.join(settings.MEDIA_URL, filename)

            context = {
                'rest_name': rest_name,
                'qr_url': qr_url,
                'filename': filename
            }

            return render(request,'qr_download.html',context)

    else:    
        form = QRcodeform()
    context = {
        'form' : form,
    }
    return render(request, 'generate_qr_code.html',context)


    