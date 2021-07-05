from django.http import JsonResponse
from django.shortcuts import render
from apps.finance.models import IPC, PurchaseOrder
from django.core import serializers

def dashboard_with_pivot(request):
    return render(request, 'dashboard/index.html', {})

def pivot_data(request):
    dataset = PurchaseOrder.objects.all().order_by('-date')
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)