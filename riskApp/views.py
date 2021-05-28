from django.http import HttpResponse
from django.shortcuts import render
from .models import AccountReceivable

def index(request):
    receivables = AccountReceivable.objects.all()
    escope = {}
    escope['receivables'] = receivables
    return render(request, "riskApp/index.html", escope)
