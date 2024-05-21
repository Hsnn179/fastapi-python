from fastapi import FastAPI, HTTPException

# Membuat instance dari FastAPI
app = FastAPI()

# Endpoint root
@app.get('/')
async def root():
    return [
        {"id": 1, "nama": "Endpoint Anime", "endpoint": "/anime"},
        {"id": 2, "nama": "Endpoint Anime Detail", "endpoint": "/anime/anime_detail"},
        {"id": 3, "nama": "Endpoint Author", "endpoint": "/author"},
        {"id": 4, "nama": "Endpoint Genre", "endpoint": "/genre"},
        {"id": 5, "nama": "Endpoint Producer", "endpoint": "/producers"},
    ]

# Data dummy untuk anime
animes = [
    {
        "id": 1, 
        "judul": "Kono Subarashii Sekai ni Shukufuku wo! 3", 
        "score": "8.52",
        "aired": "Apr 10, 2024 to ?",
        "premiered": "Spring 2024",
        "rating": "PG-13 - Teens 13 or older"
    },
    {
        "id": 2, 
        "judul": "Kimetsu no Yaiba: Hashira Geiko-hen", 
        "score": "8.30",
        "aired": "May 12, 2024 to ?",
        "premiered": "Spring 2024",
        "rating": "R - 17+ (violence & profanity)"
    },
    {
        "id": 3, 
        "judul": "Mushoku Tensei II: Isekai Ittara Honki Dasu Part 2", 
        "score": "8.36",
        "aired": "Apr 8, 2024 to ?",
        "premiered": "Spring 2024",
        "rating": "R - 17+ (violence & profanity)"
    },
]

# Endpoint untuk mendapatkan data anime
@app.get('/anime')
async def anime_data():
    # Menyederhanakan data anime agar hanya mengandung id, judul, dan score
    simplified_animes = [
        {"id": anime["id"], "judul": anime["judul"], "score": anime["score"]}
        for anime in animes
    ]
    return {
        "Message": "Berhasil mengambil data anime^^",
        "Data": simplified_animes
    }

# Endpoint untuk mendapatkan detail anime berdasarkan id
@app.get('/anime/{anime_id}')
async def anime_detail(anime_id: int):
    # Mencari anime berdasarkan id
    for anime in animes:
        if anime["id"] == anime_id:
            return {
                "Message": "Berhasil mengambil detail anime :3",
                "Data": anime
            }
    # Jika anime tidak ditemukan, mengembalikan HTTP 404
    raise HTTPException(status_code=404, detail="Anime not found T-T")

# Endpoint untuk mendapatkan data author
@app.get('/author')
async def author_data():
    # Data dummy author
    return {
        "Message": "Berhasil mengambil detail author >.<",
        "Data": [
            {"id": 1, "ditulis oleh": "Natsume Akatsuki", "diilustrasikan oleh": "Kurone Mishima"},
            {"id": 2, "ditulis dan diilustrasikan oleh": "Koyoharu Gotouge"},
            {"id": 3, "ditulis dan diilustrasikan oleh": "Rifujin na Magonote"},
        ]    
    }

# Endpoint untuk mendapatkan data genre
@app.get('/genre')
async def genre_data():
    # Data dummy genre
    return {
        "Message": "Berhasil mengambil data genre :D",
        "Data": [
            {"id": 1, "genres": "Adventure, Comedy, Fantasy"},
            {"id": 2, "genres": "Action, Fantasy"},
            {"id": 3, "genres": "Adventure, Drama, Fantasy, Ecchi"},
        ]    
    }

# Endpoint untuk mendapatkan data produser
@app.get('/producer')
async def producer_data():
    # Data dummy produser
    return {
        "Message": "Berhasil mengambil data produser :))",
        "Data": [
            {"id": 1, "produser": "Half H.P Studio, Nippon Columbia, 81 Produce, Sammy, Kadokawa"},
            {"id": 2, "produser": "Aniplex, Shueisha"},
            {"id": 3, "produser": "Frontier Works, TOHO animation, Hakuhodo DY Music & Pictures, BS11, Egg Firm, Kadokawa, GREE Entertainment"},
        ]
    }
