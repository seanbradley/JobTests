import requests

results = []

states = [
"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
"HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
"MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
"NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
"SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

def get_json():
    for state in range(len(states)):
        url = "http://api.sba.gov/geodata/city_county_links_for_state_of/" + states[state] + ".json"
        r = requests.get(url)
        results.append(r.json())
    return results

get_json()
