import requests
from datetime import datetime

USERNAME = "kdenev"
TOKEN = "" # <- insert token here 

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN
    , "username": USERNAME
    , "agreeTermsofService": "yes"
    , "notMinor": "yes"
}

# Set up a user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1"
    , "name": "reading"
    , "unit": "Pages"
    , "type": "int"
    , "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# Create a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Add a pixel to the graph
today = datetime(2024,1,12)
addpixel_endpoint = graph_endpoint + "/graph1"
addpixel_config = {
    "date": today.strftime("%Y%m%d")
    , "quantity": "50"
}

# Add a pixel to the graph
# response = requests.post(url=addpixel_endpoint, json=addpixel_config, headers=headers)
# print(response.text)


# Update pixel
updatepixel_endpoint = addpixel_endpoint + f"/{today.strftime('%Y%m%d')}"
updatepixel_config = {
    "quantity": "1"
}

# response = requests.put(url=updatepixel_endpoint, json=updatepixel_config, headers=headers)
# print(response.text)

delete_endpoint = addpixel_endpoint + f"/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
