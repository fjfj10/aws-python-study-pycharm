import pandas as pd
from UserManagement.controller.UserController import UserController
from UserManagement.entity.User import User

class UserView:

    @staticmethod
    def register():
        # 클래스 위에 from을 하면 모듈을 불러올 때마다 User과 UserController를 가지고 온다
        # register가 아닌 다른 함수에서 User과 UserController를 사용하지 않는다면 무쓸모하게 가지고 오게 되는것
        # 하지만 올려도된다 불필요할 뿐 안되는거 아님
        # 상대 경로는 안쓰는게 좋다 -> 최상위 패키지에서 시작
        print("[ 사용자 등록 화면 ]")
        username = input("사용자이름 >>> ")
        password = input("비밀번호 >>> ")
        name = input("이름 >>> ")
        email = input("이메일 >>> ")

        response = UserController.registerUser(User(
            username=username,
            password=password,
            name=name,
            email=email
        ))

        if not response.__dict__.get("body"):
            print("데이터를 추가하는 중 오류가 발생했습니다.")
            print("다시 시도해주세요.")


    @staticmethod
    def showAllUser():
        # userList = UserController.getUserListAll()
        response = UserController.getUserListAll()
        print("[ 전체 사용자 조회 ]")
        if bool(response.body):
            print(pd.DataFrame(response.body))
        else:
            print("조회할 데이터가 없습니다.")
        # print("[전체 사용자 리스트]")
        # print(pd.DataFrame(userList))


    @staticmethod
    # def getUserByUsername():
    #     from UserManagement.controller.UserController import UserController
    #     print("[사용자 검색]")
    #     username = input("사용자이름 >>> ")
    #     response = UserController.getUserByusername(username)
    #     print("[사용자 정보]")
    #     print(pd.Series(response))
    def showFindUser():
        print("[ username으로 사용자 정보 검색 ]")
        username = input("검색하실 사용자이름을 입력하세요 >>> ")
        response = UserController.getUser(username)
        if bool(response.body):
            print(pd.Series(response.body))
        else:
            print("조회할 데이터가 없습니다.")

    @staticmethod
    # def modify():
    #     from UserManagement.entity.User import User
    #     from UserManagement.controller.UserController import UserController
    #     print("[사용자 정보 변경]")
    #     userId = input("사용자 Id >>>")
    #     username = input("사용자이름 >>> ")
    #     password = input("비밀번호 >>> ")
    #     name = input("이름 >>> ")
    #     email = input("이메일 >>> ")
    #     response = UserController.modifyUser(User(
    #         userId=userId,
    #         username=username,
    #         password=password,
    #         name=name,
    #         email=email
    #     ))
    def updateUser():
        print("[ 사용자 정보 수정 ]")
        response = UserController.getUserListAll()
        if not bool(response.body):
            print("수정할 정보가 없습니다")
            return
        df = pd.DataFrame(response.body)
        print(df)
        userId = input("수정하실 userId를 입력하세요 >>> ")
        index = df.index[df["userId"] == int(userId)].values[0]
        user = UserView.showUpdateMenu(response.body[index])
        if not bool(user):
            print("수정을 취소했습니다.")
            return
        response = UserController.updateUser(user)
        if(bool(response.body)):
            print("======== << 수정 완료 >> ========")

    @staticmethod
    def showUpdateMenu(oldUser):
        newUser = oldUser.copy()

        while True:
            print("-" * 50)
            df = pd.DataFrame([oldUser, newUser], index=["수정 전", "수정 후"])
            print(df)
            print("-" * 50)
            print("1. password 수정")
            print("2. name 수정")
            print("3. email 수정")
            print("s. 저장")
            print("c. 취소")
            print("-" * 50)
            select = input("메뉴 선택 >>> ")

            if select == "c":
                return None
            elif select == "s":
                return newUser
            elif select == "1":
                password = input("비밀번호 입력 >>> ")

                if not UserView.isValid(oldUser.get("password"), password):
                    continue

                checkPassword = input("비밀번호 입력 확인 >>> ")

                if checkPassword != password:
                    print("비밀번호가 일치하지 않습니다.")
                    continue

                newUser["password"] = password

            elif select == "2":
                name = input("이름 입력 >>> ")

                if not UserView.isValid(oldUser.get("name"), name):
                    continue

                newUser["name"] = name
            elif select == "3":
                email = input("이메일 입력 >>> ")

                if not UserView.isValid(oldUser.get("email"), email):
                    continue

                newUser["email"] = email
            else:
                print("선택하신 번호는등록되지 않은 메뉴입니다.")

        return None


    @staticmethod
    def isValid(oldValue, value):
        if not bool(value):
            print("공백일 수 없습니다.")
            return False
        elif oldValue == value:
            print("기존 정보와 동일합니다.")
            return False

        return True


    @staticmethod
    def deleteUser():
        print("*"* 50)
        print("[ 사용자 삭제 ]")
        username = input("삭제할 사용자의 username을 입력해주세요 >>> ")
        response = UserController.getUser(username)
        if bool(response.body):
            print(pd.Series(response.body))
        else:
            print("존재하지 않는 사용자입니다.")
            return

        doublecheck = input("정말로 삭제하시겠습니까? [y / n]")

        if doublecheck == "n":
            print("사용자 삭제를 취소합니다.")
        elif doublecheck == "y":
            response = UserController.deleteUser(username)
            if (bool(response.body)):
                print("======== << 삭제 완료 >> ========")
