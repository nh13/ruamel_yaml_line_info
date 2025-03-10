import math
import textwrap
from typing import Any
from typing import Optional

import pytest
import ruamel

import ruamel_yaml_line_info
from ruamel_yaml_line_info import YAML
from ruamel_yaml_line_info.constructor import DoubleQuotedScalarString
from ruamel_yaml_line_info.constructor import FoldedScalarString
from ruamel_yaml_line_info.constructor import HexCapsInt
from ruamel_yaml_line_info.constructor import HexInt
from ruamel_yaml_line_info.constructor import LiteralScalarString
from ruamel_yaml_line_info.constructor import OctalInt
from ruamel_yaml_line_info.constructor import PlainScalarString
from ruamel_yaml_line_info.constructor import ScalarFloat
from ruamel_yaml_line_info.constructor import ScalarInt
from ruamel_yaml_line_info.constructor import SingleQuotedScalarString


def _assert_line_col(node: Any, line: int, col: int, value: Any, typ: Optional[Any] = None) -> None:
    assert hasattr(node, "lc")
    assert node.lc.line == line
    assert node.lc.col == col
    if isinstance(value, float) and math.isnan(value):
        assert math.isnan(node)
    else:
        assert node == value
    if typ is not None:
        assert isinstance(node, typ), type(node)


def _round_trip_load(
    text: Any,
    preserve_quotes: Optional[bool] = None,
    version: Optional[Any] = None,
) -> Any:
    text = textwrap.dedent(text)
    yaml = YAML(typ="rt")
    yaml.preserve_quotes = preserve_quotes
    yaml.version = version
    return yaml.load(text)


def test_basic() -> None:
    """Tests basic parsing and line numbers."""
    text = """\
        foo: bar
        block: >
          this is not
          a multiline
          block
        single_quote: 'single'
        double_quote: "double"
        multi: |
          this really
          is a multiline
          block
        plain: vanilla
        first_int: 1
        second_int: 2
        ints:
          canonical: 685230
          decimal: +685_230
          octal: 0o2472256
          hexadecimal_upper: 0x_0A_74_AE
          hexadecimal_lower: 0x_0a_74_ae
          binary: 0b1010_0111_0100_1010_1110
        first_float: 1.2
        second_float: 4.3
        floats:
            canonical: 1.23015e+3
            exponential: 12.3015e+02
            fixed: 1230.15
            neginf: -.inf
            nan: .NaN
        bool_true: true
        bool_false: false
        """
    yaml = _round_trip_load(text, preserve_quotes=True)

    # strings
    _assert_line_col(yaml["foo"], line=0, col=5, value="bar", typ=PlainScalarString)
    _assert_line_col(
        yaml["block"],
        line=1,
        col=7,
        value="this is not a multiline block\n",
        typ=FoldedScalarString,
    )
    _assert_line_col(
        yaml["single_quote"], line=5, col=14, value="single", typ=SingleQuotedScalarString
    )
    _assert_line_col(
        yaml["double_quote"], line=6, col=14, value="double", typ=DoubleQuotedScalarString
    )
    _assert_line_col(
        yaml["multi"],
        line=7,
        col=7,
        value="this really\nis a multiline\nblock\n",
        typ=LiteralScalarString,
    )
    _assert_line_col(yaml["plain"], line=11, col=7, value="vanilla", typ=PlainScalarString)

    # integers
    _assert_line_col(yaml["first_int"], line=12, col=11, value=1, typ=ScalarInt)
    _assert_line_col(yaml["second_int"], line=13, col=12, value=2, typ=ScalarInt)
    _assert_line_col(yaml["ints"]["canonical"], line=15, col=13, value=685230, typ=ScalarInt)
    _assert_line_col(yaml["ints"]["decimal"], line=16, col=11, value=685230, typ=ScalarInt)
    _assert_line_col(yaml["ints"]["octal"], line=17, col=9, value=685230, typ=OctalInt)
    _assert_line_col(
        yaml["ints"]["hexadecimal_upper"], line=18, col=21, value=685230, typ=HexCapsInt
    )
    _assert_line_col(yaml["ints"]["hexadecimal_lower"], line=19, col=21, value=685230, typ=HexInt)
    _assert_line_col(yaml["ints"]["binary"], line=20, col=10, value=685230)

    # floats (these will all be floats or ScalarFloats)
    _assert_line_col(yaml["first_float"], line=21, col=13, value=1.2, typ=float)
    _assert_line_col(yaml["second_float"], line=22, col=14, value=4.3, typ=float)
    _assert_line_col(yaml["floats"]["canonical"], line=24, col=15, value=1.23015e3, typ=ScalarFloat)
    _assert_line_col(
        yaml["floats"]["exponential"], line=25, col=17, value=12.3015e02, typ=ScalarFloat
    )
    _assert_line_col(yaml["floats"]["fixed"], line=26, col=11, value=1230.15, typ=ScalarFloat)
    _assert_line_col(
        yaml["floats"]["neginf"], line=27, col=12, value=float("-inf"), typ=ScalarFloat
    )
    _assert_line_col(yaml["floats"]["nan"], line=28, col=9, value=float("nan"), typ=ScalarFloat)

    # booleans
    _assert_line_col(yaml["bool_true"], line=29, col=11, value=True)
    _assert_line_col(yaml["bool_false"], line=30, col=12, value=False)


