from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int = Field(le=3)
    title: str
    #name: str = Field(alias="_name")

    #id: int =Field(le=2)
    # @validator("id")
    # def check_that_id_is_less_than_two(cls, v):
    #     if v > 2:
    #         raise ValueError('Id не меньше двух')
    #     else:
    #         return v

##{'id': 2, 'title': 'Post 2'}