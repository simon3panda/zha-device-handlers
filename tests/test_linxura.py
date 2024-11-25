"""Tests for Linxura quirks."""

import pytest
from zigpy.zcl.clusters.security import IasZone

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

    # button 1 single press
    # ZHA calls update_attribute on the IasZone cluster when it receives a status_change_notification
    cluster.update_attribute(ias_zone_status_attr_id, 1)

    # button 1 single press
    assert len(ias_zone_listener.attribute_updates) == 1
    assert ias_zone_listener.attribute_updates[0][0] == ias_zone_status_attr_id
    assert ias_zone_listener.attribute_updates[0][1] == 1

    # button 1 double press
    # ZHA calls update_attribute on the IasZone cluster when it receives a status_change_notification
    cluster.update_attribute(ias_zone_status_attr_id, 3)

    # button 1 double press
    assert len(ias_zone_listener.attribute_updates) == 2
    assert ias_zone_listener.attribute_updates[1][0] == ias_zone_status_attr_id
    assert ias_zone_listener.attribute_updates[1][1] == 3

    # button 1 long press
    # ZHA calls update_attribute on the IasZone cluster when it receives a status_change_notification
    cluster.update_attribute(ias_zone_status_attr_id, 5)

    # button 1 long press
    assert len(ias_zone_listener.attribute_updates) == 3
    assert ias_zone_listener.attribute_updates[2][0] == ias_zone_status_attr_id
    assert ias_zone_listener.attribute_updates[2][1] == 5

    # button 2 single press
    # ZHA calls update_attribute on the IasZone cluster when it receives a status_change_notification
    cluster.update_attribute(ias_zone_status_attr_id, 7)

    # button 2 single press
    assert len(ias_zone_listener.attribute_updates) == 4
    assert ias_zone_listener.attribute_updates[3][0] == ias_zone_status_attr_id
    assert ias_zone_listener.attribute_updates[3][1] == 7

    # button 2 double press
    # ZHA calls update_attribute on the IasZone cluster when it receives a status_change_notification
    cluster.update_attribute(ias_zone_status_attr_id, 9)

    # button 2 double press
    assert len(ias_zone_listener.attribute_updates) == 5
    assert ias_zone_listener.attribute_updates[4][0] == ias_zone_status_attr_id
    assert ias_zone_listener.attribute_updates[4][1] == 9

    # button 2 long press
    # ZHA calls update_attribute on the IasZone cluster when it receives a status_change_notification
    cluster.update_attribute(ias_zone_status_attr_id, 11)

    # button 2 long press
    assert len(ias_zone_listener.attribute_updates) == 6
    assert ias_zone_listener.attribute_updates[5][0] == ias_zone_status_attr_id
    assert ias_zone_listener.attribute_updates[5][1] == 11

    # button 3 single press
    # ZHA calls update_attribute on the IasZone cluster when it receives a status_change_notification
    cluster.update_attribute(ias_zone_status_attr_id, 13)

    # button 3 single press
    assert len(ias_zone_listener.attribute_updates) == 7
    assert ias_zone_listener.attribute_updates[6][0] == ias_zone_status_attr_id
    assert ias_zone_listener.attribute_updates[6][1] == 13

    # button 3 double press
    # ZHA calls update_attribute on the IasZone cluster when it receives a status_change_notification
    cluster.update_attribute(ias_zone_status_attr_id, 15)

    # button 3 double press
    assert len(ias_zone_listener.attribute_updates) == 8
    assert ias_zone_listener.attribute_updates[7][0] == ias_zone_status_attr_id
    assert ias_zone_listener.attribute_updates[7][1] == 15

    # button 3 long press
    # ZHA calls update_attribute on the IasZone cluster when it receives a status_change_notification
    cluster.update_attribute(ias_zone_status_attr_id, 17)

    # button 3 long press
    assert len(ias_zone_listener.attribute_updates) == 9
    assert ias_zone_listener.attribute_updates[8][0] == ias_zone_status_attr_id
    assert ias_zone_listener.attribute_updates[8][1] == 17

    # button 4 single press
    # ZHA calls update_attribute on the IasZone cluster when it receives a status_change_notification
    cluster.update_attribute(ias_zone_status_attr_id, 19)

    # button 4 single press
    assert len(ias_zone_listener.attribute_updates) == 10
    assert ias_zone_listener.attribute_updates[9][0] == ias_zone_status_attr_id
    assert ias_zone_listener.attribute_updates[9][1] == 19

    # button 4 double press
    # ZHA calls update_attribute on the IasZone cluster when it receives a status_change_notification
    cluster.update_attribute(ias_zone_status_attr_id, 21)

    # button 4 double press
    assert len(ias_zone_listener.attribute_updates) == 11
    assert ias_zone_listener.attribute_updates[10][0] == ias_zone_status_attr_id
    assert ias_zone_listener.attribute_updates[10][1] == 21

    # button 4 long press
    # ZHA calls update_attribute on the IasZone cluster when it receives a status_change_notification
    cluster.update_attribute(ias_zone_status_attr_id, 23)

    # button 4 long press
    assert len(ias_zone_listener.attribute_updates) == 12
    assert ias_zone_listener.attribute_updates[11][0] == ias_zone_status_attr_id
    assert ias_zone_listener.attribute_updates[11][1] == 23


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
