"""Linxura button device."""

from zigpy.quirks import CustomCluster
import zigpy.zcl.clusters.security

from zhaquirks.const import (
    BUTTON,
    BUTTON_1,
    BUTTON_2,
    BUTTON_3,
    BUTTON_4,
    COMMAND_DOUBLE,
    COMMAND_HOLD,
    COMMAND_ID,
    COMMAND_PRESS,
    PRESS_TYPE,
    ZHA_SEND_EVENT,
)

LINXURA = "Linxura"
STATUS_REPORT = 2


PRESS_TYPES = {
    1: SHORT_PRESS,
    2: DOUBLE_PRESS,
    3: LONG_PRESS,
}


class LinxuraIASCluster(CustomCluster, zigpy.zcl.clusters.security.IasZone):
    """Occupancy cluster."""

    def _update_attribute(self, attrid, value):
        self.info("Linxura update attribute - attrid: %d, value:%d", attrid, value)
        super()._update_attribute(attrid, value)
        if attrid == self.AttributeDefs.zone_status.id:
            if value > 0 and value < 24:
                if value > 0 and value < 6:
                    button = BUTTON_1
                    press_type = PRESS_TYPES[value // 2 + 1]
                if value > 6 and value < 12:
                    button = BUTTON_2
                    press_type = PRESS_TYPES[value // 2 - 3 + 1]
                if value > 12 and value < 18:
                    button = BUTTON_3
                    press_type = PRESS_TYPES[value // 2 - 6 + 1]
                if value > 18 and value < 24:
                    button = BUTTON_4
                    press_type = PRESS_TYPES[value // 2 - 9 + 1]
                action = f"{button}_{press_type}"
                event_args = {
                    BUTTON: button,
                    PRESS_TYPE: press_type,
                    COMMAND_ID: 10,  # to maintain backwards compatibility
                }
                self.listener_event(ZHA_SEND_EVENT, action, event_args)
