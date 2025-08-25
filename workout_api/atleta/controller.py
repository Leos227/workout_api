from uuid import uuid4
from datetime import datetime, timezone

from fastapi import APIRouter, Body, HTTPException, status, Response
from pydantic import UUID4
from sqlalchemy import select

from workout_api.contrib.dependencias import DatabaseDependecy
from workout_api.atleta.schema import AtletaIn, AtletaOut, AtletaUpdate
from workout_api.atleta.models import AtletaModel
from workout_api.categorias.models import CategoriaModel
from workout_api.centro_treinamento.models import CentroTreinamentoModel

router = APIRouter()

@router.post(
    "/",
    summary="Criar novo atleta",
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut,
)
async def create_atleta(
    db_session: DatabaseDependecy,
    atleta_in: AtletaIn = Body(...)
) -> AtletaOut:
    categoria_nome = atleta_in.categoria.nome
    ct_nome = atleta_in.centro_treinamento.nome

    categoria = (await db_session.execute(
        select(CategoriaModel).filter_by(nome=categoria_nome)
    )).scalars().first()
    if not categoria:
        raise HTTPException(status_code=400, detail=f"A categoria '{categoria_nome}' não foi encontrada.")

    centro = (await db_session.execute(
        select(CentroTreinamentoModel).filter_by(nome=ct_nome)
    )).scalars().first()
    if not centro:
        raise HTTPException(status_code=400, detail=f"O centro de treinamento '{ct_nome}' não foi encontrado.")

    try:
        atleta_model = AtletaModel(
            id=uuid4(),
            created_at=datetime.now(timezone.utc),
            **atleta_in.model_dump(exclude={"categoria", "centro_treinamento"}),
            categoria_id=categoria.pk_id,
            centro_treinamento_id=centro.pk_id,
        )
        db_session.add(atleta_model)
        await db_session.flush()
        await db_session.commit()
        return AtletaOut(
            id=atleta_model.id,
            created_at=atleta_model.created_at,
            **atleta_in.model_dump()
        )
    except Exception as e:
        await db_session.rollback()
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro ao inserir os dados no banco: {e.__class__.__name__}")

@router.get(
    "/",
    summary="Consultar todos os atletas",
    status_code=status.HTTP_200_OK,
    response_model=list[AtletaOut],
)
async def list_atletas(
    db_session: DatabaseDependecy,
) -> list[AtletaOut]:
    atletas = (await db_session.execute(select(AtletaModel))).scalars().all()
    return [AtletaOut.model_validate(a, from_attributes=True) for a in atletas]

@router.get(
    "/{id}",
    summary="Consultar um atleta pelo id",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def get_atleta(
    id: UUID4,
    db_session: DatabaseDependecy,
) -> AtletaOut:
    atleta = (await db_session.execute(
        select(AtletaModel).filter_by(id=id)
    )).scalars().first()
    if not atleta:
        raise HTTPException(status_code=404, detail=f"Atleta não encontrado no id: {id}")
    return AtletaOut.model_validate(atleta, from_attributes=True)

@router.patch(
    "/{id}",
    summary="Editar um atleta pelo id",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def update_atleta(
    id: UUID4,
    db_session: DatabaseDependecy,
    atleta_up: AtletaUpdate = Body(...)
) -> AtletaOut:
    atleta = (await db_session.execute(
        select(AtletaModel).filter_by(id=id)
    )).scalars().first()
    if not atleta:
        raise HTTPException(status_code=404, detail=f"Atleta não encontrado no id: {id}")

    data = atleta_up.model_dump(exclude_unset=True)
    for k, v in data.items():
        setattr(atleta, k, v)

    await db_session.commit()
    await db_session.refresh(atleta)
    return AtletaOut.model_validate(atleta, from_attributes=True)

@router.delete(
    "/{id}",
    summary="Deletar um atleta pelo id",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_atleta(
    id: UUID4,
    db_session: DatabaseDependecy,
) -> Response:
    atleta = (await db_session.execute(
        select(AtletaModel).filter_by(id=id)
    )).scalars().first()
    if not atleta:
        raise HTTPException(status_code=404, detail=f"Atleta não encontrado no id: {id}")

    await db_session.delete(atleta)
    await db_session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
