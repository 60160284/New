from django.http import request
from django.shortcuts import render,get_object_or_404,redirect


from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , authenticate,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,InvalidPage


from django.urls import reverse_lazy


from .models import Profile, UploadFile , Category,Typefile,Published
from .forms import UploadFileForm, ProfileUpdateForm, UserUpdateForm,  SignUpForm




def paymentView(request):
    return render(request, 'payment.html')


def search(request):
    uploads=UploadFile.objects.filter(name__contains=request.GET['title'])
    
    return render(request,'index.html',{'uploads':uploads})

@login_required
def upload_view(request):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
          
        if form.is_valid():
              
            obj = form.save(commit = False)
            obj.user = request.user;
            obj.save()
            return redirect('workspace')
        else:
            print(form.errors)
                
            messages.error(request,'ขออภัย, มีบางอย่าผิดพลาด โปรดกรอกข้อมูลอีกครั้ง')
            return redirect('uploadview')
          
  
    return render(request, 'uploads/upload_form.html', {'form':form})

def upload_workspaceView(request):
    uploads=UploadFile.objects.all().filter(user=request.user)
    return render(request,'uploads/upload_workspace.html',{'uploads':uploads})
    


def upload_updateView(request,pk):
    upload = UploadFile.objects.get(id=pk)
    form = UploadFileForm(instance=upload)

    if request.method =='POST':
        form = UploadFileForm(request.POST,request.FILES , instance=upload)
        if form.is_valid():
            form.save()
            return redirect('workspace')
    context={
        'form':form
    }
    return render(request, 'uploads/upload_update.html', context)




def upload_deleteView(request, pk):   
    upload= UploadFile.objects.get(id=pk)
    
    if request.method =='POST':
        upload.delete()
        messages.success(request,'ลบไฟล์สำเร็จ')
        return redirect('workspace')
        
   
    context={
        'upload': upload
    }

    return render(request, 'uploads/upload_delete.html', context)










def index(request, category_slug=None):
    uploads = None
    category_page=None
    
    if category_slug!=None:
        category_page=get_object_or_404(Category,slug=category_slug)
        uploads=UploadFile.objects.all().filter(category=category_page)
    else :
        uploads=UploadFile.objects.all().filter()

    
    paginator=Paginator(uploads, 8)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1

    try:
        uploadperPage=paginator.page(page)
    except (EmptyPage,InvalidPage):
        uploadperPage=paginator.page(paginator.num_pages)

    return render(request,'index.html',{'uploads':uploadperPage,'category':category_page})








def indextype(request, typefile_slug=None):
    uploads = None
    typefile_page=None
    
    if typefile_slug!=None:
        typefile_page=get_object_or_404(Typefile,slug=typefile_slug)
        uploads=UploadFile.objects.all().filter(typefile=typefile_page)
    else :
        uploads=UploadFile.objects.all().filter()
    
    paginator=Paginator(uploads, 8)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1

    try:
        typeperPage=paginator.page(page)
    except (EmptyPage,InvalidPage):
        typeperPage=paginator.page(paginator.num_pages)




    return render(request,'index.html',{'uploads':typeperPage,'typefile':typefile_page})



def indexpub(request, published_slug=None):
    uploads = None
    published_page=None
    
    if published_slug!=None:
        published_page=get_object_or_404(Published,slug=published_slug)
        uploads=UploadFile.objects.all().filter(published=published_page)
    else :
        uploads=UploadFile.objects.all().filter()
    
    paginator=Paginator(uploads, 8)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1

    try:
        pubperPage=paginator.page(page)
    except (EmptyPage,InvalidPage):
        pubperPage=paginator.page(paginator.num_pages)



    return render(request,'index.html',{'uploads':pubperPage,'published':published_page})






def uploadProductPage(request, category_slug, uploadfile_slug):
    try:
        uploads=UploadFile.objects.get(category__slug=category_slug,slug=uploadfile_slug)
    except Exception as e :
        raise e
    return render(request,'uploads/upload_detail.html',{'uploads':uploads})








def resetPass(request):
    return render(request,'password_reset.html')

def SignUpView(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            #บันทึกข้อมูล User
            form.save()
            #บันทึก Group Customer
            #ดึง username จากแบบฟอร์มมาใช้
            username=form.cleaned_data.get('username')
            #ดึงข้อมูล user จากฐานข้อมูล
            signUpUser=User.objects.get(username=username)
            #จัด Group
            customer_group=Group.objects.get(name="Customer")
            customer_group.user_set.add(signUpUser)

            return redirect('signIn')
        else:
            print(form.errors)
            
            messages.error(request,'ขออภัย, มีบางอย่าผิดพลาด โปรดกรอกข้อมูลอีกครั้ง')
            return redirect('signUp')
    else :
        form=SignUpForm()
    

    return render(request,"signup.html",{'form':form})


def SignInView(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user is not None :
                login(request,user)
                return redirect('home')
            else :
                return redirect('signUp')
    else:
        form=AuthenticationForm()
    return render(request,'signIn.html',{'form':form})

     

def signOutView(request):
    logout(request)
    return redirect('signIn')



@login_required
def profile_detailView(request):

    if request.method =='POST':
        user_form = UserUpdateForm(request.POST , instance=request.user)
        if user_form.is_valid():
            user_form.save()
            
            messages.success(request, f'แก้ไขสำเร็จ')
            return redirect('profileDetail')

    else:
        user_form = UserUpdateForm(instance=request.user) 
    context={
        'user_form':user_form
    }
  

    return render(request, 'profiles/profile_detail.html', context)



@login_required
def profile_formView(request):
    p_form = ProfileUpdateForm()
    if request.method =='POST':
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if p_form.is_valid():
                obj = p_form.save(commit = False)
                obj.user = request.user;
                obj.save()
                return redirect('profileForm')
            else:
                print(p_form.errors)

    context = {'p_form':p_form}
    return render(request, 'profiles/profile_form.html', context)


