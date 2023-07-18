import requests
from dotenv import dotenv_values

# Load the environment variables from .env file
config = dotenv_values(".env")
api_key = config.get("API_KEY")

headersList = {
    "Authorization": api_key
}


def Request(url, payload):
    """Make a GET request to the specified URL with the given payload.

    Args:
        url (str): The URL to make the request to.
        payload (dict): The payload to include in the request.

    Returns:
        requests.Response: The response object containing the response from the server.

    """
    return requests.request("GET", url, data=payload, headers=headersList)
