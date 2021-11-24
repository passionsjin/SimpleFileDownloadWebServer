import uvicorn
from fastapi import FastAPI
from starlette.responses import FileResponse


def create_app() -> FastAPI:
    app = FastAPI()
    return app


app = create_app()


@app.get("/asdfngeinwadsmkagoj")
async def home():
    """Home page
    """
    return FileResponse('class_video.zip', media_type='application/octet-stream', filename='class_video.zip')


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=45876)