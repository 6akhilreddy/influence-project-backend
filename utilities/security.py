from werkzeug.security import generate_password_hash, check_password_hash
class Security:
    def __init__(self) -> None:
        pass

    def encryptPassword(self, password):
        hashed_password = generate_password_hash(password, method='sha256')
        return hashed_password
    
    def verifyPassword(self, hashedPassword, password):
        return check_password_hash(hashedPassword, password)
