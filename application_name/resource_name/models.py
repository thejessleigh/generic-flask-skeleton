from sqlalchemy import Column, Text

from application_name.database import BaseModel


class ResourceModel(BaseModel):
    """A sample model
    """

    __tablename__ = "resource"
    notes = Column(Text, nullable=True)
