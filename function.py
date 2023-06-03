import requests

headersList = {
 "TRN-Api-Key": "fdd815c4-da63-458d-8822-05d7e028dd2b" 
}

def Request(url, payload):
    return requests.request("GET", url, data=payload,  headers=headersList)