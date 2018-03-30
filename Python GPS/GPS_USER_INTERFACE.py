###GPS_USER_INTERFACE
### (71018021, 'Kuan-Ping Chang') and (83144130, 'Jonathan Navarro')
from Functions_for_GPS import *
from Output_functions_for_GPS import *

def ourNames() -> ((int, str)):
    return((71018021, 'Kuan-Ping Chang'),(83144130, 'Jonathan Navarro') )

def GPS_user_interface():
    locations = organize_location_parameters(input_location_parameters(grab_number_of_locations()))
    main_response = request_GPS_response(organize_GPS_URL(locations))
    #change here: add request = num_of_outputs()
    request = num_of_outputs()
    #change here: add request to Organize_output_parameters
    Final = Send_final_output(Organize_output_parameters(request), main_response)
    return Final

if __name__ == '__main__':
    GPS_user_interface()
    copyright_()
    
    
    
    
