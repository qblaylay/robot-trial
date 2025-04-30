*** Settings ***
Library    OperatingSystem
Library    String

Test Setup       Setup Test
Test Teardown    Teardown Test


*** Test Cases ***
Failing Test Example
    [Tags]    Example
    Fail    Simulated failure for testing report modification.


*** Keywords ***
Setup Test
    ${RANDOM_VALUE}    Generate Random Value
    Set Suite Variable    ${RANDOM_CODE}    CODE${RANDOM_VALUE}
    Set Suite Variable    ${GET_ID}    GET_ID_${RANDOM_VALUE.upper()}
    Set Suite Variable    ${SYS}    SYS_${RANDOM_VALUE}
    Set Suite Variable    ${ID}    id-${random_value}
    Set Suite Variable
    ...    ${PATH}
    ...    v1/${SYS}/hotels/${HOTEL}/businessEvents

Teardown Test
    Run Keyword If Test Failed    Log Failure Details    ${TEST MESSAGE}

Generate Random Value
    ${random}    Generate Random String    10    [LOWER][NUMBERS]
    RETURN    ${random}

Log Failure Details
    [Arguments]    ${reason}
    Log    Test Name: ${TEST NAME}
    Log    Status: ${TEST STATUS}
    Log    Failure Reason: ${TEST MESSAGE}
    Log    Test failed with reason: ${reason}
    Log    HOTEL-ID: ${ID} \n BusinessEvent: ${GET_ID} \n BusinessPath: ${PATH}