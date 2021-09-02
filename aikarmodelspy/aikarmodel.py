from pydantic import BaseModel, Field


class AikarObject(BaseModel):
    cls: int = Field(alias=":cls")

    class Config:
        allow_population_by_field_name = True
