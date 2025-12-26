from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Online", "message": "Hệ thống SHIP-AI đã sẵn sàng!"}

@app.get("/chat")
def chat(msg: str):
    return {"reply": f"AI nhận lệnh: {msg}. Đang điều phối dịch vụ..."}
  
