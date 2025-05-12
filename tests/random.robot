*** Settings ***
Documentation     Tests for random variable generation and usage
Resource          common.resource
Test Teardown     Log Variables To Report

*** Variables ***
${ACS_ENV}    development

*** Test Cases ***
Use Random Variables
    [Documentation]    Test that verifies random variable generation and usage
    ${random_string}=    Generate Random String    8    [LETTERS]
    Should Not Be Empty    ${random_string}
    Log    Generated random string: ${random_string}

Success
    [Documentation]    Test that verifies successful variable generation and usage
    ${random_number}=    Generate Random String    4    [NUMBERS]
    Should Not Be Empty    ${random_number}
    Log    Generated random number: ${random_number}

Test Regular URLs
    [Documentation]    Test regular URLs in current environment
    ${url}=    Get Full URL    ${REGULAR}
    Should Be Equal    ${url}    ${BASE_URL}

Test Mock URLs
    [Documentation]    Test mock URLs in current environment
    ${url}=    Get Full URL    ${MOCK}
    Should Be Equal    ${url}    ${MOCK_URL}