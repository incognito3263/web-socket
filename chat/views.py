from django.shortcuts import render


def lobby(request):
	return render(request, 'chat/lobby.html')