import random
import string
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class testdata_generator:
    """Class to generate random test data dynamically for each test execution."""

    def __init__(self):
        self.static_string = "random_value_"

    def generate_random_string(self, length=8):
        """Generates a random lowercase alphanumeric string."""
        return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))

    def generate_random_integer(self, min_val=1000, max_val=9999):
        """Generates a random integer within a given range."""
        return random.randint(min_val, max_val)

    def generate_robot_variables(self):
        """Generates a dictionary of random variables for testing."""
        random_string = self.generate_random_string()
        random_string_upper = random_string.upper()
        random_int = self.generate_random_integer()

        return {
            # Random string-based variables
            "RANDOM_STRING": random_string,
            "RANDOM_STRING_UPPER": random_string_upper,
            # Random integer-based variables
            "RANDOM_INT": random_int,
            # Configuration variables
            "SYSTEM_VALUE": f"{self.static_string}sys_{random_string}",
            
        }
