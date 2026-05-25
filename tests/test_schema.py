from claude_api_python.schemas import PythonTip


def test_schema_valid():
    tip = PythonTip(title="t", explanation="e", example="print(1)")
    assert tip.title == "t"
