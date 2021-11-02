from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import chemicals
from datetime import datetime
from .utls import download_csv
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required(login_url='login')
def home_page(request):
    chemical = chemicals.objects.all()
    context = {'chemical':chemical}
    return render(request,'chemicals/home_page.html',context)

def startpage(request):
    chemical = chemicals.objects.all()
    context = {'chemical':chemical}
    return render(request,'chemicals/start.html',context)

@login_required(login_url='login')
def addtosql(request):
    adate = request.POST['arrive_date']
    edate = request.POST['expire_date']
    adate = datetime.strptime(adate,'%Y-%m-%d').strftime('%Y-%m-%d')
    edate = datetime.strptime(edate, '%Y-%m-%d').strftime('%Y-%m-%d')
    name = request.POST['name']
    vender = request.POST['vender']
    experiment = request.POST['experiment']
    register = chemicals(name = name,
                         vender = vender,
                         experiment = experiment,
                         arrive_date = adate,
                         expire_date= edate
                         )
    register.save()
    return redirect('/home/')

@login_required(login_url='login')
def detail(request):
    return render(request,'chemicals/detail.html')

@login_required(login_url='login')
def detailpage2(request, id):
    chemical = chemicals.objects.get(id=id)
    ardate = chemical.arrive_date
    ardate = ardate.strftime('%Y-%m-%d')
    exdate = chemical.expire_date
    exdate = exdate.strftime('%Y-%m-%d')
    context = {"chemical":chemical,'ardate':ardate,'exdate':exdate}
    return render(request, 'chemicals/detailedPage2.html', context)

@login_required(login_url='login')
def modifysql(request):
    itemid = request.POST['itemid']
    name = request.POST['name']
    vender = request.POST['vender']
    experiment = request.POST['experiment']
    adate = request.POST['arrive_date']
    edate = request.POST['expire_date']
    adate = datetime.strptime(adate, '%Y-%m-%d').strftime('%Y-%m-%d')
    edate = datetime.strptime(edate, '%Y-%m-%d').strftime('%Y-%m-%d')
    chemical =  chemicals.objects.get(id=itemid)
    chemical.name = name
    chemical.vender = vender
    chemical.experiment = experiment
    chemical.arrive_date = adate
    chemical.expire_date = edate
    chemical.save()
    return redirect('/home/')

@login_required(login_url='login')
def deleteItem(request,id):
    item = chemicals.objects.get(id=id)
    if request:
        item.delete()
        return redirect('/home/')
    else:
        return redirect('/home/')


 # def printDymo(request):

@login_required(login_url='login')
def export_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    data = download_csv(request, chemicals.objects.all())
    response = HttpResponse(data, content_type='text/csv')
    return response

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request,'Incorrect username or password')
        return render(request,'chemicals/login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            a = str(request.POST.get('email')).split('@')
            if form.is_valid() and a[1]=='ke-instruments.com':
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+ user)
                return redirect('login')
            elif form.errors:
                pass
            else:
                messages.info(request, 'Only KEI users allowed')
        context = {'form':form}
        return render(request,'chemicals/signup.html',context)


def logoutUser(request):
    logout(request)
    return redirect('start')

def searchedResults(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        chemical = chemicals.objects.filter(Q(name__contains = searched) | Q(id__contains = searched))
        return render(request, 'chemicals/searchedResults.html',{'chemical':chemical})

def print(request,id):
    chemical = chemicals.objects.get(id=id)
    expire_date = str(chemical.expire_date)
    context = {'chemical':chemical,'expire_date':expire_date}
    return render(request,'chemicals/printpage.html',context)