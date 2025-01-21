from cryptography.fernet import Fernet

# Generarea unei chei de criptare
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Cheia de criptare a fost generată și salvată în 'key.key'.")

# Încărcarea cheii din fișier
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Criptarea unui mesaj
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Decriptarea unui mesaj criptat
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

if __name__ == "__main__":
    # Generăm cheia o singură dată
    generate_key()
    key = load_key()

    # Mesaj de test
    original_message = "Acesta este un mesaj securizat."
    print(f"Mesaj original: {original_message}")

    # Criptarea mesajului
    encrypted_message = encrypt_message(original_message, key)
    print(f"Mesaj criptat: {encrypted_message}")

    # Decriptarea mesajului
    decrypted_message = decrypt_message(encrypted_message, key)
    print(f"Mesaj decriptat: {decrypted_message}")
