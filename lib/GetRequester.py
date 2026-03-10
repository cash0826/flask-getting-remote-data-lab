import requests
import json

URL = f"https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

class GetRequester:

    def __init__(self, url):
        self.url = url
        
    def get_response_body(self):
        response = requests.get(self.url) 
        # just returning response outputs the HTTP response like status code and headers, not the response body
        # use response.text to return the response body
        return response.content # Returns the response body as a JSON string

    def load_json(self):
        response_body = requests.get(self.url).json() # the json() method already parses the JSON into a Python dict/list
        return response_body
    
results = GetRequester(URL).get_response_body()
print(results)