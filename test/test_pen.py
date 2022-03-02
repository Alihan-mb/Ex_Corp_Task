import sys
import io

import pytest

from page.Pen import Pen
from page.constant import TestingData


@pytest.mark.write
def test_write():
    pen = TestingData.PEN1
    r = pen.write(TestingData.WORD)
    assert r == "", "It failed"

@pytest.mark.write
def test_write1():
    pen = TestingData.PEN2
    word = TestingData.WORD
    output = pen.write(word)
    assert word == output, "it failed"

@pytest.mark.write
def test_write2():
    pen = TestingData.PEN3
    output = pen.write(TestingData.WORD)
    assert "par" == output, "it failed"

@pytest.mark.write
def test_write3():
    pen = TestingData.PEN4
    output = pen.write(TestingData.WORD)
    assert "par" != output, "it failed"

@pytest.mark.color
def test_GetRightColor():
    red = "red"
    pen = Pen(ink_container_value=0, color=red)
    assert pen.get_color() != red, "it failed"

@pytest.mark.color
def test_GetRightColor1():
    blue = "blue"
    pen = Pen(ink_container_value=0, color=blue)
    assert pen.get_color() == blue, "it failed"

@pytest.mark.state
def test_pen_state():
    pen1 = Pen(ink_container_value=0)
    pen2 = Pen(ink_container_value=1)
    assert False == pen1.check_pen_state(), "it failed"
    assert True == pen2.check_pen_state(), "it failed"

@pytest.mark.green
def test_something_else():
    color = "green"
    pen = Pen(ink_container_value=0, color=color)
    output = io.StringIO()
    sys.stdout = output
    pen.do_something_else()
    content = output.getvalue()
    newstr = content.strip()
    assert newstr == color



# new_stdout = io.StringIO()
#     sys.stdout = new_stdout
#     pen.do_something_else()
#     output = new_stdout.getvalue()
#     assert output == color








