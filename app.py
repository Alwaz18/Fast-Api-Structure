from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


@app.get('/')
def index():
    return {'message': 'Hello World'}


app.get("/api/")


def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": ("Hello from a public endpoint! You don't need to be "
                "authenticated to see this.")
    }
    return result
# 2 new addition, query parameter


@api_router.get("/search/", status_code=200)  # 3
def search_recipes(
    keyword: Optional[str] = None, max_results: Optional[int] = 10  # 4 & 5
) -> dict:
    """
    Search for recipes based on label keyword
    """
    if not keyword:
        # we use Python list slicing to limit results
        # based on the max_results query parameter
        return {"results": RECIPES[:max_results]}  # 6

    results = filter(lambda recipe: keyword.lower()
                     in recipe["label"].lower(), RECIPES)  # 7
    return {"results": list(results)[:max_results]}
