"""Tests for Linxura quirks."""

import pytest
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
