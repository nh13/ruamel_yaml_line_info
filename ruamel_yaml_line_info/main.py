from typing import Any
from typing import List
from typing import Optional
from typing import Text
from typing import Union

import ruamel.yaml
from ruamel.yaml.representer import RoundTripRepresenter

from ruamel_yaml_line_info.constructor import BinaryInt
from ruamel_yaml_line_info.constructor import DoubleQuotedScalarString
from ruamel_yaml_line_info.constructor import FoldedScalarString
from ruamel_yaml_line_info.constructor import HexCapsInt
from ruamel_yaml_line_info.constructor import HexInt
from ruamel_yaml_line_info.constructor import LiteralScalarString
from ruamel_yaml_line_info.constructor import OctalInt
from ruamel_yaml_line_info.constructor import PlainScalarString
from ruamel_yaml_line_info.constructor import RoundTripConstructor
from ruamel_yaml_line_info.constructor import ScalarBoolean
from ruamel_yaml_line_info.constructor import ScalarFloat
from ruamel_yaml_line_info.constructor import ScalarInt
from ruamel_yaml_line_info.constructor import SingleQuotedScalarString


class YAML(ruamel.yaml.YAML):
    """Subclass of ruamel.yaml.YAML that keeps line numbers."""

    def __init__(
        self: Any,
        *,
        typ: Optional[Union[List[Text], Text]] = None,
        pure: Any = False,
        output: Any = None,
        plug_ins: Any = None,
    ) -> None:  # input=None,
        """Alternative constructor to ruamel.yaml.YAML that keeps line numbers."""
        super().__init__(typ=typ, pure=pure, output=output, plug_ins=plug_ins)
        YAML.with_line_numbers(yaml=self)

    @classmethod
    def with_line_numbers(cls, yaml: ruamel.yaml.YAML) -> ruamel.yaml.YAML:
        """Updates a ruamel.yaml.YAML instance to keep line numbers."""
        yaml.Constructor = RoundTripConstructor

        # re-add so that we override the parent class' default constructor
        yaml.Constructor.add_default_constructor("int")
        yaml.Constructor.add_default_constructor("float")
        yaml.Constructor.add_default_constructor("bool")

        # needed for representers
        RoundTripRepresenter.add_representer(
            LiteralScalarString,
            RoundTripRepresenter.represent_literal_scalarstring,
        )
        RoundTripRepresenter.add_representer(
            FoldedScalarString, RoundTripRepresenter.represent_folded_scalarstring
        )
        RoundTripRepresenter.add_representer(
            SingleQuotedScalarString,
            RoundTripRepresenter.represent_single_quoted_scalarstring,
        )
        RoundTripRepresenter.add_representer(
            DoubleQuotedScalarString,
            RoundTripRepresenter.represent_double_quoted_scalarstring,
        )
        RoundTripRepresenter.add_representer(
            PlainScalarString, RoundTripRepresenter.represent_plain_scalarstring
        )
        RoundTripRepresenter.add_representer(ScalarInt, RoundTripRepresenter.represent_scalar_int)
        RoundTripRepresenter.add_representer(BinaryInt, RoundTripRepresenter.represent_binary_int)
        RoundTripRepresenter.add_representer(OctalInt, RoundTripRepresenter.represent_octal_int)
        RoundTripRepresenter.add_representer(HexInt, RoundTripRepresenter.represent_hex_int)
        RoundTripRepresenter.add_representer(
            HexCapsInt, RoundTripRepresenter.represent_hex_caps_int
        )
        RoundTripRepresenter.add_representer(
            ScalarFloat, RoundTripRepresenter.represent_scalar_float
        )
        # RoundTripRepresenter.add_representer(
        #    ExponentialFloat, RoundTripRepresenter.represent_scalar_float
        # )
        # RoundTripRepresenter.add_representer(
        #    ExponentialCapsFloat, RoundTripRepresenter.represent_scalar_float
        # )
        RoundTripRepresenter.add_representer(
            ScalarBoolean, RoundTripRepresenter.represent_scalar_bool
        )
        return yaml
