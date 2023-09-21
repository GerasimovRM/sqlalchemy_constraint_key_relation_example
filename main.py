from sqlalchemy import select

from database import get_sync_session, UsersGroups, Solution


session = get_sync_session()

# create rows
# user_group_1 = UsersGroups(user_personal_number=1, group_id=1)
# user_group_2 = UsersGroups(user_personal_number=2, group_id=1)
# sol1 = Solution(group_id=1, user_personal_number=1)
# sol2 = Solution(group_id=1, user_personal_number=1)
# sol3 = Solution(group_id=1, user_personal_number=2)
# session.add_all([user_group_1, user_group_2])
# session.add_all([sol1, sol2, sol3])
# session.commit()

# get users_groups
user_group_1_query = select(UsersGroups).where(UsersGroups.user_personal_number == 1,
                                               UsersGroups.group_id == 1)
user_group_1: UsersGroups = session.scalar(user_group_1_query)
print(user_group_1, user_group_1.solutions)

# get solutions
sols_query = select(Solution)
sols = session.scalars(sols_query).all()
print(sols)
for sol in sols:
    print(sol, sol.user_group)


session.close()
