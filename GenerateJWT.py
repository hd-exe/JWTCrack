import jwt

secret = "REPLACE_WITH_JWT_SECRET"

payload = {
    "REPLACE_WITH_YOUR_DATA": "VALUE",
    "REPLACE_WITH_YOUR_DATA": VALUE
}

token = jwt.encode(payload, secret, algorithm="HS256")
print(token)
