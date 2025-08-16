def format_response(result):
    """
    Ensure response is always a 4-element JSON array.
    """
    if not isinstance(result, list):
        return [None, str(result), None, None]

    # Pad or truncate to 4 elements
    if len(result) < 4:
        result += [None] * (4 - len(result))
    elif len(result) > 4:
        result = result[:4]

    return result
