from django.shortcuts import render, HttpResponse, redirect, Http404
from django.views.decorators.csrf import csrf_exempt
from main.models import Branch, Locomotive, Mileage
from main.forms import SelectForm
import pandas
import json


# def page_view(request):
#
#     data = {
#         'form': SelectForm()
#     }
#     return render(request, 'main/template.html', data)


def page_view(request):
    year_choices = sorted(list(set([m.year for m in Mileage.objects.all().order_by('year')])))
    branch_choices = {}
    for b in Branch.objects.all():
        series_list = [(l.id, l.series) for l in b.locomotive_set.all()]
        branch_choices[b.name] = tuple(series_list)
    data = {
        'years': year_choices,
        'branches': branch_choices,
    }
    return render(request, 'main/template2.html', data)


# @csrf_exempt
# def on_submit(request):
#     if request.is_ajax():
#         print(request.POST)
#         form = SelectForm(request.POST)
#         if form.is_valid():
#             branches = form.cleaned_data['branch']
#             year_start = form.cleaned_data['year_start']
#             year_stop = form.cleaned_data['year_stop']
#             branches = branches[2:-2].split('\', \'') # Перевод строки в список
#             locos = Locomotive.objects.filter(id__in=branches)
#             data = {}
#             for loco in locos:
#                 ml = Mileage.objects.filter(locomotive=loco).filter(year__range=(year_start, year_stop))
#                 bn = "".join([sn[0] for sn in loco.branch.name.split('-')])
#                 loco_str = "{1} ({0})".format(bn, loco.series)
#                 data['years'] = [m.year for m in ml]
#                 data[loco_str] = [m.value*loco.rate for m in ml]
#             print(data)
#             return HttpResponse(json.dumps(data), 'application/javascript')
#         else:
#             print(form.errors)


@csrf_exempt
def on_submit(request):
    if request.is_ajax():
        # print(request.POST)
        branches = request.POST.getlist('branch')
        year_start = request.POST['year_start']
        year_stop = request.POST['year_stop']
        locos = Locomotive.objects.filter(id__in=branches)
        data = {}
        for loco in locos:
            ml = Mileage.objects.filter(locomotive=loco).filter(year__range=(year_start, year_stop))
            bn = "".join([sn[0] for sn in loco.branch.name.split('-')])
            loco_str = "{1} ({0})".format(bn, loco.series)
            data['years'] = [m.year for m in ml]
            data[loco_str] = [m.value*loco.rate for m in ml]
        # print(data)
        return HttpResponse(json.dumps(data), 'application/javascript')


def drop_objects(request):
    Branch.objects.all().delete()
    Locomotive.objects.all().delete()
    Mileage.objects.all().delete()
    return HttpResponse("Delete Success")


def reload_view(request):
    rate_dt = pandas.read_excel(io='test_LT.xlsx', sheetname='Ставка за км')
    mileage_dt = pandas.read_excel(io='test_LT.xlsx', sheetname='Пробег')
    ma_list = []
    for index in mileage_dt.index:
        branch_name = mileage_dt.iloc[index]['Филиал']
        loco_name = mileage_dt.iloc[index]['Серия']
        print(loco_name)
        loco_rate = rate_dt[rate_dt['Серия'] == loco_name]['Ставка'].values[0]
        branch, branch_created = Branch.objects.get_or_create(name=branch_name)
        loco = Locomotive.objects.create(series=loco_name, rate=loco_rate, branch=branch)
        loco.save()
        for year in mileage_dt.columns[2:]:
            year_value = mileage_dt.iloc[index][year]
            ma = Mileage(year=year, value=year_value, locomotive=loco)
            ma_list.append(ma)
    Mileage.objects.bulk_create(ma_list)
    return HttpResponse("Success")