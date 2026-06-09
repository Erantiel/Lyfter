import jwt


class JWT_Manager:
    def __init__(self, private_key, public_key, algorithm):
        self.private_key = private_key
        self.public_key = public_key
        self.algorithm = algorithm

    def encode(self, data):
        try:
            encoded = jwt.encode(data, self.private_key, algorithm=self.algorithm)
            return encoded
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

    def import_private_key_file():
        with open("private_key.pem", "r") as file:
            private_key = file.read()
            return private_key

    def import_public_key_file():
        with open("public_key.pem", "r") as file:
            public_key = file.read()
            return public_key