from django.shortcuts import render, get_object_or_404
import json
from .models import ArchivoCsv
from .forms import FormularioCsv
from .utils import Csv

# Create your views here.

def Seleccionar(request):

    form = FormularioCsv()
    items = None

    if request.method == 'POST':
        form = FormularioCsv(data=request.POST)
        if form.is_valid():
            archivo = form.cleaned_data['archivo']
            archivo_id = archivo.id
            label = request.POST.get("tipodato")
            try:
                items= archivo_id
                dbCsv = get_object_or_404(ArchivoCsv, id=archivo_id)
                ucsv = dbCsv.csv.path
                csv = Csv(ucsv)
                csv.iniciar()
                #label = 'discrim'
                items= csv.items
                labels = csv.nombreItems()
                data = csv.valoresPreguntasC(label)
                color = csv.colores(label)
                columnas = csv.atributos.values()
            except:
                items = "al mal en el try"
                return render(request,'dashboard/seleccionar.html', {'form': form , 'items': items})

            return  render(request,'dashboard/seleccionar.html', {'form': form,
                                                                      'items': items,
                                                                      'labels': labels,
                                                                      'data': data,
                                                                      'color': color,
                                                                      'label': label,
                                                                      'columnas': columnas,
                                                                      })

    return render(request,'dashboard/seleccionar.html', {'form': form , 'items': items})