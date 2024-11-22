import pytest
from unittest.mock import MagicMock
from zhaquirks.linxura import LinxuraIASCluster, STATUS_REPORT, BUTTON_1, BUTTON_2, BUTTON_3, BUTTON_4
from zhaquirks.const import COMMAND_PRESS, COMMAND_DOUBLE, COMMAND_HOLD

@pytest.fixture
def linxura_cluster():
    """Fixture to create a LinxuraIASCluster instance."""
    cluster = LinxuraIASCluster(endpoint=None, is_server=True)
    cluster.listener_event = MagicMock()
    return cluster

@pytest.mark.parametrize(
    "value, expected_button, expected_press_type",
    [
        (1, BUTTON_1, COMMAND_PRESS),
        (3, BUTTON_1, COMMAND_DOUBLE),
        (5, BUTTON_1, COMMAND_HOLD),
        (7, BUTTON_2, COMMAND_PRESS),
        (9, BUTTON_2, COMMAND_DOUBLE),
        (11, BUTTON_2, COMMAND_HOLD),
        (13, BUTTON_3, COMMAND_PRESS),
        (15, BUTTON_3, COMMAND_DOUBLE),
        (17, BUTTON_3, COMMAND_HOLD),
        (19, BUTTON_4, COMMAND_PRESS),
        (21, BUTTON_4, COMMAND_DOUBLE),
        (23, BUTTON_4, COMMAND_HOLD),
    ],
)
def test_update_attribute(linxura_cluster, value, expected_button, expected_press_type):
    """Test _update_attribute for STATUS_REPORT."""
    linxura_cluster._update_attribute(STATUS_REPORT, value)
    
    action = f"{expected_button}_{expected_press_type}"
    event_args = {
        "button": expected_button,
        "press_type": expected_press_type,
        "command_id": 10,
    }

    # Check if listener_event was called correctly
    linxura_cluster.listener_event.assert_called_once_with(
        "zha_send_event", action, event_args
    )
