from flask import Flask, request, render_template,url_for,redirect,flash,jsonify
import pandas as pd
import pickle
import numpy as np
import xgboost as xgb

from datetime import datetime, time

app = Flask(__name__)

def ValuePredictor(row):
    # row = np.array(row).reshape(1,32)
    # row=row.values[:,0:32]
    # for i in range(len(row)):
    #     if row[0,i] == 0:
    #         row[0,i] = 0.0000001
    # print(row)
    loaded_model = pickle.load(open("model2.pkl","rb"))
    result = loaded_model.predict(row)
    return result[0]

@app.route('/my_form_post')
def my_form():
    return render_template('ui.html')

@app.route('/', methods=['GET','POST'])
def my_form_post():
    bathrooms=0
    cleaning_fee=0
    bedrooms=0
    accommodates=0
    laundry=0
    gym=0
    elevator=0
    tv=0
    host_listings_count=0
    air_conditioning=0
    security_deposit=0
    self_check_in=0
    maximum_nights=0
    guests_included=0
    private_entrance=0
    availability_365=0
    parking=0
    host_days_active=0
    Bathroom_amenities=0
    balcony=0
    # price=0
    room_type_Entire_home=0
    room_type_Hotel_room=0
    room_type_Private_room=0
    room_type_Shared_room=0
    neighbourhood_group_cleansed_Bronx=0
    neighbourhood_group_cleansed_Brooklyn=0
    neighbourhood_group_cleansed_Manhattan=0
    neighbourhood_group_cleansed_Queens=0
    neighbourhood_group_cleansed_Staten_Island=0
    property_type_Apartment=0
    property_type_House=0
    property_type_Other=0
    cooking=0
    if request.method == 'POST':
        name = request.values.get('name')
        email = request.values.get('email')

        
        property_type = request.values.get('property')
        if property_type=='Apartment':
            property_type_Apartment=1
        elif property_type=='House':
            property_type_House=1
        else:
            property_type_Other=1
            
        borough = request.values.get('borough')
        if borough=='Brooklyn':
            neighbourhood_group_cleansed_Brooklyn=1
        elif borough=='Manhattan':
            neighbourhood_group_cleansed_Manhattan=1
        elif borough=='Bronx':
            neighbourhood_group_cleansed_Bronx=1
        elif borough=='Queens':
            neighbourhood_group_cleansed_Queens=1
        else:
            neighbourhood_group_cleansed_Staten_Island=1


        cleaning = request.values.get('cleaning')
        if cleaning=='Yes':
            cleaning_fee=50
        
        if request.values.get('listings'):
            host_listings_count = int(request.values.get('listings'))

        roomtype = request.values.get('roomtype')
        if roomtype=='Shared room':
            room_type_Shared_room=1
        elif roomtype=='Private room':
            room_type_Private_room=1
        elif roomtype=='Hotel room':
            room_type_Hotel_room=1
        else:
            room_type_Entire_home=1

        
        if request.values.get('bedrooms'):
            bedrooms = int(request.values.get('bedrooms'))
    
        
        if request.values.get('bathroom'):
            bathrooms = int(request.values.get('bathroom'))
        
        
        if request.values.get('guests'):
            guests_included = int(request.values.get('guests'))
        

        if request.values.get('deposit'):
            security_deposit = int(request.values.get('deposit'))
       
        if request.values.get('selfcheckin'):
            self_check_in = 1
        
        
        if request.values.get('privateentrance'):
            private_entrance = 1
        

        if request.values.get('laundry'):
            laundry = 1
      
        
        if request.values.get('gym'):
            gym = 1
       
        if request.values.get('television'):
            tv = 1
       
        
        if request.values.get('air'):
            air_conditioning =1
        
        
        if request.values.get('elevator'):
            elevator = 1
       
        
        if request.values.get('parking'):
            parking = 1
        
        
        if request.values.get('bath_amenities'):
            Bathroom_amenities = 1
       
        
        if request.values.get('cooking'): 
            cooking = 1
        

        row=[ bathrooms ,  cleaning_fee ,  bedrooms ,  accommodates ,  laundry , gym ,  elevator ,  tv ,  host_listings_count ,  air_conditioning , security_deposit ,  self_check_in ,  maximum_nights ,  guests_included ,  private_entrance ,  availability_365 ,  parking ,  host_days_active ,  Bathroom_amenities ,  balcony ,  room_type_Entire_home ,  room_type_Hotel_room ,  room_type_Private_room ,  room_type_Shared_room ,  neighbourhood_group_cleansed_Bronx ,  neighbourhood_group_cleansed_Brooklyn ,  neighbourhood_group_cleansed_Manhattan ,  neighbourhood_group_cleansed_Queens ,  neighbourhood_group_cleansed_Staten_Island ,  property_type_Apartment ,  property_type_House ,  property_type_Other ]
        df = pd.DataFrame(row).T
        
        df.columns=['bathrooms', 'cleaning_fee', 'bedrooms', 'accommodates', 'Laundry', 'gym', 'elevator', 'tv', 'host_listings_count', 'air_conditioning', 'security_deposit', 'self_check_in', 'maximum_nights', 'guests_included', 'private_entrance', 'availability_365', 'parking', 'host_days_active', 'Bathroom_amenities', 'balcony', 'room_type_Entire home/apt', 'room_type_Hotel room', 'room_type_Private room', 'room_type_Shared room', 'neighbourhood_group_cleansed_Bronx', 'neighbourhood_group_cleansed_Brooklyn', 'neighbourhood_group_cleansed_Manhattan', 'neighbourhood_group_cleansed_Queens', 'neighbourhood_group_cleansed_Staten Island', 'property_type_Apartment', 'property_type_House', 'property_type_Other']
        result = ValuePredictor(df)
        answer = str(round(result, 2))
        answer = '' + '$' + answer + '/-'
        return render_template('ui.html',data = answer)
    else:
        return render_template('ui.html')
     
if __name__=="__main__":
    app.run(debug=True)