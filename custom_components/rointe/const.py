"""Constants for the Rointe Heaters integration."""

DOMAIN = "rointe"
DEVICE_DOMAIN = "climate"
ATTRIBUTION = "Data provided by rointeconnect.com"

# Rointe's firebase app values.
FIREBASE_APP_KEY = "AIzaSyBi1DFJlBr9Cezf2BwfaT-PRPYmi3X3pdA"
FIREBASE_DEFAULT_URL = "https://elife-prod.firebaseio.com"
FIREBASE_INSTALLATIONS_PATH = "/installations2.json"
FIREBASE_DEVICES_PATH_BY_ID = "/devices/{}.json"
FIREBASE_DEVICE_DATA_PATH_BY_ID = "/devices/{}/data.json"

AUTH_HOST = "https://www.googleapis.com"
AUTH_VERIFY_URL = "/identitytoolkit/v3/relyingparty/verifyPassword"
AUTH_ACCT_INFO_URL = "/identitytoolkit/v3/relyingparty/getAccountInfo"
AUTH_TIMEOUT_SECONDS = 15


CONF_USERNAME = "rointe_username"
CONF_PASSWORD = "rointe_password"
CONF_INSTALLATION = "rointe_installation"
CONF_LOCAL_ID = "rointe_local_id"

ROINTE_DEVICE_MANAGER = "rointe_device_manager"
ROINTE_HA_ROINTE_MAP = "rointe_ha_rointe_map"
ROINTE_HA_DEVICES = "rointe_ha_devices"
ROINTE_HA_SIGNAL_UPDATE_ENTITY = "rointe_entry_update"
ROINTE_API_REFRESH_SECONDS = 30
ROINTE_SUPPORTED_DEVICES = ["radiator", "towel", "therm"]

CMD_SET_TEMP = "cmd_set_temp"
CMD_SET_PRESET = "cmd_set_preset"
CMD_HVAC_OFF = "cmd_turn_off"
