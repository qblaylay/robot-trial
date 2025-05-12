"""
This module contains variables used in the project.
The variables are used to store the URLs, environment, and other configurations.
"""

from robot.libraries.BuiltIn import BuiltIn

try:
    acs_env = BuiltIn().get_variable_value("${ACS_ENV}", "DES")
    AZURE_ENV = acs_env[-3:]
except:
    AZURE_ENV = "DES"

TENANT = {"INTERNAL": "its", "mm": "c.m"}

URL = (
    "https://{tenant}.xx.com"
    + AZURE_ENV.lower()
    + "/ebv/rest"
)

MOCK_URL = (
    "https://bb.{tenant}.mockserver.com/ddd/"
    + AZURE_ENV.lower()
)
MOCK_TARGET_URL = "https://sss.si-{env}.local:1204/"

MUXALT_URL = "muxalt-xxx-{env}.xxx.local:1204"
MUXDMO_URL = "muxdmo-xxx-{env}.xxx.local:1204"

# LOCAL DEV ENVIRONMENT URLS
MUXALT_URL_LOCAL_INGRESSHANDLER = "localhost:10005"
MUXDMO_URL_LOCAL_MOCKSERVER = "localhost:1082"
URL_LOCAL_CONFIGMANAGER = "http://localhost:10004"
LOCAL_LSS_RETRIEVEPERMISSIONS = "lll/ret"

## ArgoCD URL
ARGOCD_URL_AZURE = (
    "https://argocd.com/api/badge?name=wus2-01a-"
    + AZURE_ENV.lower()
    + "-hxx&revision=true"
)

## Configuration URL
AZURE_REST_URL_ADDITION = "rest/"

TRANSACTION_URL = "xxx/v1/configuration/trsc"
CONNECTED_SYSTEM_URL = "yyy/chains/tenancyCode/properties/propertyCode/cs"
SEARCH_CONNECTED_SYSTEM_URL = "yy/connected-systems/searches"
API_STANDARD_URL = "configuration/xxx"


# SPP Variables
SPP_SUFFIX = {"DES": "S", "DEV": "D", "PDT": "", "UAT": "U", "LOC": "L"}
MOCK_SPP = "MOCK" + SPP_SUFFIX[AZURE_ENV]
SPP = "XXX" + SPP_SUFFIX[AZURE_ENV]
SPP_SUPPORT_TOOL = "ASSS" + SPP_SUFFIX[AZURE_ENV]

SPP_FOR_URL = "/" + SPP
MOCKSPP_FOR_URL = "/" + MOCK_SPP
