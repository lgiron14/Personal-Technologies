from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'company/about.html')

def history(request):
    return render(request, 'company/history.html')

def team(request):
    return render(request, 'company/team.html')

# Service Pages
def service_support(request):
    return render(request, 'services_pages/support.html')

def service_development(request):
    return render(request, 'services_pages/development.html')

def service_networks(request):
    return render(request, 'services_pages/networks.html')

def service_cloud(request):
    return render(request, 'services_pages/cloud.html')

def service_security(request):
    return render(request, 'services_pages/security.html')

def service_consulting(request):
    return render(request, 'services_pages/consulting.html')