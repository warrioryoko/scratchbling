from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from models import Scratcher
from tastypie import fields

class ScratcherResource(ModelResource):
    item_cost = fields.DecimalField(attribute = 'item_cost')
    
    class Meta:
    	
		queryset = Scratcher.objects.filter()
		#authentication = Authentication()
		authorization = Authorization()

