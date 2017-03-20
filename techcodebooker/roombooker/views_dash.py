from .models import Rooms, Bookings, Companies
from django.http import HttpResponse
from django.shortcuts import render, redirect
import json, datetime
from .forms import CompanyForm, RoomForm, BookingForm
from django.contrib.auth.decorators import login_required

models = {'rooms': Rooms, 'bookings': Bookings, 'companies': Companies}


@login_required
def index(request):
    bookings = Bookings.objects.filter(status=True).order_by('-date')
    context = {'bookings': bookings}
    return render(request, 'communitymanager/index.html', context)


def get_model(model):
    current_date = datetime.date.today()
    models = {}
    models['rooms'] = Rooms.objects.all()
    models['companies'] = Companies.objects.all()
    models['bookings'] = Bookings.objects.filter(date__gte=current_date).order_by('-date')
    return models[model]


def get_modelform(model):
    modelforms = {}
    modelforms['rooms'] = RoomForm
    modelforms['companies'] = CompanyForm
    modelforms['bookings'] = BookingForm
    return modelforms[model]


@login_required
def show_model(request, model):
    render_model = get_model(model)
    context = {model: render_model}
    url = 'communitymanager/{}.html'.format(model)
    return render(request, url, context)


def pendingaction(request):
    action = request.GET.get('action')
    id = int(request.GET.get('id'))
    booking = Bookings.objects.get(pk=id)
    msg = {}
    if action == 'delete':
        booking.delete()
        msg['msg'] = "Pending booking was deleted."
    else:
        booking.status = False
        booking.save()
        msg['msg'] = "Pending booking was approved."
    return HttpResponse(json.dumps(msg), content_type='application/json')


@login_required
def edit_instance(request, model, id):
    instance = models[model].objects.get(pk=id)
    ModForm = get_modelform(model)
    url = '/booker/dashboard/{}'.format(model)
    if request.method == 'POST':
        if request.POST.get('delete'):
            instance.delete()
            return redirect(url)
        request_args = [request.POST]
        if model == 'rooms':
            request_args.append(request.FILES)
        form = ModForm(*request_args, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(url)
    else:
        form = ModForm(instance=instance)
        return render(request, 'communitymanager/edit_form.html', {'form': form})


@login_required
def new_instance(request, model):
    ModForm = get_modelform(model)
    if request.method == "POST":
        request_args = [request.POST]
        if model == 'rooms':
            request_args.append(request.FILES)
        form = ModForm(*request_args)
        if form.is_valid():
            form.save()
            url = '/booker/dashboard/{}'.format(model)
            return redirect(url)
    else:
        form = ModForm()
    return render(request, 'communitymanager/edit_form.html', {'form': form, 'new': True})
