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
    COMMAND_DOUBLE,
    COMMAND_HOLD,
    COMMAND_PRESS,
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

BTN_1 = "Button 1"
BTN_2 = "Button 2"
BTN_3 = "Button 3"
BTN_4 = "Button 4"


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
        (SHORT_PRESS, BTN_1): {
            COMMAND: f"{BUTTON_1}_{COMMAND_PRESS}",
            CLUSTER_ID: IasZone.cluster_id,
        },
        (DOUBLE_PRESS, BTN_1): {
            COMMAND: f"{BUTTON_1}_{COMMAND_DOUBLE}",
            CLUSTER_ID: IasZone.cluster_id,
        },
        (LONG_PRESS, BTN_1): {
            COMMAND: f"{BUTTON_1}_{COMMAND_HOLD}",
            CLUSTER_ID: IasZone.cluster_id,
        },
        (SHORT_PRESS, BTN_2): {
            COMMAND: f"{BUTTON_2}_{COMMAND_PRESS}",
            CLUSTER_ID: IasZone.cluster_id,
        },
        (DOUBLE_PRESS, BTN_2): {
            COMMAND: f"{BUTTON_2}_{COMMAND_DOUBLE}",
            CLUSTER_ID: IasZone.cluster_id,
        },
        (LONG_PRESS, BTN_2): {
            COMMAND: f"{BUTTON_2}_{COMMAND_HOLD}",
            CLUSTER_ID: IasZone.cluster_id,
        },
        (SHORT_PRESS, BTN_3): {
            COMMAND: f"{BUTTON_3}_{COMMAND_PRESS}",
            CLUSTER_ID: IasZone.cluster_id,
        },
        (DOUBLE_PRESS, BTN_3): {
            COMMAND: f"{BUTTON_3}_{COMMAND_DOUBLE}",
            CLUSTER_ID: IasZone.cluster_id,
        },
        (LONG_PRESS, BTN_3): {
            COMMAND: f"{BUTTON_3}_{COMMAND_HOLD}",
            CLUSTER_ID: IasZone.cluster_id,
        },
        (SHORT_PRESS, BTN_4): {
            COMMAND: f"{BUTTON_4}_{COMMAND_PRESS}",
            CLUSTER_ID: IasZone.cluster_id,
        },
        (DOUBLE_PRESS, BTN_4): {
            COMMAND: f"{BUTTON_4}_{COMMAND_DOUBLE}",
            CLUSTER_ID: IasZone.cluster_id,
        },
        (LONG_PRESS, BTN_4): {
            COMMAND: f"{BUTTON_4}_{COMMAND_HOLD}",
            CLUSTER_ID: IasZone.cluster_id,
        },
    }
