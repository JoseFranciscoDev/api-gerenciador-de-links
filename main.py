from fastapi import FastAPI 
from api.url_builders import build_tracked_url

app = FastAPI()

print(build_tracked_url('https://music.youtube.com/watch?v=A953td1sKS8&list=RDAMVMA953td1sKS8', {'nova query': 'nova query'}))