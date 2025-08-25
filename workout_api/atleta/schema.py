from typing import Annotated, Literal, Optional
from pydantic import Field, PositiveFloat, PositiveInt, StringConstraints

from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.contrib.schemas import BaseSchemas, OutMixin

CPFStr = Annotated[str, StringConstraints(pattern=r'^\d{11}$', min_length=11, max_length=11)]

class AtletaBase(BaseSchemas):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[CPFStr, Field(description='CPF do atleta (11 dígitos, só números)', example='12345678900')]
    idade: Annotated[PositiveInt, Field(description='Idade do atleta', example=25, le=120)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta (kg)', example=75.5, le=500)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta (m)', example=1.70, gt=0.5, lt=3.0)]
    sexo: Annotated[Literal['M', 'F', 'O'], Field(description='Sexo do atleta (M/F/O)', example='M')]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]

class AtletaIn(AtletaBase):
    pass

class AtletaOut(OutMixin, AtletaIn):
    pass

class AtletaUpdate(BaseSchemas):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Joao', max_length=50)]
    idade: Annotated[Optional[PositiveInt], Field(None, description='Idade do atleta', example=25, le=120)]