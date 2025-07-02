from uuid import UUID
from pydantic import BaseModel


class ClusterBase(BaseModel):
    name: str
    description: str | None = None


class ClusterCreate(ClusterBase):
    pass


class Cluster(ClusterBase):
    id: UUID

    class Config:
        orm_mode = True
