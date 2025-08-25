from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select

from workout_api.contrib.dependencias import DatabaseDependecy
from workout_api.categorias.models import CategoriaModel
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut

router = APIRouter()

@router.post(
    "/",
    summary="Criar uma nova categoria",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def create_categoria(
    db_session: DatabaseDependecy,
    categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:
    existente = await db_session.scalar(
        select(CategoriaModel).filter_by(nome=categoria_in.nome)
    )
    if existente:
        raise HTTPException(status_code=409, detail=f"Categoria '{categoria_in.nome}' já existe.")

    categoria_model = CategoriaModel(id=uuid4(), **categoria_in.model_dump())
    db_session.add(categoria_model)
    await db_session.flush()
    await db_session.commit()
    return CategoriaOut.model_validate(categoria_model, from_attributes=True)

@router.get(
    "/",
    summary="Consultar todas as categorias",
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut],
)
async def list_categorias(
    db_session: DatabaseDependecy,
) -> list[CategoriaOut]:
    categorias = (await db_session.execute(select(CategoriaModel))).scalars().all()
    return [CategoriaOut.model_validate(c, from_attributes=True) for c in categorias]

@router.get(
    "/{id}",
    summary="Consultar uma categoria pelo id",
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut,
)
async def get_categoria(
    id: UUID4,
    db_session: DatabaseDependecy,
) -> CategoriaOut:
    categoria = await db_session.scalar(select(CategoriaModel).filter_by(id=id))
    if not categoria:
        raise HTTPException(status_code=404, detail=f"Categoria não encontrada no id: {id}")
    return CategoriaOut.model_validate(categoria, from_attributes=True)
