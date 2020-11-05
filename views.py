from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect
from .models import Member
from django.contrib.auth import authenticate, login, logout
from .Form import CreateUserForm, MemberForm
from formtools.wizard.views import SessionWizardView
from .Form import *

# class FormWizardView(SessionWizardView):
#     template_name = "member/combined.html"
#     form_list = [UserCreationForm,MemberForm]
#     def done(self, form_list, **kwargs):
#         form_data = process_form_data(form_list)
#         return request('member/done.html',{'form_data':form_data})
# def process_form_data(form_list):
#     form_data = [form.cleaned_data for form in form_list]
def index(request):
    member = Member.objects.get(user=request.user)
    return render(request, 'member/index.html', {'member': member})


def details(request, id):
    member = Member.objects.get(pk=id)
    return render(request, 'member/details.html', {'member': member})


def l_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

    context = {}
    return render(request, 'member/login.html', context)

def next(request):
    context = {}
    return render(request, 'member/member_form.html', context)
def logoutt(request):
    logout(request)
    return l_login(request)


def register(request):
    form = CreateUserForm()
    mem_form = MemberForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        mem_form = MemberForm(request.POST)
        if form.is_valid() and mem_form.is_valid():
            user = form.save()
            profile = mem_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("login") 
    context = {"form": form,'mem_form':mem_form}
    return render(request, 'member/register.html', context)


def settings(request, id):
    member = Member.objects.get(pk=id)
    form = MemberForm(instance=member)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'member/settings.html', context)


def register_step1(request):
    Initial = {'Name': request.session.get('Name', None),
    'Email': request.session.get('Email', None),
    'Field': request.session.get('Field', None),
    'Query': request.session.get('Query', None)}
    mem_form = MemberForm(request.POST,initial=Initial)
    if request.method == "POST":
        if mem_form.is_valid():
            request.session['Name'] = mem_form.cleaned_data['Name']
            request.session['Field'] = mem_form.cleaned_data['Field']
            request.session['Email'] = mem_form.cleaned_data['Email']
            request.session['Query'] = mem_form.cleaned_data['Query']
            return HttpResponseRedirect(reverse('Step2'))
    context = {'mem_form':mem_form}
    return render(request, 'member/member_form.html', context)



def register_step2(request):
    form = CreateUserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            member = Member.objects.create(
                user = user,
                Name = request.session['Name'],
                Field=request.session['Field'],
                Email=request.session['Email'],
                Query=request.session['Query']
            )
            member.save()
            return redirect("login") 
    context = {"form": form}
    return render(request, 'member/register.html', context)














































