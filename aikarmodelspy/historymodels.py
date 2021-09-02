from pydantic import BaseModel, Field


class Item(BaseModel):
    id: int
    count: int
    lag_count: int = Field(alias="lagCount")
    lag_total: int = Field(alias="lagTotal")


class ParentItem(Item):
    children: list[Item]


class History(BaseModel):
    history: dict[str, list[ParentItem]]

    class Config:
        allow_population_by_field_name = True
