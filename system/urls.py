
from django.urls import path
from . import views 
from django.urls import re_path as url
#from django.conf.urls import url


from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('page/', views.page, name="page"),
    path('insert/', views.insert, name="insert"),

    path('signin/', views.signin, name="signin"),

    path('signout/', views.signout, name="signout"),
    path('encrypted_image/', views.encrypt_decrypt_view, name='encrypt_image'),
    path('result/', views.result, name='result'),
    path('result2/', views.result2, name='result2'),
    path('upload_image/', views.decrypt_image_view, name='decrypt_image'),

    path('decrypt/', views.fetch_encrypted_image, name='decrypt'),


    path('external', views.external,name='external'),


    url(r'^$', views.button),
    url(r'^output', views.output,name="script"),
    #url(r'^external', views.external),
    # url(r'^insert', views.insert),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header="Image Encryption Administration"
admin.site.site_title="Felix Billy"
admin.site.index_title="ImgCrypt.io"






# urls.py
#from django.urls import path
#from . import views

#urlpatterns = [
    #path('encrypt/', views.encrypt_image, name='encrypt_image'),
    #path('decrypt/<int:pk>/', views.decrypt_image, name='decrypt_image'),
#]


"""
from django.urls import path
from .views import encrypt_decrypt_view
from . import views

urlpatterns = [
    #path('', encrypt_decrypt_view, name='encrypt_decrypt'),
    path('encrypted_image/', views.encrypt_decrypt_view, name='encrypt_image'),
    path('result/', views.result, name='result'),
    path('upload_image/', views.decrypt_image_view, name='decrypt_image'),


]
"""






"""
from django.urls import path
from . import views

urlpatterns = [
    path('encrypt/', views.encrypt_image, name='encrypt_image'),
    path('decrypt/<int:image_id>/', views.decrypt_image, name='decrypt_image'),
    #path('detail/<int:image_id>/', views.image_detail, name='image_detail'),
]
"""

"""
urlpatterns = [
    path('', views.encrypt_image, name='encrypt_image'),
   path('decrypt/', views.decrypt_image, name='decrypt_image'),
]
"""
"""
urlpatterns = [
    path('', views.upload_image, name='upload_image'),  # URL for uploading image
    path('grayscale/', views.grayscale_image, name='grayscale_image'),  # URL for displaying grayscale image
]
"""