import random
import string
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class TestDataGenerator:
    """A class for generating random test data for Robot Framework tests.
    
    This class provides methods to generate various types of random test data
    that can be used in Robot Framework test cases. It follows the principle
    of generating unique data for each test execution.
    """

    def __init__(self):
        """Initialize the TestDataGenerator with default values."""
        self.static_string = "random_value_"
        self._cached_variables = None

    @keyword("Generate Random String")
    def generate_random_string(self, length: int = 8) -> str:
        """Generate a random lowercase alphanumeric string.
        
        Args:
            length (int): Length of the string to generate. Defaults to 8.
            
        Returns:
            str: Random alphanumeric string in lowercase.
        """
        return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))

    @keyword("Generate Random Integer")
    def generate_random_integer(self, min_val: int = 1000, max_val: int = 9999) -> int:
        """Generate a random integer within a given range.
        
        Args:
            min_val (int): Minimum value for the random number. Defaults to 1000.
            max_val (int): Maximum value for the random number. Defaults to 9999.
            
        Returns:
            int: Random integer within the specified range.
        """
        return random.randint(min_val, max_val)

    @keyword("Generate Robot Variables")
    def generate_robot_variables(self, force_new: bool = False) -> dict:
        """Generate a dictionary of random variables for Robot Framework tests.
        
        Args:
            force_new (bool): If True, generates new random values even if cached.
                            If False, returns cached values if they exist.
        
        Returns:
            dict: Dictionary containing various random test variables.
        """
        if not force_new and self._cached_variables is not None:
            return self._cached_variables

        random_string = self.generate_random_string()
        random_string_upper = random_string.upper()
        random_int = self.generate_random_integer()

        self._cached_variables = {
            # Random string-based variables
            "RANDOM_STRING": random_string,
            "RANDOM_STRING_UPPER": random_string_upper,
            # Random integer-based variables
            "RANDOM_INT": random_int,
            # Configuration variables
            "SYSTEM_VALUE": f"{self.static_string}sys_{random_string}",
            # New variable example
            "NEW_VARIABLE": f"new_var_{random_string}_{random_int}",
        }
        
        return self._cached_variables

    @keyword("Reset Random Variables")
    def reset_variables(self):
        """Reset the cached variables to force new random values on next generation."""
        self._cached_variables = None
