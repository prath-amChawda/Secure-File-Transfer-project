# 🔐 Secure File Transfer

A **GUI-based Python application** that encrypts and decrypts files using **AES-based Fernet encryption**. This ensures secure file transfer by encrypting data before sending it and allowing only authorized users with the correct key to decrypt it.

## 📌 Features
- **Graphical User Interface (GUI)** for easy file selection.
- **AES-based encryption (Fernet algorithm)** for strong security.
- **Generates a unique encryption key** for every file transfer.
- **File decryption only possible with the saved key**.
- **Error handling** to manage invalid file selections.
- **Cross-platform support** (Windows, macOS, Linux).

---

## ⚙️ Installation

### **1️⃣ Install Python (if not installed)**
Download and install Python from [Python.org](https://www.python.org/downloads/).

### **2️⃣ Install Required Dependencies**
Run the following command to install the required Python library:

```sh
pip install cryptography


