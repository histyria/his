from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from .forms import *
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json  
from luhn_validator import validate
from django.http import JsonResponse
from django.core import serializers



@csrf_exempt
def post_patiant(request):
    if request.method == 'POST':
        rp = json.loads(request.body.decode('utf-8'))
        patiant = patient_file( patiant_no=rp['patiant_no'], ar_patiant_name=rp['ar_patiant_name'],  en_patiant_name=rp['en_patiant_name'] , birth_date = rp['birth_date'] , gender = rp['gender'] , Nationlity = rp['Nationlity'] , social_number = rp['social_number'] , mobile_no = rp['mobile_no'])
        patiant.save()
        data = serializers.serialize('json', patient_file.objects.all())
        return JsonResponse(data, safe=False)


def validate_saudi_id(request):
    saudi_id = request.GET.get('social_number', None)
    data = {
  
        'is_taken':     validate(saudi_id)
    }
    if data['is_taken'] == False:
        data['error_message'] = 'الرقم غير صحسح'
    return JsonResponse(data)

# Create your views here.
def index(request):
    
    return render(request, 'home.html' )

def Create_PatiantFile(request):
    patiant = patient_file.objects.all()
   
    if request.method == 'POST':
        form = patiant_fileForm(request.POST)
        if form.is_valid():
            Patiant_create = form.save(commit=False)
            Patiant_create.save()
            return redirect('HOME:patiant_file')
        else:
            messages.success(request , 'erorr')
    else:
        form = patiant_fileForm()

    context = {
        'form' : form ,  
    }
    return render(request, 'er_rec.html', context)
