### Output_functions_for_GPS.py
### (71018021, 'Kuan-Ping Chang') and (83144130, 'Jonathan Navarro')
import json
import Functions_for_GPS
import urllib.parse
import urllib.request

class Directions:
    def Output(self, json):
        print('DIRECTIONS')
        for part in json['route']['legs']:
            for second_part in part['maneuvers']:
                print(second_part['narrative'])
        print()
        print()

class Distance:
    def Output(self, json):
        miles = int(json['route']['distance'])
        final_miles = round(miles)
        print('TOTAL DISTANCE: '+ str(final_miles)+ ' Miles')
        print()
        print()

class Time:
    def Output(self, json):
        print('TOTAL TIME: ', (json['route']['time'])//60, ' minutes')
        print()
        print()


class Lat_Longs:
    def Output(self, json):
        print('LATLONGS')
        for part in json['route']['locations']:
            lats = str(part['latLng']['lat'])
            if lats.startswith('-'):
                print("{:.2f} S".format(float(lats)))
            else:
                print("{:.2f} N".format(float(lats)))

            longs = str(part['latLng']['lng'])
            if longs.startswith('-'):
                print("{:.2f} W".format(float(longs)))
            else:
                print("{:.2f} E".format(float(longs)))
        print()
        print()

class Elevation:
    def __init__(self):
        self.url_base = 'http://open.mapquestapi.com/elevation/v1/profile?'

    def Output(self, response):
        latlngStr = ""
        location = []
        print('ELEVATIONS')
        for part in response['route']['locations']:
            lat = str(part['latLng']['lat'])
            lng = str(part['latLng']['lng'])
            latlngStr = lat + "," + lng 
        
        
            url = self.url_base + 'key=' + Functions_for_GPS.app_key + '&shapeFormat=raw&latLngCollection=' + latlngStr

            location.append(url)
        #print(url)
        try:
            for url in location:
                elevateUrl = urllib.request.urlopen(url)
                elevateResponse = elevateUrl.read().decode(encoding='utf-8')
                #print(elevateResponse)
            
                eleResponse = json.loads(elevateResponse)
                #print("check load")
                #print(eleResponse)
                #print(eleResponse['elevationProfile'])
                for part in eleResponse['elevationProfile']:
                    
                    print(part['height'])
            print()
            print()
            
                  
        except:
            print("Elevation Error")


def num_of_outputs():
    while True:
        try:
            num_of_outputs = int(input())
            if num_of_outputs <= 5 and num_of_outputs >=1:
                return num_of_outputs
        except:
            print("Error in parameter: Please enter the correct int(number) of requests")

def Organize_output_parameters(num_outputs):
    #add num_of_outputs out side while true parameter
    num_of_outputs = num_outputs
    param_list = []
    condition = True
    for output in range(num_of_outputs):   
        while condition == True:
            try:
                final_param = input()
                
                if final_param.upper() in "LATLONG, STEPS, TOTALTIME, TOTALDISTANCE, ELEVATION":
                    param_list.append(final_param)

                else:
                    print("The entered parameter is invalid: Please enter the correct output parameter")
                    
                #print(param_list)
                if len(param_list) == num_of_outputs:
                    condition = False
                    

            except:
                print("Error in parameters,Please Try Entering Int Again")
                
            
    return param_list        
    
def Send_final_output(parameters, json):
    for output in parameters:
        outputs = str(output.upper())
        if outputs == 'LATLONG':
            Lat_Longs.Output(1, json)
        elif outputs == 'STEPS':
            Directions.Output(1, json)
        elif outputs == 'TOTALTIME':
            Time.Output(1, json)
        elif outputs == 'TOTALDISTANCE':
            Distance.Output(1, json)
        elif outputs == 'ELEVATION':
            x = Elevation()
            Elevation.Output(x, json)
            

def copyright_():
    print()
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
            
        
        
