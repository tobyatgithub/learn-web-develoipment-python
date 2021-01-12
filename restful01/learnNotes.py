# check the serializer
from datetime import datetime 
from django.utils import timezone 
from six import BytesIO 
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser 
from toys.models import Toy 
from toys.serializers import ToySerializer 

toy_release_date = timezone.make_aware(datetime.now(), timezone.get_current_timezone()) 
toy1 = Toy(
    name='Snoopy talking action figure', 
    description='Snoopy speaks five languages', 
    release_date=toy_release_date, 
    toy_category='Action figures', 
    was_included_in_home=False) 
toy1.save() 
toy2 = Toy(
    name='Hawaiian Barbie', 
    description='Barbie loves Hawaii', 
    release_date=toy_release_date, 
    toy_category='Dolls',
     was_included_in_home=True) 
toy2.save()

# right now toy1 and toy2 are toy objects
print(type(toy1))
# print(toy1.pk) 
# print(toy1.name) 
# print(toy1.created) 
# print(toy1.was_included_in_home) 
# print(toy2.pk) 
# print(toy2.name) 
# print(toy2.created) 
# print(toy2.was_included_in_home)

# then we call serializer to serialize them
serializer_for_toy1 = ToySerializer(toy1) 
print(type(serializer_for_toy1))
print(serializer_for_toy1.data) 