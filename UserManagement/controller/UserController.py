from UserManagement.util.ResponseUtil import ResponseEntity

class UserController:

    @staticmethod
    def registerUser(user = None):
        from UserManagement.repository.UserRepository import UserRepository
        responseBody = bool(UserRepository.saveUser(user))
        return ResponseEntity(body=responseBody)
