from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import CustomUser,Question,SolvedQuestions
from django.views.decorators.gzip import gzip_page
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import time
# Create your views here.

challenges = 5
eventtime = 3600

@gzip_page
def index(request):
	return render(request,'app/index.html')

@gzip_page
def about_us(request):
	return render(request,'app/aboutus.html')


@gzip_page
def rules(request):
	return render(request,'app/rules.html')

@gzip_page
def register(request):
	if request.method == 'POST':
		u = CustomUser()
		u.username = request.POST.get('username')
		u.password = make_password(request.POST.get('password'))
		u.year = request.POST.get('year')
		u.department = request.POST.get('department')
		u.college = request.POST.get('college')
		u.first_name = request.POST.get('firstname')
		u.last_name = request.POST.get('lastname')
		u.email = request.POST.get('email')
		try:
			u.clean_fields()
			u.save()
			login(request,u)
			return redirect('/challenges')
		except Exception as e:
			messages.error(request,'Invalid form!')
			return render(request,'app/register.html')
	return render(request,'app/register.html')


@gzip_page
def custom_login(request):
	if request.method == 'POST':
		username =  request.POST.get('username')
		password = request.POST.get('password')
		print(username,password)
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('/challenges')
		else:
			messages.error(request,'Invalid credentials!')

	return render(request,'app/login.html')

@gzip_page
@login_required(login_url = '/login/')
def challenges(request):
	questions = Question.objects.all().order_by('qid')
	if 'time' not in request.session:
		request.session['time'] = time.time()
	if request.method == 'POST':
		flag = request.POST.get('flag')
		qid = request.POST.get('flagid')
		question = Question.objects.get(qid=int(qid))
		solved = SolvedQuestions.objects.filter(question=question,user=request.user)
		if flag == question.flag:
			if not solved:
				solved = SolvedQuestions()
				request.user.points+=question.points
				solved.question = question
				solved.user = request.user
				question.solved+=1
				solved.save()
				messages.success(request,'Flag is correct!')
			else:
				messages.warning(request,'Already solved!')
		else:
			messages.warning(request,'Invalid flag!')
		request.user.save()
		question.save()
	return render(request,'app/untitled.html',{'questions':questions})


@gzip_page
def leaderboard(request):
	users = CustomUser.objects.exclude(username='chaitanyarahalkar').order_by('-points')[:10]
	leaderboard = list()

	for rank,user in zip(range(1,len(users)+1),users):
		leaderboard.append((rank,user))

	return render(request,'app/leaderboard.html',{'leaderboard':leaderboard})


def custom_logout(request):
	logout(request)
	return redirect('/aboutus')


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': CustomUser.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)


def timer(request):
	if request.method == 'GET':
		return HttpResponse(eventtime - int(time.time() - request.session.get('time')))

# Challenge related 

@gzip_page
def inspect(request):
	return render(request,'app/inspect.html')



@gzip_page
@csrf_exempt
def challengelogin(request):
	response = render(request,'app/chlogin.html',{'flag':'You are not admin!'})
	response.set_cookie('admin','false')
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		if request.COOKIES['admin'].lower() == 'true' and password == 'rockyou123':
			return render(request,'app/chlogin.html',{'flag':'pict_CTF{1n53cur3_c00k13}'})

	return response