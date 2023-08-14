# Create your views here.
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.mail import send_mail
from .helpers import send_forget_password_mail
import uuid
from .models import Profile
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from .forms import PasswordChangingForm


# Create your views here.

# dashboard page

def Dashboard(request):
    return render(request,'authentication/dashboard.html')

# class view  for logout

class LogoutPage(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You're Logged Out !!")
        return redirect('user_login')
    
    
    # class view for login

class LoginPage(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        check = request.POST['check']

        user = auth.authenticate(request, username= username, password= password,check=check)

        if user:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('tasks')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('user_login')


# class view for register page

class RegisterPage(View):
    def get(self,  request):
        return render(request,'authentication/register.html')
    
    def post(self, request):
        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        email= request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
            # user validation
            user = User.objects.get(username=username)
            if user:
                messages.error(request, 'Username already exists. Try with new one!')
                return redirect('user_registration')
        
        except:
            data = User.objects.create_user(first_name= first_name, last_name= last_name, email=email, username=username,password=password)

            messages.success(request, 'Account has been created successfully!')
            # send_mail(
            #     'Account Creation |  HMS', #subject
            #     'Your account has been created! \n Welcome \n' +
            #     data.username, #message
            #     'yogendradhami631@gmail.com', # sender
            #     [data.email] #reciever
            # )
            data.save()
            return redirect('user_login')
        

# def ChangePassword(request,token):
#     context={}
#     try:
#         profile_obj =Profile.objects.filter(forget_password_token =token).first()
#         context  = {'user_id': profile_obj.user.id}
        
#         if request.method=='POST':
#             new_password=request.POST.get('new_password')
#             confirm_password=request.POST.get('reconfirm_password')
#             user_id=request.POST.get('user_id')

#             if user_id is not None:
#                 messages.success(request, "NO user id found.")
#                 return render(f'change-password{token}')
            

#             if new_password != confirm_password:
#                 messages.success(request, "Both should be equal.")
#                 return render(f'change-password{token}')
            
#             user_obj =User.objects.get(id=user_id)
#             user_obj.set_password(new_password)
#             user_obj.save()
#             return redirect('user-login')

#         context  = {'user_id': profile_obj.user.id}

#     except Exception as e:
#         print(e)
#     return render(request, 'authentication/change_password.html',context)

# def forgetPassword(request):
#     try:
#         if request.method == 'POST':
#             username=request.POST.get('username')

#             if not User.objects.filter(username=username).first():
#                 messages.success(request, 'No user found with this username.')
#                 return redirect('forgot-password')
            
#             user_obj= User.objects.get(username=username)
#             token =str(uuid.uuid4())
#             profile_obj = Profile.objects.get(user=user_obj)
#             profile_obj.forgot_password_token=token
#             profile_obj.save()
#             send_forget_password_mail(user_obj, token)
#             messages.success(request, 'An email is sent.')
#             return redirect('forgot-password')


#     except Exception as e:
#         print(e)
#     return render(request, 'authentication/forgot_password.html')


# class view for change password

class PasswordsChangeView(PasswordChangeView):
    form_class  = PasswordChangingForm
    # from_class= PasswordChangeForm
    # messages.success(request, "Your Password has been Changed Successfully!!!")
    success_url=reverse_lazy('user_login')