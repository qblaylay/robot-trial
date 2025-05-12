*** Settings ***
Library      Collections
Library      String
Library      RequestsLibrary
Library      JSONLibrary
Library      protocols
Library      DateTime
Library      variable_loader.py
Variables    variables/url_variables.py
Variables    variables/common_variables.yml
Variables    variables/random_variables.yml
Variables    variables/system_variables.yml
Variables    credentials/baisc.py


*** Variables ***
${ACS_ENV}                ${EMPTY}
${TENANCY_CODE}           ${EMPTY}
${PROPERTY_CODE}          ${EMPTY}
${BASE_DCX_HEADER}        <DCC VERS="1.0"><MW><UKEY TRXNB="1" VAL="INT_DCX_PCG"/><SPP NAME="{{SPP_NAME}}"/></DCC>
${BASE_LSS_DCX_HEADER}    <DCC VERS="1.0"><MW><UKEY TRXNB="1"/><SPP NAME="{{SPP_NAME}}" FARM="WEB" DCNAME="" ENC="U8"/><DYNR><PEAKTK TYPE="CHAIN" VAL="{{CHAIN_VALUE}}"/></DYNR></MW><SEC VERS="2.11" CONTENTS="UNDEFINED"><USERINFOS><OFFICEID VALUE="${ROBOTIC_LSS_USER}[office_id]"/><SIGN VALUE="${ROBOTIC_LSS_USER}[sign_value]"/><SIGN_OFFICE VALUE="${ROBOTIC_LSS_USER}[office_id]"/><OOFF VALUE="${ROBOTIC_LSS_USER}[office_id]"/><AREACODE VALUE="A"/><USERID VALUE="${ROBOTIC_LSS_USER}[user_id]"/><ORGANIZATION VALUE="${ROBOTIC_LSS_USER}[organization]"/></DCC>


*** Keywords ***
Setup Environment
    Get Url
    IF    '${AZURE_ENV}' in ['LOC']
        Log    Deployed version: LOCAL    console=True
        ${access_token}    Set Variable    "LOCAL"
        Set Suite Variable    ${SPP}    ${EMPTY}
        Set Suite Variable    ${MOCK_SPP}    ${EMPTY}
        Set Suite Variable    ${SPP_SUPPORT_TOOL}   ${EMPTY}
        Set Suite Variable    ${MUXALT_URL}    ${MUXALT_URL_LOCAL_INGRESSHANDLER}
        Set Suite Variable    ${MUXDMO_URL}    ${MUXDMO_URL_LOCAL_MOCKSERVER}
        Set Suite Variable    ${SPP_FOR_URL}    ${EMPTY}
        Set Suite Variable    ${MOCKSPP_FOR_URL}    ${EMPTY}
        Set Suite Variable    \${acc}
    ELSE
        Set Suite Variable    \${acc}    None

    END
    Generate Test Variables
    Log To Console    \nGenerated Variables:
    Log To Console    ${SYSTEM_VALUE} | ${random.RANDOM_STRING} | ${RANDOM_STRING_UPPER} | ${RANDOM_INT} | ${HOTEL} | ${NEW_VARIABLE}  |  ${API_CODE}

Get Url
    [Arguments]    ${env_value}=${AZURE_ENV}    ${tenant_key}=INTERNAL
    IF    '${env_value}' not in ['DES', 'LOC']
        ${tenant_key}    Set Variable    MARRIOTT
    END

    IF    '${env_value}' in ['LOC']
        Set Suite Variable    \${URL_PCG_INGRESSHANDLER}    http://${MUXALT_URL_LOCAL_INGRESSHANDLER}
        Set Suite Variable    \${URL_PCG_CONFIGMANAGER}    ${URL_LOCAL_CONFIGMANAGER}
        Set Suite Variable    \${URL_MOCKSERVER}    http://${MUXDMO_URL_LOCAL_MOCKSERVER}
    ELSE 
        ${URL_PCG_INGRESSHANDLER}    Replace String    ${URL}    {tenant}    ${TENANT}[${tenant_key}]
        ${URL_PCG_CONFIGMANAGER}    Replace String    ${URL}    {tenant}    ${TENANT}[${tenant_key}]
        Set Suite Variable    \${URL_PCG_INGRESSHANDLER} 
        Set Suite Variable    \${URL_PCG_CONFIGMANAGER}
    END