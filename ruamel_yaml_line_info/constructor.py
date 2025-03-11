from typing import Any
from typing import ClassVar
from typing import Optional
from typing import Union

import ruamel.yaml

__all__ = [
    "ScalarBoolean",
    "LiteralScalarString",
    "FoldedScalarString",
    "SingleQuotedScalarString",
    "DoubleQuotedScalarString",
    "PlainScalarString",
    # PreservedScalarString is the old name, as it was the first to be preserved on rt,
    # use LiteralScalarString instead
    "PreservedScalarString",
    "ScalarInt",
    "BinaryInt",
    "OctalInt",
    "HexInt",
    "HexCapsInt",
    "ScalarFloat",
    # Thes are not actually used by ruamel.yaml
    # "DecimalInt",
    # "ExponentialFloat",
    # "ExponentialCapsFloat",
]


class LiteralScalarString(ruamel.yaml.scalarstring.LiteralScalarString):
    """Sub-class of ruamel.yaml.scalarstring.LiteralScalarString to store line numbers."""

    __slots__ = ("comment", "lc")

    def __new__(cls, *args: Any, **kw: Any) -> Any:
        """Constructs a new class instance with the `lc` attribute (`LineCol`)."""
        ret_val = super().__new__(cls, *args, **kw)
        ret_val.lc = None
        return ret_val


class FoldedScalarString(ruamel.yaml.scalarstring.FoldedScalarString):
    """Sub-class of ruamel.yaml.scalarstring.FoldedScalarString to store line numbers."""

    __slots__ = ("fold_pos", "comment", "lc")

    def __new__(cls, *args: Any, **kw: Any) -> Any:
        """Constructs a new class instance with the `lc` attribute (`LineCol`)."""
        ret_val = super().__new__(cls, *args, **kw)
        ret_val.lc = None
        return ret_val


class DoubleQuotedScalarString(ruamel.yaml.scalarstring.DoubleQuotedScalarString):
    """Sub-class of ruamel.yaml.scalarstring.DoubleQuotedScalarString to store line numbers."""

    __slots__ = "lc"

    def __new__(cls, *args: Any, **kw: Any) -> Any:
        """Constructs a new class instance with the `lc` attribute (`LineCol`)."""
        ret_val = super().__new__(cls, *args, **kw)
        ret_val.lc = None
        return ret_val


class SingleQuotedScalarString(ruamel.yaml.scalarstring.SingleQuotedScalarString):
    """Sub-class of ruamel.yaml.scalarstring.SingleQuotedScalarString to store line numbers."""

    __slots__ = "lc"

    def __new__(cls, *args: Any, **kw: Any) -> Any:
        """Constructs a new class instance with the `lc` attribute (`LineCol`)."""
        ret_val = super().__new__(cls, *args, **kw)
        ret_val.lc = None
        return ret_val


class PlainScalarString(ruamel.yaml.scalarstring.PlainScalarString):
    """Sub-class of ruamel.yaml.scalarstring.PlainScalarString to store line numbers."""

    __slots__ = "lc"

    def __new__(cls, *args: Any, **kw: Any) -> Any:
        """Constructs a new class instance with the `lc` attribute (`LineCol`)."""
        ret_val = super().__new__(cls, *args, **kw)
        ret_val.lc = None
        return ret_val


PreservedScalarString = LiteralScalarString


class ScalarInt(ruamel.yaml.scalarint.ScalarInt):
    """Sub-class of ruamel.yaml.scalarint.ScalarInt to store line numbers."""

    def __new__(cls, *args: Any, **kw: Any) -> Any:
        """Constructs a new class instance with the `lc` attribute (`LineCol`)."""
        ret_val = super().__new__(cls, *args, **kw)
        ret_val.lc = None
        return ret_val


class BinaryInt(ruamel.yaml.scalarint.BinaryInt):
    """Sub-class of ruamel.yaml.scalarint.BinaryInt to store line numbers."""

    def __new__(cls, *args: Any, **kw: Any) -> Any:
        """Constructs a new class instance with the `lc` attribute (`LineCol`)."""
        ret_val = super().__new__(cls, *args, **kw)
        ret_val.lc = None
        return ret_val


class OctalInt(ruamel.yaml.scalarint.OctalInt):
    """Sub-class of ruamel.yaml.scalarint.OctalInt to store line numbers."""

    def __new__(cls, *args: Any, **kw: Any) -> Any:
        """Constructs a new class instance with the `lc` attribute (`LineCol`)."""
        ret_val = super().__new__(cls, *args, **kw)
        ret_val.lc = None
        return ret_val


class HexInt(ruamel.yaml.scalarint.HexInt):
    """Sub-class of ruamel.yaml.scalarint.HexInt to store line numbers."""

    def __new__(cls, *args: Any, **kw: Any) -> Any:
        """Constructs a new class instance with the `lc` attribute (`LineCol`)."""
        ret_val = super().__new__(cls, *args, **kw)
        ret_val.lc = None
        return ret_val


