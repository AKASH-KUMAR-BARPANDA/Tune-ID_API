# 🎶 Tune-ID API  

A lightweight **music recognition system** built with **FastAPI** that identifies the closest matching song from an uploaded audio file. The system extracts **MFCC features** using [Librosa](https://librosa.org/), stores them in a JSON database, and compares query songs with cosine similarity.  

##🔗 **Repo Link:**

     [Tune-ID_API](https://github.com/AKASH-KUMAR-BARPANDA/Tune-ID_API.git)  

---

## 🚀 Features  

    - Upload audio files via API (`.aac` supported).  
    - Extracts **MFCC features** for song fingerprinting.  
    - Matches songs using **cosine similarity**.  
    - Maintains a **JSON-based database** for fast lookups.  

---
---

## ⚙️ Setup & Installation  

1. Clone the repo:  
   ```bash
   git clone https://github.com/AKASH-KUMAR-BARPANDA/Tune-ID_API.git
   cd Tune-ID_API

2. Add your songs to the Song/ folder (must be .aac).
3. Build the feature database:
    ```bash
      python feature_extractor.py
5. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload

📡 API Endpoint

  ## POST /sendtoapi/
  
Upload an audio file and get the closest match.

  Request:
    
    curl -X POST "http://127.0.0.1:8000/sendtoapi/" \
       -F "audio_file=@Song/Heer Haider Ali.aac"
  
  Response:
  
    {
      "match": "Heer Haider Ali",
      "score": 0.92
    }
---------------
📌 Notes

	•	Add songs in the Song/ folder before building the database.
	•	Database (database.json) will be regenerated every time you run the builder.
	•	Currently supports .aac audio format.

⸻

🛠️ Tech Stack

	•	FastAPI – API Framework
	•	Librosa – Audio Feature Extraction
	•	NumPy – Math & Similarity Calculations
	•	JSON – Lightweight Database


  
