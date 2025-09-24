import numpy as np
import json
from feature_extractor import extract_feature


def cosine_similarity(vec1,vec2):
    return np.dot(vec1,vec2)/(np.linalg.norm(vec1) * np.linalg.norm(vec2))

def find_closest_song(query_song_feature,db_file = "Database/database.json"):
    with open(db_file,"r") as f:
        data_song = json.load(f)

    best_match = None
    best_score = -1

    for song_name,features in data_song.items():
        score = cosine_similarity(query_song_feature,features)
        if score > best_score:
            best_score = score
            best_match = song_name
    return best_match , best_score


if __name__ == "__main__":
    query = extract_feature("/Song/Heer Haider Ali.aac")  # input song
    match, score = find_closest_song(query, "/Database/database.json")
    print(f"Closest match: {match} (Score: {score:.2f})")
