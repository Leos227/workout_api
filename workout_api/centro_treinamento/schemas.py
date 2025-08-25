from typing import Annotated
from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchemas

class CentroTreinamentoIn(BaseSchemas):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT Selva', max_length=50)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='Rua 02 lote 01', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do centro de treinamento', example='Marcos', max_length=30)]

class CentroTreinamentoAtleta(BaseSchemas):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]