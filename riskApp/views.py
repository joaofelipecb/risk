from django.http import HttpResponse
from django.shortcuts import render
from .models import AccountReceivable
import riskApp.p26struct.ProbabilityMultiplicity

def index(request):
    receivables = AccountReceivable.objects.all()
    probability = riskApp.p26struct.ProbabilityMultiplicity.ProbabilityMultiplicity(receivables)
    probability.calculate()
    escope = {}
    escope['receivables'] = receivables
    escope['probability'] = probability
    return render(request, "riskApp/index.html", escope)
