from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return ('👋 Привет! Это — публичный API проекта 🕗 WorkShift. '
            '📚 Документация доступна здесь: '
            'https://api.workshift.online/docs')
