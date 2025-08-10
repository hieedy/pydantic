from pydantic import BaseModel, Field  


class Cart(BaseModel):
    user_id: int
    items: list[str]
    quantities: dict[str, int]

class BlogPOst(BaseModel):
    title: str
    content: str
    image_url : str | None = None

