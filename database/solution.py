from datetime import datetime
from enum import IntEnum, Enum as BaseEnum

from sqlalchemy import Column, Integer, String, Float, ForeignKeyConstraint, Boolean, Enum, \
    DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship

from database.base_meta import BaseSQLAlchemyModel


class Solution(BaseSQLAlchemyModel):
    __tablename__ = "dbo_solution"
    __table_args__ = (
        ForeignKeyConstraint(['user_personal_number', 'group_id'],
                             ['dbo_users_groups.user_personal_number', 'dbo_users_groups.group_id'],
                             name='dbo_users_groups_fkey'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    # group_id = Column(ForeignKey("dbo_users_groups.group_id"))
    # user_personal_number = Column(ForeignKey("dbo_users_groups.user_personal_number"))
    group_id = Column(Integer, nullable=False)
    user_personal_number = Column(Integer, nullable=False)

    user_group = relationship("UsersGroups", back_populates='solutions')

