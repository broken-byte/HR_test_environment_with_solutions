

def log_recursion(recursion_level: int, testable: bool = False, **kwargs):
    logging_message: str = (f"=============== Recursion Logger ===============\n"
                            f"Recursion level: {recursion_level}\n")
    for parameter, value in kwargs.items():
        logging_message += f"{parameter}: {value}\n"

    if testable:
        return logging_message
    else:
        print(logging_message)
