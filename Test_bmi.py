import DEVOPS_Lab2.bmi as bmi


def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.75, 70)
    assert (result == 0)


def test_bmi_underweight():
    result = bmi.calculate_bmi(1.75, 50)
    assert (result == -1)


def test_bmi_overweight():
    result = bmi.calculate_bmi(1.75, 90)
    assert (result == 1)