#  CipherNest — File Encryption & Decryption Utility

**CipherNest** is a Python-based tool for secure local file encryption and decryption.  
It demonstrates the use of **symmetric encryption (AES via the `cryptography` library)** and provides a clean command-line interface to protect sensitive data.

---

##  Features
-  Encrypts and decrypts files using **AES encryption (Fernet implementation)**  
-  Generates and securely stores unique encryption keys  
-  Organizes encrypted files in a **local vault directory**  
-  Works entirely **offline** — no external network calls  
-  Clear, modular structure for **educational or demonstration use**

---

##  Installation Code


```bash
git clone https://github.com/Reeves004/CipherNest.git
cd CipherNest
pip install -r requirements.txt
python app.py
