import tempfile

from fastapi import FastAPI ,UploadFile , File
import Matching_function
from feature_extractor import extract_feature

app = FastAPI()


# class
# class Name(BaseModel):   --> basemodel is only for json
#     textname : str  # this should match the flutter

@app.post('/sendtoapi/')
async def get_Song(audio_file:UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".aac") as tmp:
        tmp.write(await audio_file.read())
        content = tmp.name
    query = extract_feature(content)
    match, score = Matching_function.find_closest_song(query, "/Database/database.json")
    return {
        "match": match,
        "score": round(score, 2)
    }

