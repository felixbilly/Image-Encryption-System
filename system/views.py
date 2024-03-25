#from django.shortcuts import render
# encryption modules
import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image
import io
from .image1 import  decrypt_image, encrypt_image




#import requests
import sys
from subprocess import run,PIPE
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
#from .test import output, time
from django.http import HttpResponse
from .models import Result
#from image1 import image_name ,image_fullpath
# Create your views here.



def home(request):
    return render(request,'index\index.html')

@ login_required(login_url='signin')
def page(request):
    current_user=request.user
    user_id=current_user.id
    print(user_id)
    context={'user_id': user_id}
    
    return render(request,'home.html', context)


def signup(request):
    if request.method == "POST":
     username = request.POST['username']
     email = request.POST['email']
     pass1 = request.POST['pass1']
     pass2 = request.POST['pass2']
     if pass1 != pass2:
        return HttpResponse("password mismatch!!!")
     else:

        myuser = User.objects.create_user (username ,email, pass1)
         #myuser.firts_name=
        myuser.save()


        messages.success(request,"Your registration is succesfully Completed")

        return redirect('signin')
    
    return render(request,'reg_page.html')
    

def signin(request):
    if request.method == "POST":
     username = request.POST['username']
     pass1 = request.POST['pass1']
     

     User = authenticate(request,username=username, password=pass1) 
     #my_user(save)
     if User is not None:
        login(request, User)
        return redirect('page')#return render(request,"index.html")
     else:
        messages.error(request, 'Bad Credentials')

        return redirect('signin')


    return render(request,'login_page.html')
    

def signout(request):
    logout(request)
    messages.success(request, "logged out successfuly!")

    return redirect('home')


def button(request):

    return render(request,'home.html')

def output(request):
    #data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'home.html',{'data':data})

def external(request):
    inp= request.POST.get('param')
    image=request.FILES ['image']
    print("image is ",image)
    fs=FileSystemStorage()
    filename=fs.save(image.name,image)
    fileurl=fs.open(filename)
    templateurl=fs.url(filename)
    print("file raw url",filename)
    print("file full url", fileurl)
    print("template url",templateurl)
    #out= run([sys.executable,'//Users//felix//OneDrive//Desktop//image//billy//test.py',inp],shell=False,stdout=PIPE, )
    image= run([sys.executable,'//Users//felix//OneDrive//Desktop//image//billy//image.py',str(fileurl),str(filename)],shell=False,stdout=PIPE, )
    #print(out)
    print(image.stdout)
    return render(request,'home.html',{'raw_url':templateurl,'edit_url':image.stdout})




# def insert(request):
#     if  request.method== 'POST':
#         key=request.POST.get('param')
#         image =request.FILES['image']
#         encrypted_image = encrypt_image(image)

#         process=Result(key= key, image=image, encrypted_image=encrypted_image)

#         process.save()
        

#         return redirect('result')

#     return render(request, 'home.html')

def insert(request):
    if request.method == 'POST':
        key = request.POST.get('param')
        image = request.FILES['image']

        # Encrypt the image
        encrypted_image = encrypt_image(image)

        # Save the encrypted image file
        encrypted_image_file_path = os.path.join(settings.MEDIA_ROOT, 'encrypted_images', image.name)
        encrypted_image.save(encrypted_image_file_path)

        # Save the Result object with the encrypted image field
        process = Result(key=key, image=image, encrypted_image=encrypted_image_file_path)
        process.save()

        return redirect('result')

    return render(request, 'home.html')


def Retrieve(request):
    images = Result.objects.get()

    return render(request, 'result.html',{"images":images })


# Image Encryption Processing

def encrypt_image(image):
    image = Image.open(image)
    gray_img = image.convert('L')  # Convert image to grayscale
    width, height = gray_img.size
    dotted_img = Image.new('L', (width, height))

    # Create a dotted grayscale image
    for x in range(0, width, 2):
        for y in range(0, height, 2):
            pixel_value = gray_img.getpixel((x, y))
            dotted_img.putpixel((x, y), pixel_value)

    return dotted_img

def decrypt_image(image):
    width, height = image.size
    original_img = Image.new('RGB', (width, height))

    # Convert dotted grayscale image back to original
    for x in range(0, width, 2):
        for y in range(0, height, 2):
            pixel_value = image.getpixel((x, y))
            original_img.putpixel((x, y), (pixel_value, pixel_value, pixel_value))

    return original_img

def encrypt_decrypt_view(request, pk ):

    # image = Result.objects.get(pk)

    
    # # uploaded_image = request.FILES['image']
    # img = Image.open(image)
    # encrypted_image = encrypt_image(img)
    # # decrypted_image = decrypt_image(encrypted_image)

    # save to database


        # Directory to save images
    # images_directory = os.path.join(settings.BASE_DIR, 'static', 'images')
    # os.makedirs(images_directory, exist_ok=True)  # Create directory if it doesn't exist

    # # Save the encrypted and decrypted images in the static directory
    # encrypted_image_path = os.path.join('images', 'encrypted_image.png')
    # decrypted_image_path = os.path.join('images', 'decrypted_image.png')

    # encrypted_image.save(os.path.join(settings.BASE_DIR, 'static', encrypted_image_path))
    # decrypted_image.save(os.path.join(settings.BASE_DIR, 'static', decrypted_image_path))

    # Save the encrypted and decrypted images
    #encrypted_image_path = 'encrypted_image.png'
    #decrypted_image_path = 'decrypted_image.png'

    #encrypted_image.save(encrypted_image_path)
    ##decrypted_image.save(decrypted_image_path)

    return render(request, 'result.html', {'encrypted_image': encrypted_image_path, 'decrypted_image': decrypted_image_path})
# return render (request, 'home.html')#(request, 'encrypt_decrypt.html')

def decrypt_image_view(request):
    # Path to the encrypted image
    encrypted_image_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'encrypted_image.png')

    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)

    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image)

    # Create an in-memory byte stream for the decrypted image
    decrypted_image_byte_array = io.BytesIO()
    decrypted_image.save(decrypted_image_byte_array, format='PNG')
    decrypted_image_byte_array.seek(0)

    # Return the decrypted image as a HTTP response
    return HttpResponse(decrypted_image_byte_array, content_type='image/png')

def result(request):
    images = Result.objects.all()

    return render(request, 'result.html',{"images":images } )

def result2(request):
    return render(request, 'upload2.html' )