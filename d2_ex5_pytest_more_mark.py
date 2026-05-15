import pytest
import sys


@pytest.mark.skip
def test_not_used():
    assert 1 == 0

@pytest.mark.skip("this is the reason why we're skipping")
def test_not_used():
    assert 1 == 0


@pytest.mark.skipif(sys.platform != "linux",
                    reason="test running only on linux")
def test_only_on_nix():
    assert "linux" == "linux"


@pytest.mark.skipif(not sys.platform.startswith("win"),
                    reason="test running only on windows")
def test_only_on_win():
    assert "windows" == "windows"


@pytest.mark.skipif(sys.version_info >= (3, 8),
                  reason="test for Python <= 3.7")
def test_old_python():
    assert "old" is "new"


@pytest.mark.xfail
def test_that_fails_on_purpose():
    assert "failed" is "awesome"


# a custom mark
# we will want to skip these tests manually sometimes
# with: pytest -m 'not slow'
@pytest.mark.slow
def test_that_is_very_slow():
    import time
    time.sleep(5)
    assert 1 == 1


# another custom mark
# we will want to run only these tests manually sometimes
# with: pytest -m essential
@pytest.mark.essential
@pytest.mark.slow
def test_essential_1():
    assert 1 == 1

@pytest.mark.essential
def test_essential_2():
    assert 2 == 2

