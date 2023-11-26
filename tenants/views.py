from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from .models import Tenant
from .forms import TenantForm, DomainForm

# Create your views here.
def tenant_list(request):
    tenants = Tenant.objects.all()
    context = {
        'tenants': tenants
    }
    return render(request, 'tenants/tenant_list.html', context)

def create_tenant(request):
    if request.method == 'POST':
        tenant_form = TenantForm(request.POST)
        domain_form = DomainForm(request.POST)
        if tenant_form.is_valid() and domain_form.is_valid():
            tenant = tenant_form.save()
            domain = domain_form.save(commit=False)
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()
            return redirect(reverse('tenant_list'))
    else:
        tenant_form = TenantForm()
        domain_form = DomainForm()

    context = {
        'tenant_form': tenant_form,
        'domain_form': domain_form,
    }
    return render(request, 'tenants/create_tenant.html', context)

def home(request):
    return HttpResponse("Welcome to the Multi-Tenant API Home Page")