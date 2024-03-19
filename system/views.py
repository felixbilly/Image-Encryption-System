#from django.shortcuts import render

"""
from django.shortcuts import render
from PIL import Image

def upload_image(request):
    return render(request, 'upload_image.html')
def grayscale_image(request):
    if request.method == 'POST' and request.FILES['image']:
        # Get the uploaded image
        uploaded_image = request.FILES['image']

        # Open the image using Pillow
        original_image = Image.open(uploaded_image)

        # Convert the image to grayscale
        grayscale_image = original_image.convert('L')

        # Pass the original and grayscale images to the template
        return render(request, 'grayscale_image.html', {'original_image': original_image, 'grayscale_image': grayscale_image})

    return render(request, 'upload_image.html')"""""
"""""
from django.shortcuts import render
from django.http import HttpResponse
from .utilis import encrypt_image, decrypt_image
import os

def encrypt(request):
    # Replace with your secret key
    key = b'12345'

    # Provide the path to your image
    image_path = 'C:/Users/felix/Downloads/nyumba.jpeg'

    # Encrypt the image
    encrypted_data = encrypt_image(image_path, key)

    # Save or return encrypted_data as per your requirement
    return HttpResponse(encrypted_data)

def decrypt(request):
    # Replace with your secret key
    key = b'12345'

    # Assume the encrypted data is received via request.POST or request.GET
    encrypted_data = request.POST.get('encrypted_data', '')

    # Decrypt the image
    decrypted_data = decrypt_image(encrypted_data, key)

    # Save or return decrypted_data as per your requirement
    return HttpResponse(decrypted_data)
"""""
"""""
def encrypt(request):
    key = b'mysecretpassword'  # Replace with your secret key
    image_path = '/path/to/your/image.jpg'  # Provide the path to your image

    encrypted_data = encrypt_image(image_path, key)

    # Save or return encrypted_data as per your requirement
    return HttpResponse(encrypted_data)

def decrypt(request):
    key = b'mysecretpassword'  # Replace with your secret key

    # Assume the encrypted data is received via request.POST or request.GET
    encrypted_data = request.POST.get('encrypted_data', '')

    decrypted_data = decrypt_image(encrypted_data, key)

    # Save or return decrypted_data as per your requirement
    return HttpResponse(decrypted_data)

"""""

""""
from PIL import Image 
from django.shortcuts import render, redirect
from .models import EncryptedImage, DecryptedImage
from .utilis import  decrypt_image
from .utilis import encrypt_image as perform_image_encryption

def encrypt_image(request):
    if request.method == 'POST' and request.FILES['image'] and 'key' in request.POST:
        key = request.POST['key'].encode('utf-8')
        file = request.FILES['image']
        
        # Encrypt the image data
        encrypted_data = perform_image_encryption(file.read(), key) #encrypted_data = encrypt_image(file.read(), key)

        # Save the encrypted data to the database
        encrypted_image = EncryptedImage.objects.create(image=file, encrypted_image=encrypted_data)
        
        return redirect('image_detail', image_id=encrypted_image.id)
    return render(request, 'encrypt_image.html')

def decrypt_image(request, image_id):
    if request.method == 'POST' and 'key' in request.POST:
        key = request.POST['key'].encode('utf-8')
        encrypted_image = EncryptedImage.objects.get(id=image_id)
        
        # Decrypt the image data
        decrypted_data = decrypt_image(encrypted_image.encrypted_image, key)

        # Save the decrypted data to the database
        decrypted_image = DecryptedImage.objects.create(encrypted_image=encrypted_image, decrypted_image=decrypted_data)
        
        return redirect('image_detail', image_id=encrypted_image.id)
    return render(request, 'decrypt_image.html', {'image_id': image_id})

def image_detail(request, image_id):
    encrypted_image = EncryptedImage.objects.get(id=image_id)
    decrypted_image = DecryptedImage.objects.filter(encrypted_image=encrypted_image).first()
    return render(request, 'image_detail.html', {'encrypted_image': encrypted_image, 'decrypted_image': decrypted_image})

"""

