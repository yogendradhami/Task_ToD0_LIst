from django.shortcuts import render
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import viewsets, filters

# from .models import *
# from .serializers import ToDoSerializer



from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView,FormView

from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


# Create your views here.
# # code for rest api
# class ToDoViewSet(viewsets.ModelViewSet):
#     queryset=ToDo.objects.all()
#     serializer_class=ToDoSerializer
#     filter_backends=[DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
#     filterset_fields=('title','user','is_complete')
#     search_fields=('title')
#     ordering_fields=('is_complete','created_at','updated_at')


# code for templates and others

# def Home(request):
#     return render(request, 'todo/home.html')


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    fields = '__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('tasks')

class RegisterPage(FormView):
    template_name ='authentication/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user=True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage,self).get(*args, **kwargs)

class TaskList(LoginRequiredMixin,ListView):
    model =Task
    template_name='todo/task_list.html'

    context_object_name= 'tasks'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['tasks']=  context['tasks'].filter(user=self.request.user)
        context['count']=  context['tasks'].filter(is_complete=False).count()

        search_input =self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
        
        context['search_input']= search_input
        return context
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model =Task
    context_object_name='task'
    template_name  = 'todo/task.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    template_name='todo/task_form.html'

    fields =['title', 'description', 'is_complete']
    success_url= reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=  Task
    template_name='todo/task_form.html'

    fields = ['title','description', 'is_complete']
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model=Task
    context_object_name='task'
    success_url = reverse_lazy('tasks')