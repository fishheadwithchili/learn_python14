"""Demonstrate ExceptionGroup and except* (PEP 654).

Run with Python >=3.11
"""

def run_batch():
    errors = []
    try:
        1 / 0
    except ZeroDivisionError as e:
        errors.append(e)
    try:
        int("x")
    except ValueError as e:
        errors.append(e)
    if errors:
        raise ExceptionGroup("batch errors", errors)


try:
    run_batch()
except* ZeroDivisionError as eg:
    print("handled ZeroDivisionError group:", eg)
except* ValueError as eg:
    print("handled ValueError group:", eg)


