from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

class HashHelper(object):      

    @staticmethod
    def verify_password(plain_pw : str , hashed_pw : str):
        return password_hash.verify(plain_pw , hashed_pw)
    
    @staticmethod
    def get_password_hash(plain_pw : str) -> str:
        return password_hash.hash(plain_pw)

    @staticmethod
    def get_refresh_token_hash(token: str) -> str:
        return password_hash.hash(token)

    @staticmethod
    def verify_refresh_token(plain_token: str , hashed_token):
        return password_hash.verify(plain_token , hashed_token)