from pydantic import BaseModel

class Address(BaseModel):
    street: str 
    city: str 
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address 

class Comment(BaseModel):
    id: int
    content: str
    replies: list['Comment'] | None = None  # Using forward reference for nested comments

Comment.model_rebuild()  # Rebuild the model to handle forward references


if __name__ == "__main__":
    # Example usage
    address = Address(street="123 Main St", city="Anytown", postal_code="12345")
    user = User(id=1, name="John Doe", address=address)
    
    comment1 = Comment(id=1, content="This is a comment.")
    comment2 = Comment(id=2, content="This is a reply.", replies=[comment1, Comment(id=3, content="Another reply.")])
    
    print(user)
    print(comment2)