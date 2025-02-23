from enum import Enum


class Danger(Enum):

    man = 1
    woman = 0


class Role(Enum):

    GENERAL = "general"
    DESIGNER = "designer"
    ADMINISTRATOR = "administrator"


class DesignerApplicationStatus(Enum):

    WAIT_APPROVAL = "wait_approval"
    PASS = "pass"
    REFUSE = "refuse"
