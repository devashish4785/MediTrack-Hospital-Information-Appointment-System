from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import patient,patientclinicaldata
from .forms import patient_form,clinicdataform
from django.views.generic import ListView,DeleteView,UpdateView,CreateView,View
from django.http import HttpResponse

# Create your views here.
class patientindexview(ListView):
    model=patient

class patientcreateview(View):
    def get(self,request):
        form=patient_form()

        return render(request,'labuser/patient_form.html',{'form':form})

    def post(self,request):
        form=patient_form(request.POST)
        print('before form')
        if form.is_valid():
            print('valid form')
            form.save()
        return redirect('/')

class patientupdateview(UpdateView):
    model=patient
    fields=('firstname','lastname','age','gender','address','phone','email',)
    success_url=reverse_lazy('index')
    #template_name for manualo template

class patientdeleteview(DeleteView):
    model=patient
    success_url=reverse_lazy('index')
    template_name='labuser/patient_delete.html'

def addclinicdata(request,**kwargs):
    form=clinicdataform()
    pat=patient.objects.get(id=kwargs['pk'])
    if request.method=='POST':
        form=clinicdataform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'labuser/clinicdataadd.html',{'form' : form,'patient':pat})

def clinic_data_analyze(request,id):
    form=clinicdataform()
    pat=patient.objects.get(id=id)
    try:
        pat_data=patientclinicaldata.objects.get(Patient=id)
        bmi=pat_data.weight*(10**4)/(pat_data.height**2)
        return render(request,'labuser/clinic_data_analyze.html',{'patient':pat_data,'bmi':round(bmi,2)})
    except:
        return render(request,'labuser/clinicdataadd.html',{'form' : form,'patient':pat})

def patient_detail(request,id):
    pat=patient.objects.get(id=id)
    try:
        clinic_data=patientclinicaldata.objects.get(Patient=id)
        bmi=clinic_data.weight*(10**4)/(clinic_data.height**2)

        if request.method=='POST':
            clinic_data=clinicdataform(REQUEST.post)
            if clinic_data.is_valid():
                clinic_data.save()
        return render(request,'labuser/patient_detail.html',{'patient':pat,'bmi':round(bmi,2),'clinic_data':clinic_data})
    except:
        return render(request,'labuser/patient_detail.html',{'patient':pat,'clinic_data':None})
