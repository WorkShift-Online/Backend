from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return ('👋 Привет! Это — публичный API 🕗 WorkShift Backend. Если вы '
            'видите эту надпись, значит всё ✅ работает!'
            '📚 Документация доступна по адресу: '
            'https://api.workshift.online/docs')
