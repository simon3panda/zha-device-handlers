"""Tests for Linxura quirks."""

import pytest
from unittest import mock
from zigpy.zcl.clusters.security import IasZone
from tests.common import ClusterListener
import zhaquirks
import zhaquirks.linxura

zhaquirks.setup()


@pytest.mark.parametrize("value", (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23))
async def test_Linxura_button(zigpy_device_from_quirk, value):
    """Test Linxura button remotes."""

    device = zigpy_device_from_quirk(zhaquirks.linxura.button.LinxuraButton)

    # endpoint 1
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
async def test_Linxura_button_trigger(zigpy_device_from_quirk, quirk):
    """Test ZHA_SEND_EVENT case."""
    listener = mock.MagicMock()
    device = zigpy_device_from_quirk(zhaquirks.linxura.button.LinxuraButton)
    cluster = device.endpoints[1].ias_zone
    cluster.add_listener(listener)

    message = b'\x18\n\n\x02\x00\x19\x01\x00\xfe\xff0\x01'
    device.handle_message(260, cluster.cluster_id, 1, 1, message)
    assert listener.zha_send_event.call_count == 1
    assert listener.zha_send_event.call_args == mock.call(
        "button_1_remote_button_short_press", {"button": "button_1", "press_type": "remote_button_short_press", "command_id": 10}
    )

    message = b'\x18\n\n\x02\x00\x19\x03\x00\xfe\xff0\x01'
    listener.reset_mock()
    device.handle_message(260, cluster.cluster_id, 1, 1, message)
    assert listener.zha_send_event.call_count == 1
    assert listener.zha_send_event.call_args == mock.call(
        "button_1_remote_button_double_press", {"button": "button_1", "press_type": "remote_button_double_press", "command_id": 10}
    )

    message = b'\x18\n\n\x02\x00\x19\x05\x00\xfe\xff0\x01'
    listener.reset_mock()
    device.handle_message(260, cluster.cluster_id, 1, 1, message)
    assert listener.zha_send_event.call_count == 1
    assert listener.zha_send_event.call_args == mock.call(
        "button_1_remote_button_long_press", {"button": "button_1", "press_type": "remote_button_long_press", "command_id": 10}
    )

    message = b'\x18\n\n\x02\x00\x19\x07\x00\xfe\xff0\x01'
    listener.reset_mock()
    device.handle_message(260, cluster.cluster_id, 1, 1, message)
    assert listener.zha_send_event.call_count == 1
    assert listener.zha_send_event.call_args == mock.call(
        "button_2_remote_button_short_press", {"button": "button_2", "press_type": "remote_button_short_press", "command_id": 10}
    )

    message = b'\x18\n\n\x02\x00\x19\x09\x00\xfe\xff0\x01'
    listener.reset_mock()
    device.handle_message(260, cluster.cluster_id, 1, 1, message)
    assert listener.zha_send_event.call_count == 1
    assert listener.zha_send_event.call_args == mock.call(
        "button_2_remote_button_double_press", {"button": "button_2", "press_type": "remote_button_double_press", "command_id": 10}
    )

    message = b'\x18\n\n\x02\x00\x19\x0b\x00\xfe\xff0\x01'
    listener.reset_mock()
    device.handle_message(260, cluster.cluster_id, 1, 1, message)
    assert listener.zha_send_event.call_count == 1
    assert listener.zha_send_event.call_args == mock.call(
        "button_2_remote_button_long_press", {"button": "button_2", "press_type": "remote_button_long_press", "command_id": 10}
    )

    message = b'\x18\n\n\x02\x00\x19\x0d\x00\xfe\xff0\x01'
    listener.reset_mock()
    device.handle_message(260, cluster.cluster_id, 1, 1, message)
    assert listener.zha_send_event.call_count == 1
    assert listener.zha_send_event.call_args == mock.call(
        "button_3_remote_button_short_press", {"button": "button_3", "press_type": "remote_button_short_press", "command_id": 10}
    )

    message = b'\x18\n\n\x02\x00\x19\x0f\x00\xfe\xff0\x01'
    listener.reset_mock()
    device.handle_message(260, cluster.cluster_id, 1, 1, message)
    assert listener.zha_send_event.call_count == 1
    assert listener.zha_send_event.call_args == mock.call(
        "button_3_remote_button_double_press", {"button": "button_3", "press_type": "remote_button_double_press", "command_id": 10}
    )

    message = b'\x18\n\n\x02\x00\x19\x11\x00\xfe\xff0\x01'
    listener.reset_mock()
    device.handle_message(260, cluster.cluster_id, 1, 1, message)
    assert listener.zha_send_event.call_count == 1
    assert listener.zha_send_event.call_args == mock.call(
        "button_3_remote_button_long_press", {"button": "button_3", "press_type": "remote_button_long_press", "command_id": 10}
    )

    message = b'\x18\n\n\x02\x00\x19\x13\x00\xfe\xff0\x01'
    listener.reset_mock()
    device.handle_message(260, cluster.cluster_id, 1, 1, message)
    assert listener.zha_send_event.call_count == 1
    assert listener.zha_send_event.call_args == mock.call(
        "button_4_remote_button_short_press", {"button": "button_4", "press_type": "remote_button_short_press", "command_id": 10}
    )

    message = b'\x18\n\n\x02\x00\x19\x15\x00\xfe\xff0\x01'
    listener.reset_mock()
    device.handle_message(260, cluster.cluster_id, 1, 1, message)
    assert listener.zha_send_event.call_count == 1
    assert listener.zha_send_event.call_args == mock.call(
        "button_4_remote_button_double_press", {"button": "button_4", "press_type": "remote_button_double_press", "command_id": 10}
    )

    message = b'\x18\n\n\x02\x00\x19\x17\x00\xfe\xff0\x01'
    listener.reset_mock()
    device.handle_message(260, cluster.cluster_id, 1, 1, message)
    assert listener.zha_send_event.call_count == 1
    assert listener.zha_send_event.call_args == mock.call(
        "button_4_remote_button_long_press", {"button": "button_4", "press_type": "remote_button_long_press", "command_id": 10}
    )


@pytest.mark.parametrize("quirk", (zhaquirks.linxura.button.LinxuraButton,))
async def test_edge_case_request(zigpy_device_from_quirk, quirk):
    """Test edge case."""

    device = zigpy_device_from_quirk(quirk)

    # endpoint 1
    cluster = device.endpoints[1].ias_zone
    ias_zone_listener = ClusterListener(cluster)
    ias_zone_status_attr_id = IasZone.AttributeDefs.zone_status.id

    cluster.update_attribute(ias_zone_status_attr_id, 4)
    assert (
        len(ias_zone_listener.attribute_updates) == 1
    )  # No update should occur for state >= 4