"""
import PIL
from PIL import Image 

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from io import BytesIO
from django.http import HttpResponse



def encrypt_image(request):
    if request.method == 'POST' and request.FILES['image']:
        key = b'sixteen byte key'  # 16-byte encryption key
        file = request.FILES['image']
        
        # Read the image file
        image_data = file.read()

        # Encrypt the image data
        cipher = AES.new(key, AES.MODE_CBC)
        encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))

        # Encode the encrypted data
        encoded_encrypted_data = b64encode(encrypted_data)

        # Save the encoded encrypted data to a file
        fs = FileSystemStorage()
        encrypted_filename = fs.save('encrypted_' + file.name, encoded_encrypted_data)

        return render(request, 'encrypted_image.html', {'encrypted_filename': encrypted_filename})
    return render(request, 'encrypt_decrypt.html')

def decrypt_image(request):
    if request.method == 'POST' and request.FILES['encrypted_image']:
        key = b'sixteen byte key'  # 16-byte encryption key
        file = request.FILES['encrypted_image']

        # Read the encrypted image file
        encrypted_data = file.read()

        # Decode the encrypted data
        decoded_encrypted_data = b64decode(encrypted_data)

        # Decrypt the image data
        cipher = AES.new(key, AES.MODE_CBC)
        decrypted_data = unpad(cipher.decrypt(decoded_encrypted_data), AES.block_size)

        # Save the decrypted data to a file
        fs = FileSystemStorage()
        decrypted_filename = fs.save('decrypted_' + file.name, decrypted_data)

        return render(request, 'decrypted_image.html', {'decrypted_filename': decrypted_filename})
    return render(request, 'encrypt_decrypt.html')


"""






"""""
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
#from image1 import image_name ,image_fullpath
# Create your views here.

def home(request):
    return render(request,'index\index.html')
@ login_required(login_url='signin')
def page(request):
    return render(request,'home.html')


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
"""""



"""
# views.py
from django.shortcuts import render, redirect
from .models import EncryptedImage
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
import io
from io import BytesIO


def encrypt_image(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        key = get_random_bytes(16)  # Generate a random key
        cipher = AES.new(key, AES.MODE_CBC)
        encrypted_image_data = cipher.encrypt(pad(image_file.read(), AES.block_size))
        encrypted_image = EncryptedImage(image=encrypted_image_data, key=b64encode(key).decode('utf-8'))
        encrypted_image.save()

         # Convert encrypted image data to a BytesIO object
        encrypted_image_io = BytesIO()
        encrypted_image_io.write(encrypted_image_data)
        encrypted_image_io.seek(0)

        # Create EncryptedImage object and save the encrypted image
        encrypted_image = EncryptedImage(image=encrypted_image_io)
        encrypted_image.key = key  # Store the encryption key
        encrypted_image.save()

         # Convert encrypted image data to bytes-like object and save in model
        #encrypted_image = EncryptedImage()
        #encrypted_image.image.save(image_file.name, io.BytesIO(encrypted_image_data))
        #encrypted_image.key = key
        #encrypted_image.save()

        return redirect('encrypted_image', pk=encrypted_image.pk)
    return render(request, 'encrypt_image.html')

def decrypt_image(request, pk):
    encrypted_image = EncryptedImage.objects.get(pk=pk)
    key = b64decode(encrypted_image.key)
    cipher = AES.new(key, AES.MODE_CBC)
    decrypted_image_data = unpad(cipher.decrypt(encrypted_image.image), AES.block_size)
    return render(request, 'decrypt_image.html', {'image_data': decrypted_image_data})
"""






import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image
import io

def encrypt_image(image):
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

def encrypt_decrypt_view(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            uploaded_image = request.FILES['image']
            img = Image.open(uploaded_image)
            encrypted_image = encrypt_image(img)
            decrypted_image = decrypt_image(encrypted_image)
             # Directory to save images
            images_directory = os.path.join(settings.BASE_DIR, 'static', 'images')
            os.makedirs(images_directory, exist_ok=True)  # Create directory if it doesn't exist

            # Save the encrypted and decrypted images in the static directory
            encrypted_image_path = os.path.join('images', 'encrypted_image.png')
            decrypted_image_path = os.path.join('images', 'decrypted_image.png')

            encrypted_image.save(os.path.join(settings.BASE_DIR, 'static', encrypted_image_path))
            decrypted_image.save(os.path.join(settings.BASE_DIR, 'static', decrypted_image_path))

            # Save the encrypted and decrypted images
            encrypted_image_path = 'encrypted_image.png'
            decrypted_image_path = 'decrypted_image.png'

            encrypted_image.save(encrypted_image_path)
            decrypted_image.save(decrypted_image_path)

            return render(request, 'result.html', {'encrypted_image': encrypted_image_path, 'decrypted_image': decrypted_image_path})
    return render(request, 'encrypt_decrypt.html')

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
    return render(request, 'result.html' )