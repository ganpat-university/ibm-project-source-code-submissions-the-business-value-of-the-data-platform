from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from django.db.models.functions import TruncMonth
from django.db.models import Count

from .models import Complaints, NewComplaints
from .forms import NewComplaintsForm
import pandas as pd
import datetime
import random

from rest_framework.decorators import api_view
from rest_framework.response import Response

@login_required(login_url="/login/")
def index(request):
    #complaint count
    complaints = Complaints.objects.annotate(month=TruncMonth('dateReceived')).values('month').annotate(complaint_count=Count('state')).values('month', 'complaint_count', 'state')
    df = pd.DataFrame(list(complaints))
    df['month'] = df['month'].astype(str)
    month_list = list(df['month'].unique())
    state_list = list(df['state'].unique())
    df = df.query('state == "{}" or state == "{}"'.format(random.choice(state_list), random.choice(state_list)))
    month_list = pd.DataFrame(month_list)
    groups = df.groupby('state').agg(lambda x: list(x))
    groups = groups.reset_index()
    #complaint count end

    complaint_count = Complaints.objects.all().count()

    customer_disputed_count_Yes = Complaints.objects.filter(customer_disputed='Yes').count()
    customer_disputed_count_No = Complaints.objects.filter(customer_disputed='No').count()

    customer_timely_responded_count_Yes = Complaints.objects.filter(customer_timely_responded='Yes').count()
    customer_timely_responded_count_No = Complaints.objects.filter(customer_timely_responded='No').count()

    state_count = Complaints.objects.values('state').distinct().count()

    group_product_count = Complaints.objects.all().values('product').annotate(total=Count('product')).order_by('total')
    product_count = pd.DataFrame(list(group_product_count))

    context = {
        'state_list': state_list,
        'segment': 'index',

        'line_graph': groups.to_json(),
        'line_graph_month': month_list.to_json(),

        'complaint_count': complaint_count,
        'state_count': state_count,

        'customer_disputed_count_Yes': customer_disputed_count_Yes,
        'customer_disputed_count_No': customer_disputed_count_No,

        'customer_timely_responded_Yes': customer_timely_responded_count_Yes,
        'customer_timely_responded_No': customer_timely_responded_count_No,

        'group_product_count': product_count.to_json(),
    }
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def dynamic_dashboard(request):
    #complaint count
    complaints = NewComplaints.objects.annotate(month=TruncMonth('dateReceived')).values('month').annotate(complaint_count=Count('state')).values('month', 'complaint_count', 'state')
    df = pd.DataFrame(list(complaints))
    df['month'] = df['month'].astype(str)
    month_list = list(df['month'].unique())
    state_list = list(df['state'].unique())
    df = df.query('state == "{}" or state == "{}"'.format(random.choice(state_list), random.choice(state_list)))
    month_list = pd.DataFrame(month_list)
    groups = df.groupby('state').agg(lambda x: list(x))
    groups = groups.reset_index()
    #complaint count end

    complaint_count = NewComplaints.objects.all().count()

    customer_disputed_count_Yes = NewComplaints.objects.filter(customer_disputed='Yes').count()
    customer_disputed_count_No = NewComplaints.objects.filter(customer_disputed='No').count()

    customer_timely_responded_count_Yes = NewComplaints.objects.filter(customer_timely_responded='Yes').count()
    customer_timely_responded_count_No = NewComplaints.objects.filter(customer_timely_responded='No').count()

    state_count = NewComplaints.objects.values('state').distinct().count()

    group_product_count = NewComplaints.objects.all().values('product').annotate(total=Count('product')).order_by('total')
    product_count = pd.DataFrame(list(group_product_count))

    context = {
        'state_list': state_list,
        'segment': 'index',

        'line_graph': groups.to_json(),
        'line_graph_month': month_list.to_json(),

        'complaint_count': complaint_count,
        'state_count': state_count,

        'customer_disputed_count_Yes': customer_disputed_count_Yes,
        'customer_disputed_count_No': customer_disputed_count_No,

        'customer_timely_responded_Yes': customer_timely_responded_count_Yes,
        'customer_timely_responded_No': customer_timely_responded_count_No,

        'group_product_count': product_count.to_json(),
    }
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def register_complaint(request):
    context = {}
    form = NewComplaintsForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        html_template = loader.get_template('home/complaint_registered.html')
        return HttpResponse(html_template.render(context, request))
    
    context['form']= form    
    html_template = loader.get_template('home/register_complaint.html')
    return HttpResponse(html_template.render(context, request))

@api_view(['GET'])
def get_state_data(request, state):
    try:
        complaints = Complaints.objects.annotate(month=TruncMonth('dateReceived')).values('month').annotate(complaint_count=Count('state')).values('month', 'complaint_count', 'state')
        df = pd.DataFrame(list(complaints))
        df['month'] = df['month'].astype(str)
        df = df.query('state == "{}"'.format(state))
        groups = df.groupby('state').agg(lambda x: list(x))
        groups = groups.reset_index()
    except Post.DoesNotExist:
        return HttpResponse(status=404)
    if len(groups) == 0:
        try:
            complaints = NewComplaints.objects.annotate(month=TruncMonth('dateReceived')).values('month').annotate(complaint_count=Count('state')).values('month', 'complaint_count', 'state')
            df = pd.DataFrame(list(complaints))
            df['month'] = df['month'].astype(str)
            df = df.query('state == "{}"'.format(state))
            groups = df.groupby('state').agg(lambda x: list(x))
            groups = groups.reset_index()
        except Post.DoesNotExist:
            return HttpResponse(status=404)
    if request.method == 'GET':
        return Response(groups)