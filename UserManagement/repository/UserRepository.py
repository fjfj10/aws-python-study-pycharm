from UserManagement.config.DataBaseConfig import DataBaseConfig
import pymysql.cursors

class UserRepository:

    @staticmethod
    def saveUser(user = None):
        connection = DataBaseConfig.getConnection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = f"""
insert into user_tb
values(0, %s, %s, %s, %s)
"""
        # 튜플 형태로 넣어준다
        insertcount = cursor.execute(sql, (user.username, user.password, user.name, user.email))
        # 마지막에는 commit해줘야 끝난다
        connection.commit()
        return insertcount