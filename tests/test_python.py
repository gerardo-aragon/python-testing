
# request param
# https://docs.pytest.org/en/6.2.x/fixture.html

def test01(test, request):
    print(request.config.getoption("--env"))
    assert 1 == 1


def test02(test):
    assert 1 == 1
