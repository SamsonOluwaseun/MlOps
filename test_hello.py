from hello import more_hello, more_goodbye


def test_more_hello():
    assert "hi" == more_hello()  # Passes


def test_more_goodbye():
    assert "bye" == more_goodbye()  # Passes
