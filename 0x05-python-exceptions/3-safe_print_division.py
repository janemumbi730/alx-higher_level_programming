def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: None")
        print("Error: Division by zero is not allowed.")
        return None
    except Exception as e:
        print("Inside result: None")
        print("Error:", str(e))
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        print("Finally block executed.")
