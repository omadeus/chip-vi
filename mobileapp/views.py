from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .models import Database
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
import json
import os
from cv2 import cv2
import imread
from werkzeug.utils import secure_filename
from datetime import datetime
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':

        print('zapros proshel')
        file = request.FILES['file']
        print(file)
        file.filename = '123.jpg'
        filename = secure_filename(file.filename)
        fs = FileSystemStorage(location='mobileapp/pics')
        filename = fs.save('123.jpg', file)
        print('foto-s')
        print('foto-s')
        redirect('/')
        CURRENT_FRAME = [cv2.imread('mobileapp/pics/123.jpg'), None]
        CURRENT_FRAME[1] = imread.analyse_frame_with_nnet(CURRENT_FRAME[0])
        image = CURRENT_FRAME[1]

        time_now = datetime.now().timestamp()
        tom = str(time_now)
        user_image = 'mobileapp/pics/123.png'
        cv2.imwrite(user_image, image)
        os.remove('mobileapp/pics/123.jpg')

        return render(request, "mobileapp/index2.html", {'user_image': user_image})

    else:
        return render(request, "mobileapp/index.html")

def logic_1(request):
    return render(request, 'mobileapp/logic_1.html')
def logic_1_no(request):
    return render(request, 'mobileapp/logic_1_no.html')
def logic_1_no_no(request):
    return render(request, 'mobileapp/logic_1_no_no.html')
def logic_2(request):
    return render(request, 'mobileapp/logic_2.html')
def logic_2_no(request):
    return render(request, 'mobileapp/logic_2_no.html')
def logic_2_yes(request):
    return render(request, 'mobileapp/logic_2_yes.html')
def logic_3(request):
    return render(request, 'mobileapp/logic_3.html')


def register(request):
    if request.method == 'POST':
        print('1')
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print('2')
            user = form.save()
            login(request, user)
            messages.success(request, _('Вы успешно зарегестрировались'))
            return redirect('website')
        else:
            print('3')
            messages.error(request, _('Ошибка регистрации'))

    else:
        print('4')
        form = UserRegisterForm()
    return render(request, 'mobileapp/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('website')
    else:
        form = UserLoginForm()
    return render(request, 'mobileapp/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('website')

def website(request):
    if request.method == 'POST':  # and 'image' in request.files:

        print('zapros proshel')
        file = request.FILES['file']

        file.filename = '123.jpg'
        filename = secure_filename(file.filename)
        last = Database.objects.last()
        id = last.id
        print(f'id===={id}')
        fs = FileSystemStorage(location='mobileapp/pics/database')
        filename = fs.save(f'{id}.jpg', file)
        last.photo = f'/mobileapp/pics/database/{id}.jpg'
        last.save()
        print('foto-s')
        print('foto-s')
        return render(request, 'mobileapp/web.html')
    else:
        return render(request, 'mobileapp/web.html')
def save(request):
    if request.method == 'POST':  # and 'image' in request.files:

        print('zapros proshel')
        c_1 = Database(mother_name = request.POST['mother_1'],
                        mother_mark = request.POST['mother_2'],
                        mother_type = request.POST['mother_3'],
                        mother_made = request.POST['mother_4'],
                        mother_doc = request.POST['mother_5'],
                        mother_status = request.POST['mother_6'],
                        red_type = request.POST['red_1'],
                        red_mark = request.POST['red_2'],
                        red_designation = request.POST['red_3'],
                        red_nominal = request.POST['red_4'],
                        red_efficiency = request.POST['red_5'],
                        red_made = request.POST['red_6'],
                        red_doc = request.POST['red_7'],
                        red_status = request.POST['red_8'],
                        yellow_type = request.POST['yellow_1'],
                        yellow_mark = request.POST['yellow_2'],
                        yellow_designation = request.POST['yellow_3'],
                        yellow_nominal = request.POST['yellow_4'],
                        yellow_efficiency = request.POST['yellow_5'],
                        yellow_made = request.POST['yellow_6'],
                        yellow_doc = request.POST['yellow_7'],
                        yellow_status = request.POST['yellow_8'],
                        orange_type = request.POST['orange_1'],
                        orange_mark = request.POST['orange_2'],
                        orange_designation = request.POST['orange_3'],
                        orange_nominal = request.POST['orange_4'],
                        orange_efficiency = request.POST['orange_5'],
                        orange_made = request.POST['orange_6'],
                        orange_doc = request.POST['orange_7'],
                        orange_status = request.POST['orange_8'],
                        green_type = request.POST['green_1'],
                        green_mark = request.POST['green_2'],
                        green_designation = request.POST['green_3'],
                        green_nominal = request.POST['green_4'],
                        green_efficiency = request.POST['green_5'],
                        green_made = request.POST['green_6'],
                        green_doc = request.POST['green_7'],
                        green_status = request.POST['green_8'],
                        blue_type = request.POST['blue_1'],
                        blue_mark = request.POST['blue_2'],
                        blue_designation = request.POST['blue_3'],
                        blue_nominal = request.POST['blue_4'],
                        blue_efficiency = request.POST['blue_5'],
                        blue_made = request.POST['blue_6'],
                        blue_doc = request.POST['blue_7'],
                        blue_status = request.POST['blue_8'],
                        indigo_type = request.POST['indigo_1'],
                        indigo_mark = request.POST['indigo_2'],
                        indigo_designation = request.POST['indigo_3'],
                        indigo_nominal = request.POST['indigo_4'],
                        indigo_efficiency = request.POST['indigo_5'],
                        indigo_made = request.POST['indigo_6'],
                        indigo_doc = request.POST['indigo_7'],
                        indigo_status = request.POST['indigo_8'],
                        violet_type = request.POST['violet_1'],
                        violet_mark = request.POST['violet_2'],
                        violet_designation = request.POST['violet_3'],
                        violet_nominal = request.POST['violet_4'],
                        violet_efficiency = request.POST['violet_5'],
                        violet_made = request.POST['violet_6'],
                        violet_doc = request.POST['violet_7'],
                        violet_status = request.POST['violet_8']).save()

        return HttpResponse(
            json.dumps({
                "result": 'result',
            }),
            content_type="application/json"
        )
    else:
        return render(request, 'mobileapp/web.html')



