from pydantic import BaseModel

class userPostIn(BaseModel):
    body: str

class UserPost(UserPostIn):
    id: int
