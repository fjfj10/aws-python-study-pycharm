class UserInfo:

    # cls변수(클래스변수 == static변수) = 생성자가 없으면 그냥 static
    adminUser = {
        "username": "root",
        "password": "1q2w3e4r"
    }

    def __init__(self):
        # 생성된 객체의 변수가 생김
        self.adminUser = {
            "username": "user1",
            "password": "1234"
        }

    @classmethod
    def showAdminUser(cls):
        print("[showAdminUser]")
        print(cls.adminUser)


class User:

    # 멤버변수의 초기값을 init에다 정의
    def __init__(self):
        self.username = None
        self.password = None
        self.name = None
        self.email = None

    @staticmethod
    def showUserClassInfo():
        print("그냥 실행할 수 있는 메소드 -> 아무데도 접근 할 수 없음: 싱글톤 만들 때 사용")


if __name__ == "__main__":
    userInfo = UserInfo()
    print(userInfo.adminUser)
    print(UserInfo.adminUser)

    # 생성자에서 넣어준 값으로 가져온다
    # @classmethod를 사용하면 cls변수를 가져온다
    userInfo.showAdminUser()
    # showAdminUser는 멤버 메소드 생성 해야지만 사용가능
    # @classmethod를 사용하면 생성하지 않아도 사용가능
    UserInfo.showAdminUser()

    User.showUserClassInfo()