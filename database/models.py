# coding: utf-8
from sqlalchemy import (
    Column,
    DECIMAL,
    ForeignKey,
    Integer,
    String,
    TIMESTAMP,
    Table,
    text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    password = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(
        TIMESTAMP,
        server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
    )


class Progress(Base):
    __tablename__ = 'progress'

    id = Column(Integer, primary_key=True)
    page = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(
        TIMESTAMP,
        server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
    )
    user_id = Column(ForeignKey('users.id', ondelete='RESTRICT'))

    user = relationship('User')
