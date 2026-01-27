#capsys is a fixture allows to capture output to stdout and stderr during tests,useful whe  you want to test functions that print
def test_greet(capsys):
    from greet import greet
    greet("Alice")
    #readouter resets the output
    captured=capsys.readouterr()
    assert captured.out.strip() == "Hello, Alice!"