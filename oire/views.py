from django.shortcuts import render


def land(request):
    return render(request, template_name='site/landing.html')