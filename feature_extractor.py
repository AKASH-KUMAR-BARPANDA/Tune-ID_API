import librosa
import os
import numpy as np
import json
from librosa import feature # feature is not defined in init


def extract_feature(file_path , nMFCC = 20):
    waveform_amplitude , sample_rate = librosa.load(file_path,sr=22050,mono=True)
    MFCC = feature.mfcc(y=waveform_amplitude,sr=sample_rate,n_mfcc=nMFCC,)
    MFCC_mean = np.mean(MFCC.T,axis=0)
    return MFCC_mean.tolist()


def build_database(Song_folder = "Song" , Db_file = "database.json"):
    """Extract features from all songs in Song folder and save to JSON"""

    database = {}
    for file in os.listdir(Song_folder):
        if file.endswith(".aac"):
            path = os.path.join(Song_folder,file)
            feature = extract_feature(file_path = path)
            song_name = os.path.splitext(file)[0]
            database[song_name] = feature
            print(f"Processed: {song_name}")

    with open(Db_file,"w") as f:
        json.dump(database, f ,indent=4)  ## convert the dict to a json formatt f -> handler
        print(f"Song saved to {Db_file}")

if __name__ == "__main__":
    build_database(Song_folder="/Users/akashbarpanda/PycharmProjects/TuneID/Song"
                   , Db_file="/Database/database.json")