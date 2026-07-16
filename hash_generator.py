import hashlib

print("=" * 50)
print(" HASH GENERATOR & FILE INTEGRITY CHECKER ")
print("=" * 50)

text = input("Enter text to hash: ")

print("\nChoose Hash Algorithm")
print("1. MD5")
print("2. SHA1")
print("3. SHA256")

choice = input("Enter choice (1-3): ")

if choice == "1":
    result = hashlib.md5(text.encode()).hexdigest()
    print("\nMD5 Hash:")
    print(result)

elif choice == "2":
    result = hashlib.sha1(text.encode()).hexdigest()
    print("\nSHA1 Hash:")
    print(result)

elif choice == "3":
    result = hashlib.sha256(text.encode()).hexdigest()
    print("\nSHA256 Hash:")
    print(result)

else:
    print("Invalid Choice")