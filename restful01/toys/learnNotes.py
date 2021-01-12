"""
So far:
serializer = object data (a toy instance) -> dictionary like serialized data

"""
# check and understand the serializer
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
# print(toy1.pk) 
# print(toy1.name) 
# print(toy1.created) 
# print(toy1.was_included_in_home) 
# print(toy2.pk) 
# print(toy2.name) 
# print(toy2.created) 
# print(toy2.was_included_in_home)
print(type(toy1)) # <class 'toys.models.Toy'>

# then we call serializer to serialize them into a somewhat dict-like object
serializer_for_toy1 = ToySerializer(toy1) 
print(type(serializer_for_toy1)) #<class 'toys.serializers.ToySerializer'>
print(serializer_for_toy1.data) 

serializer_for_toy2 = ToySerializer(toy2) 
print(serializer_for_toy2.data)

# turn into json
json_renderer = JSONRenderer() 
toy1_rendered_into_json = json_renderer.render(serializer_for_toy1.data) 
toy2_rendered_into_json = json_renderer.render(serializer_for_toy2.data) 
print(toy1_rendered_into_json) 
print(toy2_rendered_into_json) 

###
# Now the other way around: deserialize
json_string_for_new_toy = '{"name":"Clash Royale play set","description":"6 figures from Clash Royale", "release_date":"2017-10-09T12:10:00.776594Z","toy_category":"Playset","was_included_in_home":false}' 
json_bytes_for_new_toy = bytes(json_string_for_new_toy, encoding="UTF-8") 
stream_for_new_toy = BytesIO(json_bytes_for_new_toy)
parser = JSONParser() 
parsed_new_toy = parser.parse(stream_for_new_toy) #BytesIO -> dictionary
print(type(parsed_new_toy)) # dictionary
print(parsed_new_toy) 

new_toy_serializer = ToySerializer(data=parsed_new_toy) # data must be the keyword from superclass
if new_toy_serializer.is_valid(): 
    toy3 = new_toy_serializer.save() 
    print(toy3.name)