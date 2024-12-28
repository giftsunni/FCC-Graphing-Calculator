def validate_input(value, value_type=float):
    try:
        return value_type(value)
    except ValueError:
        raise ValueError(f"Invalid input: {value} is not of type {value_type.__name__}")

def format_table_data(data):
    formatted_data = []
    for x, y in data:
        formatted_data.append(f"x: {x:.2f}, y: {y:.2f}")
    return formatted_data

def get_range(start, end, step):
    return [round(start + i * step, 2) for i in range(int((end - start) / step) + 1)]