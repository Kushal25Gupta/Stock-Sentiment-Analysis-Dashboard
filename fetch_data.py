import requests

# This article returns some basis information about GITHUB in JSON format 
url = "https://api.github.com"

# making a GET request from the url
response = requests.get(url)

# convert the repsonse to JSON format
data = response.json()

# print the data
print("Data fectched from GITHUB API:")
print(data)