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

def compareDescription( location, newDescrip , oldReviews):
    saver = list();
    score = 1000000;
    newLat , newLong = getlatlong(location)
    for centre , old in data , oldReviews:
        temp = (centre['lat'] - newLat)**2 + (centre['lng'] - newLong)**2
        if temp < score:
            if convert(newDescrip , old) < threshold:
                score = temp
                saver.append(centre)
    with open(outFile , 'w') as file:
        json.dump(saver , file)

def getlatlong(string):
    geolocator = Nominatim(user_agent="one")
    location = geolocator.geocode(string)
    return location.latitude , location.longitude