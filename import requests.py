import requests

url = "https://api.themoviedb.org/3/movie/119?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNmIxYjg2MTE4YzhiMzk4ZjcwNDQ1MDZmNWM0NmFjOSIsInN1YiI6IjY1NWI3YzYyZWE4NGM3MTA5NmUwMDRkZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.5cDYIo0Q-rPC5hqU3BfJcvAOyhHe17AnEbbZDI7LO6E"
}

response = requests.get(url, headers=headers)

print(response.text)