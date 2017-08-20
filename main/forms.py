from django import forms
from main.models import Branch, Locomotive, Mileage


class SelectForm(forms.Form):
    year_choices = sorted(list(set([(m.year, m.year) for m in Mileage.objects.all().order_by('year')])))
    branch_choices = []
    for b in Branch.objects.all():
        series_list = [(l.id, l.series) for l in b.locomotive_set.all()]
        branch_choices.append((b.name, tuple(series_list)))
    branch_choices = tuple(branch_choices)
    branch = forms.CharField(label='Филиал')
    year_start = forms.CharField(label='Начало', max_length=10)
    year_stop = forms.CharField(label='Конец', max_length=10)

    branch.widget = forms.CheckboxSelectMultiple(choices=branch_choices)
    year_start.widget = forms.Select(choices=year_choices)
    year_stop.widget = forms.Select(choices=year_choices)
