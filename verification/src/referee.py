from checkio_referee import RefereeBase
from checkio_referee import covercodes


import settings_env
from tests import TESTS


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "clock_angle"
    ENV_COVERCODE = {
        "python_2": covercodes.py_2_str,
        "python_3": None,
        "javascript": None
    }