class HexCapsInt(ruamel.yaml.scalarint.HexCapsInt):
    """Sub-class of ruamel.yaml.scalarint.HexCapsInt to store line numbers."""

    def __new__(cls, *args: Any, **kw: Any) -> Any:
        """Constructs a new class instance with the `lc` attribute (`LineCol`)."""
        ret_val = super().__new__(cls, *args, **kw)
        ret_val.lc = None
        return ret_val


# class DecimalInt(ruamel.yaml.scalarint.DecimalInt):
#    """Sub-class of ruamel.yaml.scalarint.DecimalInt to store line numbers."""
#
#    def __new__(cls, *args: Any, **kw: Any) -> Any:
#        """Constructs a new class instance with the `lc` attribute (`LineCol`)."""
#        ret_val = super().__new__(cls, *args, **kw)
#        ret_val.lc = None
#        return ret_val


class ScalarBoolean(ruamel.yaml.scalarbool.ScalarBoolean):
    """Sub-class of ruamel.yaml.scalarbool.ScalarBoolean to store line numbers."""

    def __new__(cls, *args: Any, **kw: Any) -> Any:
        """Constructs a new class instance with the `lc` attribute (`LineCol`)."""
        ret_val = super().__new__(cls, *args, **kw)
        ret_val.lc = None
        return ret_val


class ScalarFloat(ruamel.yaml.scalarfloat.ScalarFloat):
    """Sub-class of to store line numbers."""

    def __new__(cls, *args: Any, **kw: Any) -> Any:
        """Constructs a new class instance with the `lc` attribute (`LineCol`)."""
        ret_val = super().__new__(cls, *args, **kw)
        ret_val.lc = None
        return ret_val


# class ExponentialFloat(ruamel.yaml.scalarfloat.ExponentialFloat):
#    """Sub-class of to store line numbers."""
#
#    def __new__(cls, *args: Any, **kw: Any) -> Any:
#        """Constructs a new class instance with the `lc` attribute (`LineCol`)."""
#        ret_val = super().__new__(cls, *args, **kw)
#        ret_val.lc = None
#        return ret_val
#
#
# class ExponentialCapsFloat(ruamel.yaml.scalarfloat.ExponentialCapsFloat):
#    """Sub-class of to store line numbers."""
#
#    def __new__(cls, *args: Any, **kw: Any) -> Any:
#        """Constructs a new class instance with the `lc` attribute (`LineCol`)."""
#        ret_val = super().__new__(cls, *args, **kw)
#        ret_val.lc = None
#        return ret_val


StyledScalarString = Union[
    "LiteralScalarString",
    "FoldedScalarString",
    "DoubleQuotedScalarString",
    "SingleQuotedScalarString",
    "PlainScalarString",
    "PreservedScalarString",
]


