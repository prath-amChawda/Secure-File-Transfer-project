import os
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

class SecureFileTransferApp:
    def __init__(self, master):
        self.master = master
        master.title("Secure File Transfer")

        self.label = tk.Label(master, text="Select a file to transfer:")
        self.label.pack()

        self.file_path = tk.StringVar()
        self.file_entry = tk.Entry(master, textvariable=self.file_path, width=50)
        self.file_entry.pack()

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.pack()

        self.encrypt_button = tk.Button(master, text="Encrypt and Transfer", command=self.encrypt_and_transfer)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(master, text="Decrypt File", command=self.decrypt_file)
        self.decrypt_button.pack()

    def browse_file(self):
        filename = filedialog.askopenfilename()
        self.file_path.set(filename)

    def encrypt_and_transfer(self):
        file_path = self.file_path.get()
        if not file_path:
            messagebox.showerror("Error", "Please select a file.")
            return

        # Generate a key for encryption
        key = Fernet.generate_key()
        cipher = Fernet(key)

        # Read the file
        with open(file_path, 'rb') as file:
            file_data = file.read()

        # Encrypt the file data
        encrypted_data = cipher.encrypt(file_data)

        # Save the encrypted file
        encrypted_file_path = file_path + '.encrypted'
        with open(encrypted_file_path, 'wb') as file:
            file.write(encrypted_data)

        # Save the key to a file (in a real application, you should handle this securely)
        with open('key.key', 'wb') as key_file:
            key_file.write(key)

        messagebox.showinfo("Success", f"File encrypted and saved as {encrypted_file_path}.\nKey saved as key.key.")

    def decrypt_file(self):
        key_file_path = filedialog.askopenfilename(title="Select Key File", filetypes=[("Key Files", "*.key")])
        if not key_file_path:
            messagebox.showerror("Error", "Please select a key file.")
            return

        encrypted_file_path = filedialog.askopenfilename(title="Select Encrypted File", filetypes=[("Encrypted Files", "*.encrypted")])
        if not encrypted_file_path:
            messagebox.showerror("Error", "Please select an encrypted file.")
            return

        # Load the key
        with open(key_file_path, 'rb') as key_file:
            key = key_file.read()

        cipher = Fernet(key)

        # Read the encrypted file
        with open(encrypted_file_path, 'rb') as file:
            encrypted_data = file.read()

        # Decrypt the file data
        decrypted_data = cipher.decrypt(encrypted_data)

        # Save the decrypted file
        decrypted_file_path = encrypted_file_path.replace('.encrypted', '.decrypted')
        with open(decrypted_file_path, 'wb') as file:
            file.write(decrypted_data)

        messagebox.showinfo("Success", f"File decrypted and saved as {decrypted_file_path}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SecureFileTransferApp(root)
    root.mainloop()