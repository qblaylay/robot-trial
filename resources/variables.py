# robot_variables.py
from resources.testdata_generator import generate_robot_variables

random_data = generate_robot_variables()

# Random values
RANDOM_STRING        = random_data["RANDOM_STRING"]
RANDOM_STRING_UPPER  = random_data["RANDOM_STRING_UPPER"]
RANDOM_INT           = random_data["RANDOM_INT"]

# Test Random Variables

SYSTEM_VALUE              = random_data["SYSTEM_CODE"]
HOTEL                 = random_data["HOTEL_ID"]
