*** Settings ***
Library           String
Library           JSONLibrary
Library           RequestsLibrary
Resource          common.resource

Test Setup    Setup Test


*** Variables ***
${RANDOM_NUMBER}                Generate Random String    10    [LETTERS]


*** Test Cases ***
Logs Variables
    [Documentation]    Print the variables section
    Log To Console    ${RANDOM_NUMBER}

dLogs Variables2
    [Documentation]    Print the variables section
    Log To Console    ${RANDOM_NUMBER}


*** Keywords ***
Delete Settings
    [Arguments]    ${auth_id}

    Log To Console    DELETE successful for ${auth_id}


Setup Test
    Setup Environment
    Log To Console    ${RANDOM_NUMBER}