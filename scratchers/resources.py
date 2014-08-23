from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from models import Scratcher

class ScratcherResource(ModelResource):
    class Meta:
    	
		queryset = Scratcher.objects.filter()
		authentication = ApiKeyAuthentication()
		authorization = DjangoAuthorization()

