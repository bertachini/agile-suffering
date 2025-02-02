from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Lead
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import LeadForm, LeadFilterForm  # You'll need to create this form
from django.db.models import Q  # Add this import at the top
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home.html')  # Certifique-se de que 'home.html' existe no diretório de templates.

# Funções de autenticação
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('lead_list')
        else:
            messages.error(request, 'Registration failed. Please check your input.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            logger.debug(f"Authentication attempt for user {username}: {'successful' if user else 'failed'}")
            if user is not None:
                login(request, user)
                logger.debug(f"Login successful for user {username}")
                messages.success(request, 'Login successful!')
                return redirect('lead_list')
            else:
                logger.debug(f"Login failed for user {username}")
                messages.error(request, 'Invalid username or password.')
        else:
            logger.debug(f"Form validation failed: {form.errors}")
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



# Adicione o decorador @login_required para todas as views que precisam de autenticação
@login_required
def lead_list(request):
    search_query = request.GET.get('search', '')
    leads = Lead.objects.all()
    
    if search_query:
        leads = leads.filter(
            Q(name__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    
    filter_form = LeadFilterForm(request.GET)
    
    return render(request, 'lead_list.html', {
        'leads': leads,
        'filter_form': filter_form,
        'search_query': search_query,
    })

@login_required
def lead_create(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            messages.success(request, 'Lead created successfully!')
            return redirect('lead_list')
    else:
        form = LeadForm()
    
    return render(request, 'lead_create.html', {'form': form})

@login_required
def lead_update(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lead updated successfully!')
            return redirect('lead_list')
    else:
        form = LeadForm(instance=lead)
    
    return render(request, 'lead_update.html', {'form': form, 'lead': lead})

@login_required
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    
    if request.method == 'POST':
        lead.delete()
        messages.success(request, 'Lead deleted successfully!')
        return redirect('lead_list')
    
    return render(request, 'lead_confirm_delete.html', {'lead': lead})

@login_required
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, 'lead_detail.html', {'lead': lead})
