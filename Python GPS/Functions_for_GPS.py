#Functions_for_GPS.py
### (71018021, 'Kuan-Ping Chang') and (83144130, 'Jonathan Navarro')
import urllib.request
import urllib.parse
import json

model_URL = 'http://open.mapquestapi.com/directions/v2/route?'
app_key = urllib.parse.unquote('Fmjtd%7Cluu82161l9%2Cb5%3Do5-942au6', encoding='utf-8')
           
def grab_number_of_locations():
    while True:
         try:
             locations = int(input())
             return locations
            
         except:
             print('Error: enter only integers')
             

def input_location_parameters(location_nums: int):
    location_list = []
    for num in range(location_nums):
        location_list.append(input())
    return location_list
        
    
def organize_location_parameters(locations: list):
    organized_locations = []

    organized_locations.append(('from', locations[0]))

    for location in locations[1:]:
        organized_locations.append(('to', location))

    return organized_locations
        
    
def organize_GPS_URL(the_locations: list):
    predefined_parameters = [('key', app_key),('ambiguities','ignore')]

    for location in the_locations:
        predefined_parameters.append(location)

    return model_URL + urllib.parse.urlencode(predefined_parameters)

def request_GPS_response(gps_url: str):
    try:
        response = urllib.request.urlopen(gps_url)
        nicer_json_response = response.read().decode(encoding= 'utf-8')
        much_nicer_json_response = json.loads(nicer_json_response)
        if str(much_nicer_json_response['info']['messages']) == "['We are unable to route with the given locations.']":
            response.close()
            print(' ')
            print('NO ROUTE FOUND')
        else:
            return much_nicer_json_response
    except:
        print('MAPQUEST ERROR')
            

