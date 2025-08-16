from typing import Any, List
import logging

logging.basicConfig(level=logging.INFO)

def format_response(result: Any) -> List[Any]:
    """
    Ensure API response is always a 4-element JSON array:
    [ans1, ans2, ans3, plot]

    - Pads with None if fewer than 4 elements
    - Truncates if more than 4
    - Converts non-list inputs into a safe error response
    """
    if not isinstance(result, list):
        logging.warning("Non-list response detected, wrapping into error format")
        return [None, str(result), None, None]

    # Normalize list length to exactly 4
    if len(result) < 4:
        result = result + [None] * (4 - len(result))
    elif len(result) > 4:
        result = result[:4]

    return result
