import requests

url = "https://covid-19-data.p.rapidapi.com/report/country/name"

querystring = {"date":"2020-11-19","name":"USA"}

headers = {
    'x-rapidapi-key': "0befc5f52dmsh9218de6ab72579ap14dd44jsncad545bb53ee",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)