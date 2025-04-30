*** Settings ***
Library      Collections
Library      String
Library      RequestsLibrary
Library      JSONLibrary
Library      protocols
Library      DateTime
Library      dynamic_variables.py

Variables    tests_variables.py



*** Variables ***

*** Keywords ***
Setup Environment
    ${test_data}    Generate Random Test Variables
    Log    ${SYSTEM_VALUE}    console=True