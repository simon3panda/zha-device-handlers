"""Linxura button device."""

from zigpy.quirks import CustomCluster
from zigpy.zcl.clusters.security import IasZone

from zhaquirks.const import (
    BUTTON,
    BUTTON_1,
    BUTTON_2,
    BUTTON_3,
    BUTTON_4,
    COMMAND_ID,
    DOUBLE_PRESS,
    LONG_PRESS,
    PRESS_TYPE,
    SHORT_PRESS,
    ZHA_SEND_EVENT,
)

LINXURA = "Linxura"

PRESS_TYPES = {
    1: SHORT_PRESS,
    2: DOUBLE_PRESS,
    3: LONG_PRESS,
}


class LinxuraIASCluster(CustomCluster, IasZone):
    """IAS cluster used for Linxura button."""

    def _update_attribute(self, attrid, value):
        super()._update_attribute(attrid, value)
        if attrid == self.AttributeDefs.zone_status.id and 0 < value < 24:
            if 0 < value < 6:
                button = BUTTON_1
                press_type = PRESS_TYPES[value // 2 + 1]
            elif 6 < value < 12:
                button = BUTTON_2
                press_type = PRESS_TYPES[value // 2 - 3 + 1]
            elif 12 < value < 18:
                button = BUTTON_3
                press_type = PRESS_TYPES[value // 2 - 6 + 1]
            elif 18 < value < 24:
                button = BUTTON_4
                press_type = PRESS_TYPES[value // 2 - 9 + 1]
            action = f"{button}_{press_type}"
            event_args = {
                BUTTON: button,
                PRESS_TYPE: press_type,
                COMMAND_ID: 10,
            }
            self.listener_event(ZHA_SEND_EVENT, action, event_args)
