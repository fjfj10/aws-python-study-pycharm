from UserManagement.config.DataBaseConfig import DataBaseConfig
import pymysql.cursors
import pandas as pd

class UserRepository:

    @staticmethod
    def saveUser(user = None):
        try:
            connection = DataBaseConfig.getConnection()
            # cursor = java의 preparedstatement, DictCursor는 cursor이 데이터를 다룰 때 dict형태로 바꿔줌
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            insert into user_tb
            values(0, %s, %s, %s, %s)
            """
            # 튜플 형태로 넣어준다
            insertcount = cursor.execute(sql, (user.username, user.password, user.name, user.email))
            # 마지막에는 commit해줘야 끝난다
            connection.commit()
            return insertcount
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def getUserAll():
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            select
                user_id as userId,
                username,
                password,
                name,
                email
            from
                user_tb
            """
            cursor.execute(sql)
            # fetchone: 첫째행만 들고옴 / fetchall: 리스트에 담아 점부 가지고 온다
            rs = cursor.fetchall()
            return rs
        except Exception as e:
            print(e)
            return None

    @staticmethod
    # def getUserByusername(username):
    #     try:
    #         connection = DataBaseConfig.getConnection()
    #         cursor = connection.cursor(pymysql.cursors.DictCursor)
    #         sql = f"""
    #         select
    #             user_id as userId,
    #             username,
    #             password,
    #             name,
    #             email
    #         from
    #             user_tb
    #         where
    #             username = "{username}"
    #         """
    #         cursor.execute(sql)
    #         rs = cursor.fetchone()
    def findUserByUsername(username = None):
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
                   select
                       user_id as userId,
                       username,
                       password,
                       name,
                       email
                   from
                       user_tb
                    where
                    username = %s
                   """
            cursor.execute(sql, username)
            # fetchone: 첫째행만 들고옴 / fetchall: 리스트에 담아 점부 가지고 온다
            rs = cursor.fetchall()
            return rs
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def updateUser(user = None):
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = f"""
            update
                user_tb
            set
                username = %s,
                password = %s,
                name = %s,
                email = %s
            where
                user_id = %s
            """
            updatecount = cursor.execute(sql, (user.username, user.password, user.name, user.email, user.userId))
            connection.commit()
            return updatecount
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def deleteUser(username):
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = f"""
            delete from user_tb
            where username = "{username}"
            """
            deletecount = cursor.execute(sql)
            connection.commit()
            return deletecount
        except Exception as e:
            print(e)
            return None



if __name__ == "__main__":
    userList = UserRepository.getUserAll()
    print(userList)

    data = {
        "userId": [1, 2, 3],
        "username": ["aaa", "bbb", "ccc"],
        "password": ["1234", "1111", "2222"],
        "name": ["aaa", "bbb", "ccc"],
        "email": ["aaa@gmail.com", "bbb@gmail.com", "ccc@gmail.com"]
    }

    # df = pd.DataFrame(data)
    # print(df.get("userId"))

    # DataFrame은 리스트를 넣어줘야 함/ Series은 값 하나만 다룰 때 사용
    # df = pd.DataFrame(userList)
    # print(df)
    print(pd.Series(userList))
    user = UserRepository.getUserByusername("aaa")
    print(user)