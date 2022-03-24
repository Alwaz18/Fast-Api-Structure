from fastapi import FastAPI
from starlette.responses import HTMLResponse
# import locale files
from models import models
from database.configuration import engine
# import router files
from core import order, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SecureAPI",
    description="Hello thank you for reading my Blog UwU",
    version="1.0.0",)

app.include_router(order.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/", response_class=HTMLResponse)
def index():
    return """
<!Doctype html>
    <html>
        <body>
            <h1>SecureAPI</h1>
            <div class="btn-group">
                <a href="/docs"><button>SwaggerUI</button></a>
                <a href="/redoc"><button>Redoc</button></a>
            </div>
        </body>
    </html>"""
