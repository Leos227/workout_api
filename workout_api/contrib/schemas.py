from pydantic import UUID4, BaseModel, Field
from datetime import datetime
from typing import Annotated

class BaseSchemas(BaseModel):
    class config:
        extra =  'forbid'
        from_attributes = True

class OutMixin(BaseSchemas):
    id: Annotated[UUID4, Field(description='Identificador')]
    created_at: Annotated[datetime, Field(description='Data De Criação')]