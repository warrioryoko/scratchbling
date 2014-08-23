from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from models import Scratcher

class ScratcherResource(ModelResource):
    class Meta:
    	
		queryset = Scratcher.objects.filter()
		#authentication = Authentication()
		authorization = Authorization()

