from read_files import read_public_key, read_encrypted_message

def log_method(func):
    def wrapper(*args, **kwargs):
        method_name = func.__name__
        with open("log.txt", "a") as log_file:
            log_file.write(f"Method '{method_name}' called.\n")
        return func(*args, **kwargs)
    return wrapper

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log_exception(func.__name__, str(e))

    def log_exception(function_name, exception_message):
        with open("exceptions_log.txt", "a") as log_file:
            log_file.write(f"Exception in '{function_name}': {exception_message}\n")

    return wrapper

def method_of_procedure(func):
    def wrapper(*args, **kwargs):
        with open("method_of_procedure.txt", "a") as mop_file:
            mop_file.write(f"Method of Procedure for '{func.__name__}':\n")

            mop_file.write("Step 1: Initialize variables.\n")
            mop_file.write("Explanation: Set up the necessary variables for the function.\n")

            mop_file.write("Step 2: Iterate through possible passwords.\n")
            mop_file.write("Explanation: Iterate through the list of possible passwords.\n")

            mop_file.write("Step 3: Calculate matrix multiplication.\n")
            mop_file.write("Explanation: Use matrix multiplication to check each password.\n")

            mop_file.write("Step 4: Check for a match.\n")
            mop_file.write("Explanation: Verify if the result matches the encrypted message.\n")

            mop_file.write("Step 5: Return the recovered password if found.\n")
            mop_file.write("Explanation: If a match is found, return the recovered password.\n")

            mop_file.write("Step 6: Return None if no match is found.\n")
            mop_file.write("Explanation: If no match is found, return None as the recovered password.\n")

        return func(*args, **kwargs)

    return wrapper

@log_method
def brute_force_attack(public_key, encrypted_message):
    message_length = len(encrypted_message)
    possible_passwords = generate_possible_passwords(message_length)
    return recover_password(possible_passwords, public_key, encrypted_message)

@handle_exceptions
def generate_possible_passwords(length):
    return [[int(digit) for digit in bin(i)[2:].zfill(length)] for i in range(2 ** length)]

@method_of_procedure
def recover_password(possible_passwords, public_key, encrypted_message):
    for password in possible_passwords:
        result = multiply_matrix(password, public_key)
        if result == encrypted_message:
            return password
    return None

def multiply_matrix(password, public_key):
    def compute_row(row, password):
        return sum(a * b for a, b in zip(row, password)) % 2

    return [compute_row(row, password) for row in public_key]

if __name__ == "__main__":
    public_key = read_public_key()
    encrypted_message = read_encrypted_message()

    recovered_password = brute_force_attack(public_key, encrypted_message)

    print("Recovered Password:", recovered_password) if recovered_password else print("Password recovery failed.")


#intentional error inserted for exception logging in the code below:

"""

from read_files import read_public_key, read_encrypted_message

def log_method(func):
    def wrapper(*args, **kwargs):
        method_name = func.__name__
        with open("log.txt", "a") as log_file:
            log_file.write(f"Method '{method_name}' called.\n")
        return func(*args, **kwargs)
    return wrapper


def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log_exception(func.__name__, str(e))

    def log_exception(function_name, exception_message):
        with open("exceptions_log.txt", "a") as log_file:
            log_file.write(f"Exception in '{function_name}': {exception_message}\n")

    return wrapper

@log_method
def brute_force_attack(public_key, encrypted_message):
    message_length = len(encrypted_message)
    length = -1  # Simulating the condition to trigger the exception
    possible_passwords = generate_possible_passwords(length)

    for password in possible_passwords:
        result = multiply_matrix(password, public_key)
        if result == encrypted_message:
            return password

        if all(a == b for a, b in zip(result, encrypted_message)):
            return password

    return None

@handle_exceptions
def generate_possible_passwords(length):
    if length < 0:  # Simulating an invalid operation that might raise an exception
        raise ValueError("Invalid length for generating possible passwords.")
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


"""