# from PyYAML docs
class _Dice(tuple):
    def __new__(cls, a: int, b: int) -> "_Dice":
        return tuple.__new__(cls, [a, b])

    def __repr__(self) -> str:
        return "_Dice(%s,%s)" % self


def _dice_constructor(loader: Any, node: Any) -> _Dice:
    value = loader.construct_scalar(node)
    a, b = map(int, value.split("d"))
    return _Dice(a, b)


def test_dice_constructor() -> None:
    """Tests using a loader and custom constructor."""
    import ruamel.yaml  # NOQA

    with pytest.warns(PendingDeprecationWarning):
        yaml = ruamel.yaml.YAML(typ="unsafe", pure=True)
    ruamel.yaml.add_constructor("!dice", _dice_constructor)
    data = yaml.load("initial hit points: !dice 8d4")
    assert str(data) == "{'initial hit points': _Dice(8,4)}"


class _RoundTripLoader(
    ruamel.yaml.reader.Reader,
    ruamel.yaml.scanner.RoundTripScanner,
    ruamel.yaml.parser.RoundTripParser,
    ruamel.yaml.composer.Composer,
    ruamel_yaml_line_info.constructor.RoundTripConstructor,
    ruamel.yaml.resolver.VersionedResolver,
):
    def __init__(
        self,
        stream: Any,
        version: Optional[Any] = None,
        preserve_quotes: Optional[bool] = None,
    ) -> None:
        self.comment_handling = None  # issue 385
        ruamel.yaml.reader.Reader.__init__(self, stream, loader=self)
        ruamel.yaml.scanner.RoundTripScanner.__init__(self, loader=self)
        ruamel.yaml.parser.RoundTripParser.__init__(self, loader=self)
        ruamel.yaml.composer.Composer.__init__(self, loader=self)
        ruamel_yaml_line_info.RoundTripConstructor.__init__(
            self, preserve_quotes=preserve_quotes, loader=self
        )
        ruamel.yaml.resolver.VersionedResolver.__init__(self, version, loader=self)


def test_dice_constructor_with_loader() -> None:
    """Tests using a loader and custom constructor."""
    yaml = ruamel_yaml_line_info.YAML(typ="rt", pure=True)
    ruamel_yaml_line_info.constructor.RoundTripConstructor.add_constructor(
        "!dice",
        _dice_constructor,
    )
    data = yaml.load("initial hit points: !dice 8d4  # some comment")
    assert str(data) == "{'initial hit points': _Dice(8,4)}"
    value = data["initial hit points"]
    assert value == _Dice(8, 4)


def test_comment() -> None:
    """Tests using a loader and custom constructor."""
    yaml = ruamel_yaml_line_info.YAML(typ="rt", pure=True)
    data = yaml.load("foo:\n  # some comment\n  bar: cow\n")
    assert str(data) == "{'foo': {'bar': 'cow'}}"
    assert data["foo"].ca.comment[1][0].value == "# some comment\n"
