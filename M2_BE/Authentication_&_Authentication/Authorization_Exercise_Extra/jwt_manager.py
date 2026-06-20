import jwt
from datetime import datetime, timedelta, timezone


class JWT_Manager:
    def __init__(self, private_key, public_key, algorithm):
        self.private_key = private_key
        self.public_key = public_key
        self.algorithm = algorithm

    def encode(self, data):
        try:
            payload = data.copy()
            payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=15)
            encoded = jwt.encode(payload, self.private_key, algorithm=self.algorithm)
            return encoded
        except jwt.ExpiredSignatureError:
            print("JWT ERROR: Token expired")
            return None
        except jwt.InvalidTokenError as e:
            print("JWT ERROR: Invalid token", e)
            return None
        except Exception as e:
            print("JWT ERROR:", e)
            return None


    def encode_refresh_token(self, data):
        try:
            payload = data.copy()

            payload["exp"] = datetime.now(timezone.utc) + timedelta(days=7)
            payload["type"] = "refresh"

            refresh_token = jwt.encode(
                payload,
                self.private_key,
                algorithm=self.algorithm
            )

            return refresh_token

        except Exception as e:
            print("JWT ERROR:", e)
            return None


    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.public_key, algorithms=[self.algorithm])
            return decoded
        except Exception as e:
            print("JWT ERROR:", e)
            return None

    @staticmethod
    def import_private_key_file():
        with open("private_key.pem", "r") as file:
            private_key = file.read()
            return private_key

    @staticmethod
    def import_public_key_file():
        with open("public_key.pem", "r") as file:
            public_key = file.read()
            return public_key