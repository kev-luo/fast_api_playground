from typing import Optional
from fastapi import FastAPI, APIRouter
from models import User
from recipes_data import RECIPES

app = FastAPI(title="Recipe API", openapi_url="/openapi.json")  # app is an "instance" of the class FastAPI

api_router = APIRouter()


@api_router.get("/", status_code=200)
async def root() -> dict:
    """
    Root Get
    """
    return {"message": "Who's there?"}


@api_router.get("/recipe/{recipe_id}", status_code=200)
async def fetch_recipe(*, recipe_id: int) -> dict:
    """
    Fetch a single recipe by ID
    """
    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    if result:
        return result[0]


@api_router.get("/search/", status_code=200)
async def search_recipes(keyword: Optional[str] = None, max_results: Optional[int] = 10) -> dict:
    """
    Search for recipes based on label keyword
    """
    if not keyword:
        return {"results": RECIPES[:max_results]}

    results = filter(lambda recipe: keyword.lower() in recipe["label"].lower(), RECIPES)
    return {"results": list(results)[:max_results]}


app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8001, log_level="debug", reload=True)
