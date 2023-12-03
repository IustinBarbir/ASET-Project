def log_sensitive_access(func):
    def wrapper(*args, **kwargs):
        accessed_module = func.__module__
        if "read_files" in accessed_module:
            with open("security_log.txt", "a") as log_file:
                log_file.write(f"Sensitive access to module '{accessed_module}' detected.\n")
        return func(*args, **kwargs)
    return wrapper