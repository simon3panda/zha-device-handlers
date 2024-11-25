"""Tests for Linxura quirks."""

from unittest import mock

import pytest
from zigpy.zcl.clusters.security import IasZone

from tests.common import ClusterListener
import zhaquirks
import zhaquirks.linxura

zhaquirks.setup()


@pytest.mark.parametrize("value", (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23))
async def test_button_ias(zigpy_device_from_quirk, value):
    """Test Linxura button remotes."""

    device = zigpy_device_from_quirk(zhaquirks.linxura.button.LinxuraButton)
    cluster = device.endpoints[1].ias_zone
    ias_zone_listener = ClusterListener(cluster)
    ias_zone_status_attr_id = IasZone.AttributeDefs.zone_status.id

    # button press
    cluster.update_attribute(ias_zone_status_attr_id, value)

    # ZHA calls update_attribute on the IasZone cluster when it receives a status_change_notification
    assert len(ias_zone_listener.attribute_updates) == 1
    assert ias_zone_listener.attribute_updates[0][0] == ias_zone_status_attr_id
    assert ias_zone_listener.attribute_updates[0][1] == value


@pytest.mark.parametrize("quirk", (zhaquirks.linxura.button.LinxuraButton,))
async def test_button_edge_case_request(zigpy_device_from_quirk, quirk):
    """Test button edge case."""

    device = zigpy_device_from_quirk(quirk)
    cluster = device.endpoints[1].ias_zone
    ias_zone_listener = ClusterListener(cluster)
    ias_zone_status_attr_id = IasZone.AttributeDefs.zone_status.id

    cluster.update_attribute(ias_zone_status_attr_id, 4)
    # No update should occur for state >= 4
    assert len(ias_zone_listener.attribute_updates) == 1


@pytest.mark.parametrize(
    "message, button, press_type",
    [
        (
            b"\x18\n\n\x02\x00\x19\x01\x00\xfe\xff0\x01",
            "button_1",
            "remote_button_short_press",
        ),
        (
            b"\x18\n\n\x02\x00\x19\x03\x00\xfe\xff0\x01",
            "button_1",
            "remote_button_double_press",
        ),
        (
            b"\x18\n\n\x02\x00\x19\x05\x00\xfe\xff0\x01",
            "button_1",
            "remote_button_long_press",
        ),
        (
            b"\x18\n\n\x02\x00\x19\x07\x00\xfe\xff0\x01",
            "button_2",
            "remote_button_short_press",
        ),
        (
            b"\x18\n\n\x02\x00\x19\x09\x00\xfe\xff0\x01",
            "button_2",
            "remote_button_double_press",
        ),
        (
            b"\x18\n\n\x02\x00\x19\x0b\x00\xfe\xff0\x01",
            "button_2",
            "remote_button_long_press",
        ),
        (
            b"\x18\n\n\x02\x00\x19\x0d\x00\xfe\xff0\x01",
            "button_3",
            "remote_button_short_press",
        ),
        (
            b"\x18\n\n\x02\x00\x19\x0f\x00\xfe\xff0\x01",
            "button_3",
            "remote_button_double_press",
        ),
        (
            b"\x18\n\n\x02\x00\x19\x11\x00\xfe\xff0\x01",
            "button_3",
            "remote_button_long_press",
        ),
        (
            b"\x18\n\n\x02\x00\x19\x13\x00\xfe\xff0\x01",
            "button_4",
            "remote_button_short_press",
        ),
        (
            b"\x18\n\n\x02\x00\x19\x15\x00\xfe\xff0\x01",
            "button_4",
            "remote_button_double_press",
        ),
        (
            b"\x18\n\n\x02\x00\x19\x17\x00\xfe\xff0\x01",
            "button_4",
            "remote_button_long_press",
        ),
    ],
)
async def test_button_triggers(zigpy_device_from_quirk, message, button, press_type):
    """Test ZHA_SEND_EVENT case."""
    listener = mock.MagicMock()
    device = zigpy_device_from_quirk(zhaquirks.linxura.button.LinxuraButton)
    cluster = device.endpoints[1].ias_zone
    cluster.add_listener(listener)

    device.handle_message(260, cluster.cluster_id, 1, 1, message)
    assert listener.zha_send_event.call_count == 1
    assert listener.zha_send_event.call_args == mock.call(
        f"{button}_{press_type}",
        {
            "button": button,
            "press_type": press_type,
            "command_id": 10,
        },
    )
