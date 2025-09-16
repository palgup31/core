"""Home assistant custom component setup.

This package provide the setup function used to initialize the integration.
"""

from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "hello_state"

# Empty config schema (no YAML options needed)
CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)


def setup(hass: HomeAssistant, base_config: ConfigType) -> bool:
    """Set up a skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.
    hass.states.set("hello_state.world", "Pallavi")

    # Return boolean to indicate that initialization was successfully.
    return True
