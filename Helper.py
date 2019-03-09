import json
import numpy as np
import spacy
from geopy.geocoders import Nominatim

nlp = spacy.load('en_core_web_md')
data = json.load(open('data.json'))
threshold = 0.5 # Desimilarity Score
outFile = 'outFile.json'

def convert(newDescrip , existingReviews):
    score  = 0;
    for existing in existingReviews:
        score += np.sqrt(np.mean(np.square(nlp(existing).vector - nlp(newDescrip).vector)))
    return score

def compareDescription( location, newDescrip):
    oldReviews = getOldReviews()
    saver = list();
    score = 1000000;b
    newLat , newLong = getlatlong(location)
    for centre , old in data , oldReviews:
        temp = (centre['lat'] - newLat)**2 + (centre['lng'] - newLong)**2
        if temp < score:
            if convert(newDescrip , list(old.values()) ) < threshold:
                score = temp
                saver.append(centre)
    with open(outFile , 'w') as file:
        json.dump(saver , file)

def getLatLong(string):
    geolocator = Nominatim(user_agent="one")
    location = geolocator.geocode(string)
    return location.latitude , location.longitude

def getOldReviews()
    result = json.load(open('oldReviews.json'))
    return result