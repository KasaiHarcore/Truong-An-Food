from django import forms
import re

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    username = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=10)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
      email = self.cleaned_data.get('email')  
      if not re.match(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email):
        raise forms.ValidationError('email không hợp lệ')
      return email

    def clean_phone(self):
      phone = self.cleaned_data.get('phone')
      if not re.match(r'^\d{10}$', phone): 
        raise forms.ValidationError('Số điện thoại không hợp lệ')
      return phone    

    def clean(self):
      cleaned_data = super().clean()
      p1 = cleaned_data.get("password1")
      p2 = cleaned_data.get("password2")

      if p1 and p2 and p1 != p2:
          raise forms.ValidationError("Mật khẩu không trùng khớp, vui lòng nhập lại")
      if len(p1) < 8:
          raise forms.ValidationError("Mật khẩu phải có ít nhất 8 ký tự")
      if not re.match(r'^[a-zA-Z0-9]+$', p1):
          raise forms.ValidationError("Mật khẩu chỉ được chứa ký tự và số (Ít nhất 1 chữ hoa, 1 chữ thường và 1 số)")
      return cleaned_data
