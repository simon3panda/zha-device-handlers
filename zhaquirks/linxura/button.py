"""Linxura button device."""

from zigpy.profiles import zha
from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.general import Basic
from zigpy.zcl.clusters.security import IasZone

from zhaquirks.const import (
    BUTTON_1,
    BUTTON_2,
    BUTTON_3,
    BUTTON_4,
    CLUSTER_ID,
    COMMAND,
    DEVICE_TYPE,
    DOUBLE_PRESS,
    ENDPOINTS,
    INPUT_CLUSTERS,
    LONG_PRESS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
    SHORT_PRESS,
)
from zhaquirks.linxura import LINXURA, LinxuraIASCluster


class LinxuraButton(CustomDevice):
    """Linxura button device."""

    signature = {
        # <SimpleDescriptor endpoint=1 profile=260 device_type=1026
        # device_version=0
        # input_clusters=[0, 3, 1280]=>input_clusters=[0, 1280]
        # output_clusters=[3]>=>output_clusters=[]
        MODELS_INFO: [(LINXURA, "Smart Controller")],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.IAS_ZONE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    IasZone.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    LinxuraIASCluster,
                ],
                OUTPUT_CLUSTERS: [],
            },
        }
    }

    device_automation_triggers = {
        (press_type, button): {
            COMMAND: f"{button}_{press_type}",
            CLUSTER_ID: IasZone.cluster_id,
        }
        for press_type in (SHORT_PRESS, DOUBLE_PRESS, LONG_PRESS)
        for button in (BUTTON_1, BUTTON_2, BUTTON_3, BUTTON_4)
    }
