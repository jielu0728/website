#coding:utf-8
from django.shortcuts import render
from app.models import Marques

def home(request):
	page = 'home'
	return render(request, 'index.html', {'page':page})

def marques(request):
	page = 'marques'
	current_url = request.get_full_path()
	url = current_url.rsplit('/',1)[-1]
	if url == '':
		n = 0
	else:
		n = int(current_url.rsplit('/',1)[-1])-1
	marques_all = Marques.objects.all()
	if n*10 > len(marques_all):
		marques = marques_all[n*10:]
	else:
		marques = marques_all[n*10:(n+1)*10]
	total = len(marques_all)/10+1 if len(marques_all)%10 != 0 else len(marques_all)/10
	marques = [marques[:5],marques[5:len(marques)]] if len(marques)>=5 else [marques[:len(marques)],[]]
	return render(request, 'marques.html', {'page':page, 'marques':marques, 'total':range(2,total+1)})

def contact(request):
	page = 'contact'
	return render(request, 'contact.html', {'page':page})

def externalisation(request):
	page = 'externalisation'
	return render(request, 'externalisation.html', {'page':page})

def nosforces(request):
	page = 'nosforces'
	return render(request, 'nosforces.html', {'page':page})

def quisommesnous(request):
	page = 'quisommesnous'
	return render(request, 'quisommesnous.html', {'page':page})

def vouscherchez(request):
	page = 'vouscherchez'
	return render(request, 'vouscherchez.html', {'page':page})