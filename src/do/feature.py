import uuid
from typing import Literal, Optional

from fastapi import FastAPI, HTTPException

import geoalchemy2 as ga
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy.dialects.postgresql import JSONB

class GeoJSONGeometry(SQLModel):
    """A GeoJSON geometry fragment."""

    type: Literal["Point", "LineString", "Polygon"]
    coordinates: tuple[float, float] | list[tuple[float, float]] | list[list[tuple[float, float]]]


class Feature(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    geometry: bytes = Field(
        sa_type=ga.Geometry,
        nullable=False,
    )
    properties: Optional[dict] = Field(
        default=None,
        sa_type=JSONB,
        nullable=True,
    )
    pid:Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        nullable=False,
    )


# class FeatureCreate(SQLModel):
#     geometry: GeoJSONGeometry = Field(
#         default=None,
#         sa_type=JSONB,
#         nullable=False,
#     )
#     properties: Optional[dict]


# class FeatureRead(FeatureCreate):
#     id: uuid.UUID
#     geometry: GeoJSONGeometry
#     properties: Optional[dict]