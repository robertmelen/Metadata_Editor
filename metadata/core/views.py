from django.shortcuts import render, redirect

#project scoped imports
from .forms import UploadImageForm, Uploaded_Image

#object retrival imports
from django.shortcuts import get_object_or_404

#response imports
from django.http import HttpResponse, HttpResponseRedirect

#testingimports
from django.views.decorators.csrf import csrf_exempt


#non Django imports
import exiftool
#any @csrf_exempt views must be fixed to except csrf propely


def all_data(image_path):
    with exiftool.ExifToolHelper() as et:
        return(et.execute_json(image_path,  "-j"))






#Main page with upload form

def upload(request):
    if request.htmx:
        form = UploadImageForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            image = form.save()
            return redirect(result, image=image.id)
            
    else: 
        form = UploadImageForm(request.POST, request.FILES)
        print(form)
        form = UploadImageForm()
        return render(request, "upload.html", {'form': form} )



#this is handlind returning a HTMX partial with the image
#it also pushes a new URL rou

def result(request, image=None):
    if image is not None:
        image_obj = get_object_or_404(Uploaded_Image, pk=image)
        form = UploadImageForm()
        return render(request, "result.html", {'image': image_obj, 'form': form})
   
    
    
      
def get_data(request, image=None):
    if request.htmx:
        image_obj = get_object_or_404(Uploaded_Image, pk=image)
        get_data = all_data(image_obj.image.path)
        test = get_data[0]
        print(test)
        return render(request, "partials/data.html", {'test': test})
   