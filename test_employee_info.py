import employee_info


def test_get_employees_by_age():
    age_lower = 30
    age_upper = 40

    answer = [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
            {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]

    result = employee_info.get_employees_by_age_range(age_lower, age_upper)

    assert result == answer


def test_calculate_average_salary():
    answer = 60167
    result = employee_info.calculate_average_salary()

    assert result == answer


def test_get_employees_by_dept():
    dept = "Engineering"

    answer = [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
            {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]

    result = employee_info.get_employees_by_dept(dept)

    assert result == answer