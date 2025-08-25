from datetime import datetime
from uuid import uuid4, UUID

from sqlalchemy import DateTime, ForeignKey, Integer, String, Float, func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from workout_api.contrib.models import BaseModel


class AtletaModel(BaseModel):
    __tablename__ = "atletas"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), unique=True, nullable=False, default=uuid4, index=True
    )

    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False, index=True)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    categoria_id: Mapped[int] = mapped_column(
        ForeignKey("categorias.pk_id"), nullable=False
    )
    categoria: Mapped["CategoriaModel"] = relationship(
        back_populates="atletas", lazy="selectin"
    )

    centro_treinamento_id: Mapped[int] = mapped_column(
        ForeignKey("centros_treinamento.pk_id"), nullable=False
    )
    centro_treinamento: Mapped["CentroTreinamentoModel"] = relationship(
        back_populates="atletas", lazy="selectin"
    )

