def parse_test_data(data_list, index):
    try:
        # Might throw IndexError or TypeError
        value = int(data_list[index])
        result = 100 / value
    except IndexError:
        print("[ERROR] Index is out of bounds for the list!")
    except ZeroDivisionError:
        print("[ERROR] Cannot divide by zero in calculation!")
    except ValueError:
        print("[ERROR] The item found could not be converted to an integer!")
    except Exception as err:
    # Catches ANY standard error (IndexError, TypeError, ZeroDivisionError, etc.)
        print(f"[ERROR] Unexpected failure occurred: {type(err).__name__} -> {err}")
    else:
        print(f"Success! Calculated result: {result}")
    finally:
        print("Cleanup: Finished execution attempt.")

# Test it out:
parse_test_data(None, 1)
# parse_test_data(["10", "20", "0"], 2)  # Triggers ZeroDivisionError
# parse_test_data(["10", "20", "0"], 4)  # Triggers ZeroDivisionError
# parse_test_data(["10", "test", "0"], 1)  # Triggers ZeroDivisionError
# parse_test_data(["10", "20", "0"], 1)  # Triggers ZeroDivisionError