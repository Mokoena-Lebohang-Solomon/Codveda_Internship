import os

from cryptography.fernet import Fernet


KEY_FILE = "secret.key"


def generate_key():
    key = Fernet.generate_key()

    with open(
        KEY_FILE,
        "wb"
    ) as file:

        file.write(key)

    print("Encryption key generated.")


def load_key():

    if not os.path.exists(KEY_FILE):
        print("Encryption key does not exist.")
        print("Generate a key first.")
        return None

    try:
        with open(
            KEY_FILE,
            "rb"
        ) as file:

            return file.read()

    except OSError as error:
        print(f"Error reading key: {error}")
        return None


def encrypt_file(input_file, output_file):

    key = load_key()

    if key is None:
        return

    try:
        with open(
            input_file,
            "rb"
        ) as file:

            data = file.read()

        encrypted_data = Fernet(key).encrypt(data)

        with open(
            output_file,
            "wb"
        ) as file:

            file.write(encrypted_data)

        print(
            f"File encrypted successfully: {output_file}"
        )

    except FileNotFoundError:
        print("Input file was not found.")

    except OSError as error:
        print(f"File error: {error}")


def decrypt_file(input_file, output_file):

    key = load_key()

    if key is None:
        return

    try:

        with open(
            input_file,
            "rb"
        ) as file:

            encrypted_data = file.read()

        decrypted_data = Fernet(key).decrypt(
            encrypted_data
        )

        with open(
            output_file,
            "wb"
        ) as file:

            file.write(decrypted_data)

        print(
            f"File decrypted successfully: {output_file}"
        )

    except FileNotFoundError:
        print("Encrypted file was not found.")

    except Exception:
        print(
            "Decryption failed. "
            "The key or encrypted file may be invalid."
        )


def main():

    while True:

        print("\n" + "=" * 40)
        print("FILE ENCRYPTION TOOL")
        print("=" * 40)

        print("1. Generate encryption key")
        print("2. Encrypt file")
        print("3. Decrypt file")
        print("4. Exit")

        choice = input(
            "\nSelect an option: "
        ).strip()

        if choice == "1":

            generate_key()

        elif choice == "2":

            input_file = input(
                "Enter file to encrypt: "
            ).strip()

            output_file = input(
                "Enter encrypted output filename: "
            ).strip()

            encrypt_file(
                input_file,
                output_file
            )

        elif choice == "3":

            input_file = input(
                "Enter encrypted file: "
            ).strip()

            output_file = input(
                "Enter decrypted output filename: "
            ).strip()

            decrypt_file(
                input_file,
                output_file
            )

        elif choice == "4":

            print("Goodbye!")
            break

        else:

            print("Invalid option.")


if __name__ == "__main__":
    main()