from read_files import read_public_key, read_encrypted_message


def brute_force_attack(public_key, encrypted_message):
    message_length = len(encrypted_message)
    possible_passwords = generate_possible_passwords(message_length)

    for password in possible_passwords:
        result = multiply_matrix(password, public_key)
        if result == encrypted_message:
            return password

    return None


def generate_possible_passwords(length):
    return [[int(digit) for digit in bin(i)[2:].zfill(length)] for i in range(2 ** length)]


def multiply_matrix(password, public_key):
    return [(sum(a * b for a, b in zip(row, password))) % 2 for row in public_key]


if __name__ == "__main__":
    public_key = read_public_key()
    encrypted_message = read_encrypted_message()

    recovered_password = brute_force_attack(public_key, encrypted_message)

    if recovered_password:
        print("Recovered Password:", recovered_password)
    else:
        print("Password recovery failed.")
