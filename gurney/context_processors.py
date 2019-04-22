from .gurney import Gurney

def gurney(request):
	return {'gurney': Gurney(request)} 