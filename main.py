from typing import Optional
from fastapi import FastAPI, APIRouter, Query, HTTPException
from models import Recipe, RecipeSearchResults, RecipeCreate
from recipes_data import RECIPES

app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()


# Root Get
@api_router.get("/", status_code=200)
async def root() -> dict:
    return {"message": "Who's there?"}


# Fetch a single recipe by ID
@api_router.get("/recipe/{recipe_id}", status_code=200, response_model=Recipe)
async def fetch_recipe(*, recipe_id: int) -> dict:
    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    if not result:
        raise HTTPException(status_code=404, detail=f"Recipe with ID {recipe_id} not found")
    return result[0]


# Search for recipes based on label keyword
@api_router.get("/search/", status_code=200, response_model=RecipeSearchResults)
async def search_recipes(
    *, keyword: Optional[str] = Query(None, min_length=3, example="chicken"), max_results: Optional[int] = 10
) -> dict:
    if not keyword:
        return {"results": RECIPES[:max_results]}

    results = filter(lambda recipe: keyword.lower() in recipe["label"].lower(), RECIPES)
    return {"results": list(results)[:max_results]}


@api_router.post("/recipe/", status_code=201, response_model=Recipe)
async def create_recipe(*, recipe_in: RecipeCreate) -> dict:
    new_entry_id = len(RECIPES) + 1
    recipe_entry = Recipe(
        id=new_entry_id,
        label=recipe_in.label,
        source=recipe_in.source,
        url=recipe_in.url,
    )

    RECIPES.append(recipe_entry.dict())
    return recipe_entry


app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8001, log_level="debug", reload=True)
