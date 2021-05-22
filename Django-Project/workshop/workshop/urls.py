"""workshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path



from django.conf.urls.static import static
from django.conf import settings
from django.utils.translation.trans_real import DjangoTranslation
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.index,name="home"),
    path('category/<slug:category_slug>',views.index,name="product_by_category"),
    path('typefile/<slug:typefile_slug>',views.indextype,name="product_by_typefile"),
    path('published/<slug:published_slug>',views.indexpub,name="product_by_published"),

    #path('product/<slug:category_slug>/<slug:product_slug>',views.productPage,name='productDetail'),
    
    path('payment',views.paymentView, name="paymentOrder"),


    path('upload/',views.upload_view, name="uploadview"),
    path('upload/workspace/',views.upload_workspaceView,name='workspace'),


    path('upload/workspace/update/<str:pk>/',views.upload_updateView,name='workspaceUpdate'),


    path('upload/workspace/delete/<str:pk>/',views.upload_deleteView,name='workspaceDelete'),


    path('upload/<slug:category_slug>/<slug:uploadfile_slug>',views.uploadProductPage,name="uploadProductDetail"),

    path('account/create',views.SignUpView, name="signUp"),
    path('account/login',views.SignInView, name="signIn"),
    path('account/reset',views.resetPass, name="resetPass"),
    path('account/logout',views.signOutView,name="signOut"),
    path('account/profile/',views.profile_detailView,name="profileDetail"),
    path('account/profile/profile_form/',views.profile_formView,name="profileForm"),
    path('search',views.search, name="searchItem"),
   
 
    
]

if settings.DEBUG :

    #/mediaproduct
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
    #/static/
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

