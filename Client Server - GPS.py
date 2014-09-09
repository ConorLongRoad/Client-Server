import urllib.parse,urllib.request, json

def address_to_gps(address): 
     parameters = {'address': address,'sensor': 'false' } 
     parameters = urllib.parse.urlencode(parameters) 
     url = "http://maps.googleapis.com/maps/api/geocode/json?" 
     url = url + parameters 
     rawreply = urllib.request.urlopen(url).read() 
     reply = json.loads(rawreply.decode("utf-8")) 
     gps = reply['results'][0]['geometry']['location'] 
     return gps
    
print(address_to_gps("Long Road, Cambridge, UK")) 