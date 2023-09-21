from enum import IntEnum

from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from database.base_meta import BaseSQLAlchemyModel


class UsersGroups(BaseSQLAlchemyModel):
    __tablename__ = "dbo_users_groups"

    user_personal_number = Column(Integer, primary_key=True)
    group_id = Column(Integer, primary_key=True)

    solutions = relationship("Solution", back_populates="user_group")




