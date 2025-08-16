from adapter import format_response

def test_format_response_valid():
    res = format_response([1, "ok", 0.2, "img"])
    assert len(res) == 4

def test_format_response_padding():
    res = format_response([1, "ok"])
    assert len(res) == 4
    assert res[2] is None

def test_format_response_truncate():
    res = format_response([1, "ok", 2, "img", "extra"])
    assert len(res) == 4
