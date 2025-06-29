from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
# from django.views.templates import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the Contact Management System")

# class ContactListView(ListView):
#     model = Contact
#     template_name = 'contacts/contact_list.html'
#     context_object_name = 'contacts'

# class ContactDetailView(DetailView):
#     model = Contact
#     template_name = 'contacts/contact_detail.html'
#     context_object_name = 'contact'

# class ContactCreateView(CreateView):
#     model = Contact
#     template_name = 'contacts/contact_form.html'
#     fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']
#     success_url = '/contacts/'

# class ContactUpdateView(UpdateView):
#     model = Contact
#     template_name = 'contacts/contact_form.html'
#     fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']
#     success_url = '/contacts/'

# class ContactDeleteView(DeleteView):
#     model = Contact
#     template_name = 'contacts/contact_confirm_delete.html'
#     success_url = '/contacts/'

# def home(request):
#     return render(request, 'contacts/home.html')


