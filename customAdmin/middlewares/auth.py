from django.shortcuts import render,redirect

def authMiddlware(get_response):

	def middleware(request):
		if not request.session.get('id'):
			print("middleware working")
			return redirect('login')

		return get_response(request)

	return middleware