class RoundTripConstructor(ruamel.yaml.constructor.RoundTripConstructor):
    """
    Round trip constructor that keeps line numbers for most elements.

    Adapted from: https://stackoverflow.com/questions/45716281/parsing-yaml-get-line-numbers-even-in-ordered-maps
    """

    def __init__(self, preserve_quotes: Union[None, bool] = None, loader: Any = None) -> None:
        super().__init__(preserve_quotes=preserve_quotes, loader=loader)
        if not hasattr(self.loader, "comment_handling"):
            self.loader.comment_handling = None

    def _update_lc(self, node: ruamel.yaml.ScalarNode, value: Any) -> None:
        value.lc = ruamel.yaml.comments.LineCol()
        value.lc.line = node.start_mark.line
        value.lc.col = node.start_mark.column

    def _construct_literal_scalar_string(
        self, node: ruamel.yaml.nodes.ScalarNode
    ) -> LiteralScalarString:
        lss = LiteralScalarString(value=node.value, anchor=node.anchor)
        if self.loader and self.loader.comment_handling is None:
            if node.comment and node.comment[1]:
                lss.comment = node.comment[1][0]  # type: ignore[attr-defined]
        else:
            # NEWCMNT
            if node.comment is not None and node.comment[1]:
                # nprintf('>>>>nc1', node.comment)
                # EOL comment after |
                lss.comment = self.comment(node.comment[1][0])  # type: ignore[attr-defined]
        return lss

    def _construct_folded_scalar_string(
        self, node: ruamel.yaml.nodes.ScalarNode
    ) -> FoldedScalarString:
        fold_positions: list[int] = []
        idx = -1
        while True:
            idx = node.value.find("\a", idx + 1)
            if idx < 0:
                break
            fold_positions.append(idx - len(fold_positions))
        fss = FoldedScalarString(value=node.value.replace("\a", ""), anchor=node.anchor)
        if self.loader and self.loader.comment_handling is None:
            if node.comment and node.comment[1]:
                fss.comment = node.comment[1][0]  # type: ignore[attr-defined]
        else:
            # NEWCMNT
            if node.comment is not None and node.comment[1]:
                # nprintf('>>>>nc2', node.comment)
                # EOL comment after >
                fss.comment = self.comment(node.comment[1][0])  # type: ignore[attr-defined]
        if fold_positions:
            fss.fold_pos = fold_positions  # type: ignore[attr-defined]
        return fss

    def construct_scalar(
        self, node: ruamel.yaml.nodes.ScalarNode
    ) -> ruamel.yaml.scalarstring.ScalarString:
        ret_val: Optional[StyledScalarString] = None
        if node.style == "|" and isinstance(node.value, str):
            ret_val = self._construct_literal_scalar_string(node)
        elif node.style == ">" and isinstance(node.value, str):
            ret_val = self._construct_folded_scalar_string(node)
        elif bool(self._preserve_quotes) and isinstance(node.value, str):
            if node.style == "'":
                ret_val = SingleQuotedScalarString(value=node.value, anchor=node.anchor)
            if node.style == '"':
                ret_val = DoubleQuotedScalarString(value=node.value, anchor=node.anchor)
        if ret_val is None:
            if node.anchor is not None:
                ret_val = PlainScalarString(value=node.value, anchor=node.anchor)
            else:
                ret_val = PlainScalarString(value=node.value)
        self._update_lc(node, ret_val)
        return ret_val

    _INT_CLASS_MAP: ClassVar = {
        ruamel.yaml.scalarint.BinaryInt: BinaryInt,
        ruamel.yaml.scalarint.OctalInt: OctalInt,
        ruamel.yaml.scalarint.HexInt: HexInt,
        ruamel.yaml.scalarint.HexCapsInt: HexCapsInt,
        # ruamel.yaml.scalarint.DecimalInt: DecimalInt,
        # this needs to be last as the other classes above are sub-classes
        ruamel.yaml.scalarint.ScalarInt: ScalarInt,
    }

    def construct_yaml_int(self, node: ruamel.yaml.ScalarNode) -> Any:
        super_value = super().construct_yaml_int(node)
        ret_val: Optional[Union[int, ruamel.yaml.scalarint.ScalarInt]] = None
        for src_clazz, dst_clazz in self._INT_CLASS_MAP.items():
            if isinstance(super_value, src_clazz):
                ret_val = dst_clazz(super_value, anchor=node.anchor)
                break
        else:
            ret_val = ScalarInt(super_value, anchor=node.anchor)
        if isinstance(super_value, ruamel.yaml.scalarint.ScalarInt):
            ret_val.__dict__.update(super_value.__dict__)
        self._update_lc(node, ret_val)
        assert ret_val is not None  # for the type checker
        return ret_val

    _FLOAT_CLASS_MAP: ClassVar = {
        # ruamel.yaml.scalarfloat.ExponentialFloat: ExponentialFloat,
        # ruamel.yaml.scalarfloat.ExponentialCapsFloat: ExponentialCapsFloat,
        # this needs to be last as the other classes above are sub-classes
        ruamel.yaml.scalarfloat.ScalarFloat: ScalarFloat,
    }

    def construct_yaml_float(self, node: ruamel.yaml.ScalarNode) -> Union[float, ScalarFloat]:
        super_value: Union[float, ruamel.yaml.scalarfloat.ScalarFloat] = (
            super().construct_yaml_float(node)
        )
        ret_val: Optional[Union[float, ruamel.yaml.scalarfloat.ScalarFloat]] = None
        for src_clazz, dst_clazz in self._FLOAT_CLASS_MAP.items():
            if isinstance(super_value, src_clazz):
                ret_val = dst_clazz(super_value, anchor=node.anchor)
                break
        else:
            ret_val = ScalarFloat(super_value, anchor=node.anchor)
        if isinstance(super_value, ruamel.yaml.scalarfloat.ScalarFloat):
            ret_val.__dict__.update(super_value.__dict__)
        assert ret_val is not None  # for the type checker
        self._update_lc(node, ret_val)
        return ret_val

    def construct_yaml_bool(self, node: ruamel.yaml.ScalarNode) -> ScalarBoolean:  # type: ignore[explicit-override, override]
        super_value: Union[bool, ruamel.yaml.scalarbool.ScalarBoolean] = (
            super().construct_yaml_bool(node)
        )
        ret_val: ScalarBoolean = ScalarBoolean(super_value, anchor=node.anchor)
        if isinstance(super_value, ruamel.yaml.scalarbool.ScalarBoolean):
            ret_val.__dict__.update(super_value.__dict__)
        self._update_lc(node, ret_val)
        return ret_val
