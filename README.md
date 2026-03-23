JWTCrack.py

Brute-force a JWT secret using a wordlist.

python JWTCrack.py -t <JWT_TOKEN> -w <WORDLIST>

Options:
-t, --token → JWT token to crack (required)
-w, --wordlist → Path to wordlist (required)
-a, --algorithm → JWT algorithm (HS256, HS384, HS512)
-v, --verbose → Show progress
Example:
python JWTCrack.py -t eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... -w rockyou.txt -v



GenerateJWT.py

Generate a JWT for testing.

Edit the script first:
secret = "your-secret-key"

payload = {
    "user": "admin",
    "role": "admin"
}
Run:
python GenerateJWT.py
