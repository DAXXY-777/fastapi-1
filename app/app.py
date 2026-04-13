from fastapi.openapi.utils import status_code_ranges
from fastapi import FastAPI,HTTPException

app=FastAPI()

text_post = {
    1: {"title": "New post", "content": "cooltestpost"},
    2: {"title": "Morning Thoughts", "content": "Sunrise was beautiful today"},
    3: {"title": "Tech Update", "content": "Trying out a new Python library"},
    4: {"title": "Workout Log", "content": "Completed a 5km run"},
    5: {"title": "Food Diary", "content": "Had pasta for lunch"},
    6: {"title": "Movie Review", "content": "Watched a sci-fi thriller"},
    7: {"title": "Travel Plans", "content": "Planning a trip to the mountains"},
    8: {"title": "Daily Journal", "content": "Learned something new today"},
    9: {"title": "Coding Notes", "content": "Practiced recursion problems"},
    10: {"title": "Random Idea", "content": "Build a simple game app"},
    11: {"title": "Music Vibes", "content": "Listening to chill beats"},
    12: {"title": "Book Notes", "content": "Reading a mystery novel"},
    13: {"title": "Evening Reflection", "content": "Productive and calm day"}
}


@app.get("/content/{id}")
def get_id_post(id:int):
    if id not in text_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_post.get(id)
