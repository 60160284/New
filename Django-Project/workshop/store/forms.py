from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UploadFile,Category,Typefile,Published,Profile,UploadFile
  


class SignUpForm(UserCreationForm):
    first_name=forms.CharField(
        label='ชื่อ',
        max_length=100,
        required=True)

    last_name=forms.CharField(
        label='นามสกุล',
        max_length=100,
        required=True)

    username=forms.CharField(
        label='ชื่อผู้ใช้งาน',
        max_length=100,
        required=True,
        help_text='ชื่อผู้ใช้งานมีตัวอักษรไม่เกิน 30 ตัว สามารถใส่ตัวเลขและอักขระพิเศษ @ /. / + / - / _ เท่านั้น')
    

    email=forms.EmailField(
        label='อีเมล',
        max_length=250,
        required=True,
        help_text='ตัวอย่าง : example@gmail.com')

    password1 = forms.CharField(
        label='รหัสผ่าน', 
        widget=forms.PasswordInput,
        help_text='<ul><li>รหัสผ่านต้องไม่น้อยกว่า 8 ตัวอักษร แต่ไม่เกิน 25 ตัวอักษร</li><li>รหัสผ่านของคุณไม่ควรคล้ายกับข้อมูลส่วนบุคคลอื่น ๆ ของคุณมากเกินไป</li><li>รหัสผ่านของคุณต้องไม่เป็นตัวเลขทั้งหมด</li></ul>'
       
        )
    password2 = forms.CharField(
        label='ยืนยันรหัสผ่าน', 
        widget=forms.PasswordInput,
        help_text='กรุณาใส่รหัสผ่านให้ตรงกันกับรหัสผ่านก่อนหน้านี้ เพื่อยืนยันการสร้างบัญชี'
       
        )
    
    class Meta :
        model=User
        fields=('first_name' ,
        'last_name',
        'username',
        'email',
        'password1',
        'password2')





class UploadFileForm(forms.ModelForm):

    name = forms.CharField(
        label='ชื่อไฟล์งาน',max_length=50,
        help_text="ใส่ชื่อไฟล์เป็นภาษาอังกฤษ")
    

    description= forms.CharField(
        label='คำอธิบาย',
        widget=forms.Textarea(attrs={"rows":5, "cols":20}))

    category=forms.ModelChoiceField(
        label='หมวดหมู่',
        queryset=Category.objects.all())

    typefile=forms.ModelChoiceField(
        label='รูปแบบ',
        queryset=Typefile.objects.all())

    published=forms.ModelChoiceField(
        label='การเผยแพร่',
        queryset=Published.objects.all())

    inputfile=forms.FileField(
        label='เลือกไฟล์',
        help_text='ไฟล์ (เช่น .zip, .ai, .obj, .blender เป็นต้น)'
    )
    image=forms.ImageField(
        label='เลือกไฟล์หน้าปก',
        help_text='ไฟล์ (เช่น .jpeg, .png เป็นต้น)'
    )
   
   
    class Meta:
        model = UploadFile  
        fields =['name','description','category','typefile','published','inputfile','image','price']

  
class UserUpdateForm(forms.ModelForm):
    username=forms.CharField(
        label='ชื่อผู้ใช้งาน',
        max_length=100,
        required=True,
        help_text='ชื่อผู้ใช้งานมีตัวอักษรไม่เกิน 30 ตัว สามารถใส่ตัวเลขและอักขระพิเศษ @ /. / + / - / _ เท่านั้น')

    class Meta:
        model = User
        fields = ['username',
                'first_name',
                'last_name',
                'email']
    
class ProfileUpdateForm(forms.ModelForm):
 

    profile_image=forms.ImageField(
        
        label='เลือกรูปโปรไฟล์',
        help_text='ไฟล์ (เช่น .jpeg, .png เป็นต้น)',
        

    )
    class Meta:
        model = Profile
        fields = ['profile_image']
        
