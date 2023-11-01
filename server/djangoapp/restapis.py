import requests
import json
from .models import CarDealer
from requests.auth import HTTPBasicAuth

# Function to perform a GET request
def get_request(url, **kwargs):
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs)
        response.raise_for_status()  # Raise an exception for HTTP errors
        json_data = response.json()
        return json_data
    except requests.exceptions.RequestException as e:
        # If any error occurs
        print(f"Network exception occurred: {e}")
        return None

# Function to retrieve dealers from a cloud function



def get_dealers_from_cf(url, **kwargs):
    results = []
    json_result = get_request(url)
    
    if json_result:
        for dealer_doc in json_result:
            # Create a CarDealer object with values from the dealer_doc
            dealer_obj = CarDealer(
                address=dealer_doc["address"],
                city=dealer_doc["city"],
                full_name=dealer_doc["full_name"],
                id=dealer_doc["id"],
                lat=dealer_doc["lat"],
                long=dealer_doc["long"],
                short_name=dealer_doc["short_name"],
                state=dealer_doc["state"],
                zip=dealer_doc["zip"],
                st=dealer_doc["st"]
            )
            results.append(dealer_obj)

    return results



# Function to get reviews by dealer ID from a cloud function
def get_dealer_by_id_from_cf(url, dealerId):
    # Implement the logic to retrieve reviews for a dealer by ID from the cloud function
    pass

# Function to analyze review sentiments using Watson NLU
def analyze_review_sentiments(text):
    # Implement the logic to analyze review sentiments using Watson NLU
    pass
