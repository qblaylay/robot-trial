import random
import string
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from urllib.parse import urljoin

# Constants for variable generation
DEFAULT_STRING_LENGTH = 8
DEFAULT_MIN_INT = 1000
DEFAULT_MAX_INT = 9999

# List of variables to track
TRACKED_VARIABLES = [
    "RANDOM_STRING",
    "RANDOM_STRING_UPPER",
    "RANDOM_INT",
    "SYSTEM_VALUE",
    "HOTEL",
    "NEW_VARIABLE"
]

@keyword("Generate Random String")
def generate_random_string(length=DEFAULT_STRING_LENGTH):
    """Generate a random string of specified length.
    
    Args:
        length (int): Length of the random string to generate.
        
    Returns:
        str: Random string containing lowercase letters and digits.
    """
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

@keyword("Generate Random Integer")
def generate_random_integer(min_val=DEFAULT_MIN_INT, max_val=DEFAULT_MAX_INT):
    """Generate a random integer within the specified range.
    
    Args:
        min_val (int): Minimum value for the random integer.
        max_val (int): Maximum value for the random integer.
        
    Returns:
        int: Random integer within the specified range.
    """
    return random.randint(min_val, max_val)

@keyword("Generate Test Variables")
def generate_test_variables():
    """Generate all test variables with random values and set them as test variables.
    
    Returns:
        dict: Dictionary containing all generated variables.
    """
    random_string = generate_random_string()
    random_int = generate_random_integer()
    
    variables = {
        "RANDOM_STRING": random_string,
        "RANDOM_STRING_UPPER": random_string.upper(),
        "RANDOM_INT": random_int,
        "SYSTEM_VALUE": f"system_{random_string}",
        "HOTEL": f"hotel_{random_int}",
        "NEW_VARIABLE": f"new_{random_string}_{random_int}"
    }
    
    # Set all variables at once
    builtin = BuiltIn()
    for key, value in variables.items():
        builtin.set_test_variable(f"${{{key}}}", value)
    
    return variables

@keyword("Get Environment URL Config")
def get_environment_url_config(url_type=None):
    """Get the URL configuration for the current environment and URL type.
    
    Args:
        url_type (str, optional): Type of URL to use ('regular' or 'mock'). 
                                 If not provided, uses DEFAULT_URL_TYPE from variables.
    
    Returns:
        tuple: A tuple containing (base_url, api_version) for the current environment.
    """
    builtin = BuiltIn()
    env = builtin.get_variable_value("${SYSTEM_ENV}")
    urls = builtin.get_variable_value("${URLS}")
    
    if env not in urls:
        raise ValueError(f"No URL configuration found for environment: {env}")
    
    # If url_type not provided, use default
    if url_type is None:
        url_type = builtin.get_variable_value("${DEFAULT_URL_TYPE}")
    
    if url_type not in urls[env]:
        raise ValueError(f"No URL configuration found for type '{url_type}' in environment: {env}")
    
    env_config = urls[env][url_type]
    return env_config["BASE_URL"], env_config["API_VERSION"]

@keyword("Get Full URL")
def get_full_url(endpoint_key, url_type=None):
    """Get the full URL for a given endpoint.
    
    Args:
        endpoint_key (str): Key of the endpoint in ENDPOINTS dictionary.
        url_type (str, optional): Type of URL to use ('regular' or 'mock').
                                 If not provided, uses DEFAULT_URL_TYPE from variables.
        
    Returns:
        str: Complete URL for the endpoint.
    """
    builtin = BuiltIn()
    base_url, api_version = get_environment_url_config(url_type)
    endpoints = builtin.get_variable_value("${ENDPOINTS}")
    
    if endpoint_key not in endpoints:
        raise ValueError(f"Endpoint key '{endpoint_key}' not found in ENDPOINTS")
    
    endpoint = endpoints[endpoint_key]
    # Ensure base_url ends with a slash
    if not base_url.endswith('/'):
        base_url += '/'
    # Ensure api_version doesn't start or end with a slash
    api_version = api_version.strip('/')
    # Ensure endpoint starts with a slash
    if not endpoint.startswith('/'):
        endpoint = '/' + endpoint
    
    return f"{base_url}{api_version}{endpoint}"

@keyword("Log Variables To Report")
def log_variables_to_report():
    """Log all generated variables to the report for debugging purposes.
    
    Returns:
        dict: Dictionary containing all current variable values.
    """
    builtin = BuiltIn()
    variables = {}
    
    # Get current values of all tracked variables
    for var_name in TRACKED_VARIABLES:
        value = builtin.get_variable_value(f"${{{var_name}}}")
        variables[var_name] = value
    
    # Log to both console and report
    builtin.log("Test Variables for Debugging:", level="INFO")
    for key, value in variables.items():
        builtin.log(f"{key}: {value}", level="INFO")
    
    return variables 