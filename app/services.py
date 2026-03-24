import bcrypt


class UserService:

    # HASH

    @staticmethod
    def hash_password(password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed.decode()

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed.encode())
