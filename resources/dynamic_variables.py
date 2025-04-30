# dynamic_variables.py

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from testdata_generator import testdata_generator

generator = testdata_generator()


@keyword("Generate Random Test Variables")
def generate_random_test_variables():
    variables = generator.generate_robot_variables()
    bi = BuiltIn()
    for key, value in variables.items():
        bi.set_test_variable(f"${{{key}}}", value)
