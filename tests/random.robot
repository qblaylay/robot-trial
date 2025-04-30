*** Settings ***
Resource    common.resource

Variables    variables.py

*** Test Cases ***
Use Random Variables
    Log    Username: ${API_STANDARD_CODE}