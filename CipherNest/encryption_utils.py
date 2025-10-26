import os
import logging
from cryptography.fernet import Fernet

# Setup a logs folder
if not os.path.exists("logs"):
    os.mkdir("logs")

# Configure logging
logging.basicConfig(
    filename="logs/vault_activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

KEY_FILE = "vault_key.key"
VAULT_DIR = "vault"


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    logging.info("New encryption key generated.")
    print("[+] New encryption key generated and saved.")


def load_key():
    if not os.path.exists(KEY_FILE):
        print("[!] No key found. Generate one first.")
        logging.warning("Attempted to load key before one was generated.")
        return None
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


def encrypt_file(file_path):
    key = load_key()
    if key is None:
        return
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)
    encrypted_path = os.path.join(VAULT_DIR, os.path.basename(file_path) + ".encrypted")

    with open(encrypted_path, "wb") as enc_file:
        enc_file.write(encrypted_data)

    print(f"[+] File '{file_path}' encrypted successfully -> '{encrypted_path}'")
    logging.info(f"Encrypted file: {file_path} -> {encrypted_path}")


def decrypt_file(file_path):
    key = load_key()
    if key is None:
        return
    cipher = Fernet(key)

    with open(file_path, "rb") as enc_file:
        encrypted_data = enc_file.read()

    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_path = os.path.join(VAULT_DIR, os.path.basename(file_path).replace(".encrypted", ".decrypted"))

    with open(decrypted_path, "wb") as dec_file:
        dec_file.write(decrypted_data)

    print(f"[+] File '{file_path}' decrypted successfully -> '{decrypted_path}'")
    logging.info(f"Decrypted file: {file_path} -> {decrypted_path}")
