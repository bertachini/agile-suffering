from django.shortcuts import render, redirect, get_object_or_404
from .models import Lead
from django.contrib import messages

def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'app/lead_list.html', {'leads': leads})

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

def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    
    if request.method == 'POST':
        lead.delete()
        messages.success(request, 'Lead deleted successfully!')
        return redirect('lead_list')
    
    return render(request, 'app/lead_confirm_delete.html', {'lead': lead})

def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, 'app/lead_detail.html', {'lead': lead})
