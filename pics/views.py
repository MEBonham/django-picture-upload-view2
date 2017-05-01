from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .models import Picture

# Create your views here.
def index(request):
    picture_bank = Picture.objects.order_by('id')
    context = {
        'picture_bank': picture_bank,
        'this_pic': picture_bank[0].image,
        'idx': 0,
        'file_name': picture_bank[0].file_name,
        'galleryLength': len(picture_bank),
    }
    return render(request, 'pics/base.html', context)
    
def picture(request, page_idx):
    picture_id = int(page_idx)
    picture_bank = Picture.objects.order_by('id')
    context = {
        'picture_bank': picture_bank,
        'this_pic': picture_bank[picture_id].image,
        'idx': picture_id,
        'file_name': picture_bank[picture_id].file_name,
        'galleryLength': len(picture_bank),
    }
    return render(request, 'pics/base.html', context)
    
def upload(request):
    if request.method == 'POST':
        #filePost = request.POST['fileToUpload']
        file = request.FILES['fileToUpload']
        p = Picture(image=file, file_name=file.name) #file_name=str(filePost))
        p.save()
        pic_bank = Picture.objects.order_by('id')
        pic_idx = len(pic_bank) - 1
        return HttpResponseRedirect('/pics/' + str(pic_idx))
    else:
        return HttpResponseRedirect('/pics')