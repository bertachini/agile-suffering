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

def home(request):
    return render(request, 'home.html')  # Certifique-se de que 'home.html' existe no diretório de templates.

# Funções de autenticação
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect('lead_list')
        else:
            messages.error(request, 'Erro no registro. Por favor, verifique os dados.')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('lead_list')
        messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



# Adicione o decorador @login_required para todas as views que precisam de autenticação
@login_required
def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'app/lead_list.html', {'leads': leads})

@login_required
def lead_create(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        whatsapp = request.POST.get('whatsapp')
        facebook = request.POST.get('facebook')
        
        # Create new lead
        Lead.objects.create(
            name=name,
            email=email,
            phone=phone,
            whatsapp=whatsapp,
            facebook=facebook
        )
        messages.success(request, 'Lead created successfully!')
        return redirect('lead_list')
    
    return render(request, 'app/lead_form.html')

@login_required
def lead_update(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    
    if request.method == 'POST':
        # Update lead data
        lead.name = request.POST.get('name')
        lead.email = request.POST.get('email')
        lead.phone = request.POST.get('phone')
        lead.whatsapp = request.POST.get('whatsapp')
        lead.facebook = request.POST.get('facebook')
        lead.save()
        
        messages.success(request, 'Lead updated successfully!')
        return redirect('lead_list')
    
    return render(request, 'app/lead_form.html', {'lead': lead})

@login_required
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    
    if request.method == 'POST':
        lead.delete()
        messages.success(request, 'Lead deleted successfully!')
        return redirect('lead_list')
    
    return render(request, 'app/lead_confirm_delete.html', {'lead': lead})

@login_required
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, 'app/lead_detail.html', {'lead': lead})
