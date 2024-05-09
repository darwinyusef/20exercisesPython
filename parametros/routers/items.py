from typing import Annotated
from fastapi import APIRouter, Query
from pydantic import BaseModel, HttpUrl

descript = []


class EventInfo(BaseModel):
    name: str
    description: Annotated[str | None, Query(max_length=30)] = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ],
            "normal": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={
        404: {"description": "Items router Not found"},
    },
)


@router.get("/{item_id}")
def read_item(item_id: int, q: str | None = None):
    if (len(descript) > 0):
        return {"item_id": item_id, "q": q, "descript": descript}
    else:
        return {"item_id": item_id, "q": q}


@router.post("/")
def chargue_item(item: EventInfo):
    descript.append(item)
    return descript


@router.put("/{item_id}")
async def update_item(item_id: int, item: EventInfo):
    results = {"item_id": item_id, "item": item}
    return results


@router.patch("/{item_id}")
def chargue_item(item_id: int, item: EventInfo):
    return {"id": item_id, "item": item}


@router.delete("/{item_id}")
def chargue_item(item_id: int):
    return item_id
