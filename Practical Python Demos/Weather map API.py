


api_key = "67db99899ef5e794ec449dc8e81883ff"
city = "Covington"
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+""

requests = requests.get(url)
json = requests.json()

print(json)