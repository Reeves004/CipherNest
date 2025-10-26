from encryption_utils import generate_key, encrypt_file, decrypt_file
import os

def main():
    print("""
    =====================================
            🔐 CipherNest Vault
           "Secure your secrets."
    =====================================
    1. Generate Encryption Key
    2. Encrypt a File
    3. Decrypt a File
    4. Exit
    """)

    while True:
        choice = input("\n[?] Enter choice (1-4): ").strip()

        if choice == "1":
            generate_key()

        elif choice == "2":
            file_path = input("[+] Enter path of file to encrypt: ").strip()
            if os.path.exists(file_path):
                encrypt_file(file_path)
            else:
                print("[!] File not found.")

        elif choice == "3":
            file_path = input("[+] Enter path of file to decrypt: ").strip()
            if os.path.exists(file_path):
                decrypt_file(file_path)
            else:
                print("[!] File not found.")

        elif choice == "4":
            print("[*] Exiting CipherNest. Stay secure 🛡️")
            break

        else:
            print("[!] Invalid choice. Try again.")

if __name__ == "__main__":
    main()
