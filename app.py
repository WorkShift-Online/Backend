from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return ('👋 Привет! Это — публичный API 🕗 WorkShift Backend. '
            '📚 Документация доступна по адресу: '
            'https://api.workshift.online/docs')
