from UserManagement.util.ResponseUtil import ResponseEntity
from UserManagement.repository.UserRepository import UserRepository

class UserController:

    @staticmethod
    def registerUser(user = None):
        responseBody = bool(UserRepository.saveUser(user))
        return ResponseEntity(body=responseBody)

    @staticmethod
    def getUserListAll():
        # userList = UserRepository.getUserAll()
        # return userList
        responseBody = UserRepository.getUserAll()
        return ResponseEntity(body=responseBody)

    @staticmethod
    # def getUserByusername(username):
    #     from UserManagement.repository.UserRepository import UserRepository
    #     userInfo = UserRepository.getUserByusername(username)
    #     return userInfo
    def getUser(username=None):
        responseBody = UserRepository.findUserByUsername(username)
        return ResponseEntity(body=responseBody)

    @staticmethod
    def modifyUser(user = None):
        from UserManagement.repository.UserRepository import UserRepository
        responseBody = bool(UserRepository.updateUser(user))
        return ResponseEntity(body=responseBody)

    @staticmethod
    def deleteUser(username):
        from UserManagement.repository.UserRepository import UserRepository
        user = UserRepository.deleteUser(username)