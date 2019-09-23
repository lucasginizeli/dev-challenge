import logging

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from core.models import Registro0000, Registro0150, RegistroC100, RegistroC170
from core.utils import Util
from django.urls import reverse
from django.forms import ModelForm


class Registro0000Form(ModelForm):
    class Meta:
        model = Registro0000
        fields = ['data_inicial', 'data_final', 'nome', 'cnpj']


class Registro0150Form(ModelForm):
    class Meta:
        model = Registro0150
        fields = ['cod_participante', 'nome', 'cod_pais', 'cnpj']


class RegistroC100Form(ModelForm):
    class Meta:
        model = RegistroC100
        fields = ['cod_participante', 'cod_modelo', 'cod_situacao', 'serie', 'numero_documento', 'chave_nfe',
                  'data_documento', 'data_entrada_saida', 'valor_documento']


class RegistroC170Form(ModelForm):
    class Meta:
        model = RegistroC170
        fields = ['numero_item', 'cod_item', 'descricao', 'quantidade', 'unidade', 'valor_item']


def index(request):
    return render(request, 'index.html')


def list(request, tipo):
    data = dict()
    data['tipo'] = tipo

    if tipo == '0000':
        lista_registro = Registro0000.objects.all()
        data['lista_registro'] = lista_registro
        return render(request, 'list.html', data)
    elif tipo == '0150':
        lista_registro = Registro0150.objects.all()
        data['lista_registro'] = lista_registro
        return render(request, 'list.html', data)
    elif tipo == 'C100':
        lista_registro = RegistroC100.objects.all()
        data['lista_registro'] = lista_registro
        return render(request, 'list.html', data)
    elif tipo == 'C170':
        lista_registro = RegistroC170.objects.all()
        data['lista_registro'] = lista_registro
        return render(request, 'list.html', data)


def edit(request, tipo, pk):

    registro = Util.solve_register(tipo, pk)

    if tipo == '0000':
        form = Registro0000Form(request.POST or None, instance=registro)
    elif tipo == '0150':
        form = Registro0150Form(request.POST or None, instance=registro)
    elif tipo == 'C100':
        form = RegistroC100Form(request.POST or None, instance=registro)
    elif tipo == 'C170':
        form = RegistroC170Form(request.POST or None, instance=registro)
    else:
        logging.getLogger("error_logger").error("Tipo registro não encontrado")
        return redirect('index')

    if form.is_valid():
        form.save()
        return redirect('list', tipo)

    return render(request, 'edit.html', {'form': form})


def delete(request, tipo, pk):

    registro = Util.solve_register(tipo, pk)

    if request.method == 'POST':
        registro.delete()
        return redirect('list', tipo)

    return render(request, 'delete_confirm.html', {'object': registro, 'tipo': tipo})


def upload_csv(request):

    data = {}
    if "GET" == request.method:
        return render(request, "upload_csv.html", data)

    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return HttpResponseRedirect(reverse("upload_csv"))
        # if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
            return HttpResponseRedirect(reverse("upload_csv"))

        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")

        for line in lines:
            fields = line.split("|")
            type_data = fields[1]
            data_dict = dict()
            if type_data == '0000':
                data_dict["data_inicial"] = Util.datetime_format(fields[2])
                data_dict["data_final"] = Util.datetime_format(fields[3])
                data_dict["nome"] = fields[4]
                data_dict["cnpj"] = fields[5]
                form = Registro0000Form(data_dict)
                Util.save_form(form)
            elif type_data == '0150':
                data_dict["cod_participante"] = fields[2]
                data_dict["nome"] = fields[3]
                data_dict["cod_pais"] = fields[4]
                data_dict["cnpj"] = fields[5]
                form = Registro0150Form(data_dict)
                Util.save_form(form)
            elif type_data.upper() == 'C100':
                data_dict["cod_participante"] = fields[2]
                data_dict["cod_modelo"] = fields[3]
                data_dict["cod_situacao"] = fields[4]
                data_dict["serie"] = fields[5]
                data_dict["numero_documento"] = fields[6]
                data_dict["chave_nfe"] = fields[7]
                data_dict["data_documento"] = Util.datetime_format(fields[8])
                data_dict["data_entrada_saida"] = Util.datetime_format(fields[9])
                data_dict["valor_documento"] = Util.parse_decimal(fields[10])
                form = RegistroC100Form(data_dict)
                Util.save_form(form)
            elif type_data.upper() == 'C170':
                data_dict["numero_item"] = fields[2]
                data_dict["cod_item"] = fields[3]
                data_dict["descricao"] = fields[4]
                data_dict["quantidade"] = Util.parse_decimal(fields[5])
                data_dict["unidade"] = fields[6]
                data_dict["valor_item"] = Util.parse_decimal(fields[7])
                form = RegistroC170Form(data_dict)
                Util.save_form(form)

    except Exception as e:
        logging.getLogger("error_logger").error("Não foi possível processar o upload " + repr(e))
        messages.error(request, "Não foi possível processar o upload " + repr(e))

    return HttpResponseRedirect(reverse("upload_csv"))


