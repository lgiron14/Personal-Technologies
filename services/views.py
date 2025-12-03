from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Service, TechnicalReport
from .forms import ClientForm, ServiceForm, TechnicalReportForm

# CRUD for Clients
def client_list(request):
    """
    Muestra la lista de todos los clientes.
    
    Args:
        request: Objeto HttpRequest.
        
    Returns:
        HttpResponse: Renderiza la plantilla 'services/client_list.html'.
    """
    clients = Client.objects.all()
    return render(request, 'services/client_list.html', {'clients': clients})

def client_create(request):
    """
    Crea un nuevo cliente.
    
    Si el método es POST, procesa el formulario.
    Si es GET, muestra un formulario vacío.
    
    Args:
        request: Objeto HttpRequest.
        
    Returns:
        HttpResponse: Renderiza el formulario o redirige a la lista de clientes.
    """
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'services/client_form.html', {'form': form, 'title': 'Crear Cliente'})

def client_update(request, pk):
    """
    Actualiza un cliente existente.
    
    Args:
        request: Objeto HttpRequest.
        pk (int): ID del cliente a editar.
        
    Returns:
        HttpResponse: Renderiza el formulario con datos o redirige.
    """
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
    """
    Elimina un cliente.
    
    Muestra una página de confirmación antes de eliminar.
    
    Args:
        request: Objeto HttpRequest.
        pk (int): ID del cliente a eliminar.
        
    Returns:
        HttpResponse: Renderiza confirmación o redirige tras eliminar.
    """
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'services/client_confirm_delete.html', {'client': client})

# CRUD for Services
def service_list(request):
    """
    Muestra la lista de todos los servicios.
    """
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

def service_create(request):
    """
    Crea un nuevo servicio técnico.
    """
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form': form, 'title': 'Crear Servicio'})

def service_update(request, pk):
    """
    Actualiza un servicio existente.
    """
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
    """
    Elimina un servicio técnico.
    """
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'services/service_confirm_delete.html', {'service': service})

# CRUD for Technical Reports
def report_list(request):
    """
    Muestra la lista de reportes técnicos.
    """
    reports = TechnicalReport.objects.all()
    return render(request, 'services/report_list.html', {'reports': reports})

def report_create(request):
    """
    Crea un nuevo reporte técnico.
    """
    if request.method == 'POST':
        form = TechnicalReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = TechnicalReportForm()
    return render(request, 'services/report_form.html', {'form': form, 'title': 'Crear Reporte Técnico'})

def report_update(request, pk):
    """
    Actualiza un reporte técnico existente.
    """
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
    """
    Elimina un reporte técnico.
    """
    report = get_object_or_404(TechnicalReport, pk=pk)
    if request.method == 'POST':
        report.delete()
        return redirect('report_list')
    return render(request, 'services/report_confirm_delete.html', {'report': report})

# PDF and Email Generation
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from io import BytesIO

import os
from django.conf import settings
from django.contrib.staticfiles import finders

def link_callback(uri, rel):
    """
    Convierte URIs HTML a rutas absolutas del sistema para xhtml2pdf.
    
    Permite que el generador de PDF acceda a recursos estáticos y multimedia.
    
    Args:
        uri (str): La URI del recurso.
        rel (str): La relación del recurso.
        
    Returns:
        str: La ruta absoluta al archivo o la URI original si no se encuentra.
    """
    # Remove leading slash if present to avoid absolute path issues
    if uri.startswith('/'):
        uri = uri[1:]
    
    # Handle static files
    if uri.startswith('static/'):
        # Remove 'static/' prefix
        static_path = uri[7:]  # len('static/') = 7
        result = finders.find(static_path)
        if result:
            return result
    
    # Try to find the file directly
    result = finders.find(uri)
    if result:
        return result
    
    # Handle media files
    if uri.startswith(settings.MEDIA_URL.lstrip('/')):
        media_path = uri.replace(settings.MEDIA_URL.lstrip('/'), '')
        full_path = os.path.join(settings.MEDIA_ROOT, media_path)
        if os.path.isfile(full_path):
            return full_path
    
    # If nothing works, return the original URI
    return uri

def generate_pdf(request, pk):
    """
    Genera un archivo PDF para un reporte técnico específico.
    
    Args:
        request: Objeto HttpRequest.
        pk (int): ID del reporte técnico.
        
    Returns:
        HttpResponse: El archivo PDF generado o un mensaje de error.
    """
    report = get_object_or_404(TechnicalReport, pk=pk)
    template_path = 'services/technical_report_pdf.html'
    context = {'report': report}
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="reporte_{report.id}.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)
    
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    
    if pisa_status.err:
        return HttpResponse('Hubo un error al generar el PDF', status=500)
    return response

def send_report_email(request, pk):
    """
    Envía el reporte técnico por correo electrónico al cliente.
    
    Genera el PDF en memoria y lo adjunta al correo.
    
    Args:
        request: Objeto HttpRequest.
        pk (int): ID del reporte técnico.
        
    Returns:
        HttpResponse: Redirecciona a la lista de reportes con un mensaje de éxito o error.
    """
    report = get_object_or_404(TechnicalReport, pk=pk)
    
    # Generate PDF
    template_path = 'services/technical_report_pdf.html'
    context = {'report': report}
    template = get_template(template_path)
    html = template.render(context)
    
    pdf_file = BytesIO()
    pisa_status = pisa.CreatePDF(
       html, dest=pdf_file, link_callback=link_callback)
    
    if pisa_status.err:
        messages.error(request, 'Error al generar el PDF para el correo.')
        return redirect('report_list')
    
    # Create Email
    subject = f'Reporte Técnico - Servicio #{report.service.id}'
    message = f'Adjunto encontrará el reporte técnico del servicio realizado para {report.service.client.name}.'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [report.service.client.email]
    
    email = EmailMessage(subject, message, email_from, recipient_list)
    email.attach(f'reporte_{report.id}.pdf', pdf_file.getvalue(), 'application/pdf')
    
    try:
        email.send()
        messages.success(request, 'Reporte enviado exitosamente por correo.')
    except Exception as e:
        messages.error(request, f'Error al enviar el correo: {str(e)}')
        
    return redirect('report_list')
