from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Service, TechnicalReport
from .forms import ClientForm, ServiceForm, TechnicalReportForm

# CRUD for Clients
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'services/client_list.html', {'clients': clients})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'services/client_form.html', {'form': form, 'title': 'Crear Cliente'})

def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'services/client_form.html', {'form': form, 'title': 'Editar Cliente'})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'services/client_confirm_delete.html', {'client': client})

# CRUD for Services
def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form': form, 'title': 'Crear Servicio'})

def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/service_form.html', {'form': form, 'title': 'Editar Servicio'})

def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'services/service_confirm_delete.html', {'service': service})

# CRUD for Technical Reports
def report_list(request):
    reports = TechnicalReport.objects.all()
    return render(request, 'services/report_list.html', {'reports': reports})

def report_create(request):
    if request.method == 'POST':
        form = TechnicalReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = TechnicalReportForm()
    return render(request, 'services/report_form.html', {'form': form, 'title': 'Crear Reporte Técnico'})

def report_update(request, pk):
    report = get_object_or_404(TechnicalReport, pk=pk)
    if request.method == 'POST':
        form = TechnicalReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = TechnicalReportForm(instance=report)
    return render(request, 'services/report_form.html', {'form': form, 'title': 'Editar Reporte Técnico'})

def report_delete(request, pk):
    report = get_object_or_404(TechnicalReport, pk=pk)
    if request.method == 'POST':
        report.delete()
        return redirect('report_list')
    return render(request, 'services/report_confirm_delete.html', {'report': report})
