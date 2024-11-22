"""Tests for Linxura quirks."""

import pytest
from zigpy.zcl.clusters.security import IasZone
from zigpy.zcl.foundation import ZCLHeader

from tests.common import ClusterListener
import zhaquirks
import zhaquirks.linxura

zhaquirks.setup()


@pytest.mark.parametrize("quirk", (zhaquirks.linxura.button.LinxuraButton,))
async def test_Linxura_button(zigpy_device_from_quirk, quirk):
    """Test Linxura button remotes."""

    device = zigpy_device_from_quirk(quirk)

    # endpoint 1
    cluster = device.endpoints[1].ias_zone
    ias_zone_listener = ClusterListener(cluster)
    ias_zone_status_attr_id = IasZone.AttributeDefs.zone_status.id

    # ZHA calls update_attribute on the IasZone cluster when it receives a status_change_notification
    cluster.update_attribute(ias_zone_status_attr_id, 1)

    # button 1 single press
    assert len(ias_zone_listener.attribute_updates) == 1
    assert ias_zone_listener.attribute_updates[0][0] == ias_zone_status_attr_id
    assert ias_zone_listener.attribute_updates[0][1] == 1

    # button1 double press
    # ZHA calls update_attribute on the IasZone cluster when it receives a status_change_notification
    cluster.update_attribute(ias_zone_status_attr_id, 3)

    # button 1 double press
    assert len(ias_zone_listener.attribute_updates) == 2
    assert ias_zone_listener.attribute_updates[1][0] == ias_zone_status_attr_id
    assert ias_zone_listener.attribute_updates[1][1] == 3

    # button1 long press
    # ZHA calls update_attribute on the IasZone cluster when it receives a status_change_notification
    cluster.update_attribute(ias_zone_status_attr_id, 5)

    # button 1 long press
    assert len(ias_zone_listener.attribute_updates) == 3
    assert ias_zone_listener.attribute_updates[2][0] == ias_zone_status_attr_id
    assert ias_zone_listener.attribute_updates[2][1] == 5





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
