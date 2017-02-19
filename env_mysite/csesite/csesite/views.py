from django.http import HttpResponse,Http404  

def hello(request):
    return HttpResponse("Hello world")

def time(request):
	import datetime
	p="The time now is %s"%datetime.datetime.now()
	return HttpResponse(p)
def timeahead(request , offset):
	import datetime
	try:
		offset=int(offset)
	except ValueError:
		raise Http404()
	
	return HttpResponse("The time in %s will be %s"%(offset ,datetime.datetime.now()+datetime.timedelta(hours=offset)))
