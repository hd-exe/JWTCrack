import jwt
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Simple tool for brute-forcing JWT secrets"
    )
    parser.add_argument("-t", "--token", required=True,
                        help="JWT token to crack")
    parser.add_argument("-w", "--wordlist", required=True,
                        help="Path to wordlist")
    parser.add_argument("-a", "--algorithm",
                        choices=["HS256", "HS384", "HS512"],
                        default="HS256",
                        help="JWT algorithm (default: HS256)")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Show progress output")
    args = parser.parse_args()
    token = args.token
    wordlist_path = args.wordlist
    algorithm = args.algorithm
    verbose = args.verbose
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for i, line in enumerate(f, 1):
                key = line.strip()
                if not key:
                    continue
                try:
                    jwt.decode(token, key, algorithms=[algorithm])
                    print(f"\n[!!!] Found match for secret: {key}")
                    print(f"[+] Attempts: {i}")
                    return
                except jwt.exceptions.InvalidSignatureError:
                    pass
                except Exception:
                    pass
                if verbose and i % 250 == 0:
                    print(f"[-] Tried {i} keys...", end="\r")
        print("\n[-] Secret is not present in wordlist.")
    except FileNotFoundError:
        print(f"Wordlist not found at: {wordlist_path}")
if __name__ == "__main__":
    main()
