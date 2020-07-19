from django.shortcuts import render,redirect

def loginCheck(get_response):

	def middleware(request):
		if not request.session.get('id'):
			return redirect('login')

		return get_response(request)

	return middleware

def logoutCheck(get_response):

	def middleware(request):
		if request.session.get('id'):
			return redirect('dashboard')

		return get_response(request)

	return middleware
