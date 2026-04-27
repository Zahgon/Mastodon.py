from __future__ import annotations # python < 3.9 compat
import typing
from typing import List, Union, Optional, Dict, Any, Tuple, Callable, get_type_hints, TypeVar, IO, Generic, ForwardRef
from datetime import datetime, timezone
import dateutil
import dateutil.parser
from collections import OrderedDict
from mastodon.compat import PurePath
import sys
import json
import copy

# A type representing a file name as a PurePath or string, or a file-like object, for convenience
PathOrFile = Union[str, PurePath, IO[bytes]]

BASE62_ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def base62_to_int(base62: str) -> int:
    """
    internal helper for *oma compat: convert a base62 string to an int since
    that is what that software uses as ID type.

    we don't convert IDs in general, but this is needed for snowflake ID
    calculations.
    """
    pass

def int_to_base62(val: int) -> str:
    """
    Internal helper to convert an int to a base62 string.
    """
    pass


PrimitiveIdType = Union[str, int]
"""
The base type for all non-snowflake IDs. This is a union of int and str 
because while Mastodon mostly uses IDs that are ints, it doesn't guarantee
this and other implementations do not use integer IDs.

In a change from previous versions, string IDs now take precedence over ints.
This is a breaking change, and I'm sorry about it, but this will make every piece
of software using Mastodon.py more robust in the long run.
"""

def _str_to_type(mastopy_type):
    """
    String name to internal type resolver
    """
    pass

class MaybeSnowflakeIdType(str):
    """
    Represents, maybe, a snowflake ID.

    Contains what a regular ID can contain (int or str) and will convert to int if
    containing an int or a str that naturally converts to an int (e.g. "123").

    Can *also* contain a *datetime* which gets converted to a  timestamp.

    It's also just *maybe* a snowflake ID, because some implementations may not use those.

    This may seem annoyingly complex, but the goal here is:
    1) If constructed with some ID, return that ID unchanged, so equality and hashing work
    2) Allow casting to int and str, just like a regular ID
    3) Halfway transparently convert to and from datetime with the correct format for the server we're talking to
    """
    def __new__(cls, value, *args, **kwargs):
        try:
            return super(cls, cls).__new__(cls, value)
        except:
            return object.__new__(cls)

    def __init__(self, val: Union[PrimitiveIdType, datetime], assume_pleroma: bool = False):
        try:
            super(MaybeSnowflakeIdType, self).__init__()
        except:
            pass
        if isinstance(val, (int, str)):
            self.__val = val
        elif isinstance(val, datetime):
            self.__val = (int(val.timestamp()) << 16) * 1000
            if assume_pleroma:
                self.__val = int_to_base62(self.__val)
        else:
            pass
        self.assume_pleroma = assume_pleroma
        
    def to_datetime(self) -> Optional[datetime]:
        """
        Convert to datetime. This *can* fail because not every implementation of
        the masto API is guaranteed to actually use snowflake IDs where masto uses
        snowflake IDs, so it can in fact return None.
        """
        pass

    def __str__(self) -> str:
        """
        Return as string representation.
        """
        return str(self.__val)

    def __int__(self) -> int:
        """
        Return as int representation.

        This is not guaranteed to work, because the ID might be a string,
        though on Mastodon it is generally going to be an int.
        """
        if isinstance(self.__val, str):
            return int(self.__val)
        return self.__val
    
    def __repr__(self) -> str:
        """
        Overriden so that the integer representation doesn't take precedence
        """
        return str(self.__val)

# Forward reference resolution for < 3.9
if sys.version_info < (3, 9):
    def resolve_type(t):
        # I'm sorry about this, but I cannot think of another way to make this work properly in versions below 3.9 that
        # cannot resolve forward references in a sane way
        pass
else:
    def resolve_type(t):
        pass

# Type to string that is more robust than repr
def stringify_type(tp):
    pass

# Function that gets a type class but doesn't break in lower python versions as much
def get_type_class(typ):
    pass

# Restore behaviour that was removed from python for mysterious reasons
def real_issubclass(type1, type2orig):
    pass

# Helper functions for typecasting attempts
def try_cast(t, value, retry = True, union_specializer = None):
    """
    Base case casting function. Handles:
    * Casting to any AttribAccessDict subclass (directly, no special handling)
    * Casting to bool (with possible conversion from json bool strings)
    * Casting to datetime (with possible conversion from all kinds of funny date formats because unfortunately this is the world we live in)
    * Casting to whatever t is
    * Trying once again to AttribAccessDict as a fallback
    Gives up and returns as-is if none of the above work.
    """
    pass

def try_cast_recurse(t, value, union_specializer=None):
    """
    Non-dict compound type casting function. Handles:
    * Casting to list, tuple, EntityList or (Non)PaginatableList, converting all elements to the correct type recursively
    * Casting to Union, use union_specializer to special case the union type to the correct one
    * Casting to Union, special case out Quote vs ShallowQuote by the presence of "quoted_status" or "quoted_status_id" in the value
    * Casting to Union, trying all types in the union until one works
    Gives up and returns as-is if none of the above work.
    """
    pass

class Entity():
    """
    Base class for everything returned by the API. This is a union of :class:`AttribAccessDict` and :class:`EntityList`.

    Defines two methods: to_json(), and (static) from_json(), for serializing and deserializing to/from JSON.
    """
    def __init__(self):
        self._mastopy_type = None
    
    def to_json(self, pretty=True) -> str:
        """
        Serialize to JSON.

        The returned JSON data includes type information and a version field.
        """
        def remove_renamed_fields(obj):
            pass
        def json_serial(obj):
            pass
        pass

    @staticmethod
    def from_json(json_str: str) -> Entity:
        """
        Deserialize from JSON.

        Parse a JSON string and cast to the to the appropriate type
        by using a special field that is added by serialization.

        This `should` be safe to call on any JSON string (no less safe than json.loads), 
        but I would still recommend to be very careful when using this on untrusted data 
        and to check that the returned value matches your expectations.

        There is currently a bug on specifically python 3.7 and 3.8 where the return value
        is not guaranteed to be of the right type. I will probably not fix this, since the versions
        are out of support, anyways. However, the data will still be loaded correctly.
        """
        pass


class PaginationInfo(OrderedDict):
    """
    Pagination info

    Not likely to change, but very much implementation (Mastodon.py) and implementation (Mastodon server) defined. It would be best
    if you treated this as opaque.
    """
    pass

IdType = Union[PrimitiveIdType, MaybeSnowflakeIdType, datetime]
"""
IDs returned from Mastodon.py ar either primitive (int or str) or snowflake
(still int or str, but potentially convertible to datetime), but also
a datetime (which will get converted to a snowflake id).
"""

T = TypeVar('T')
class PaginatableList(List[T], Entity):
    """
    This is a list with pagination information attached.

    It is returned by the API when a list of items is requested, and the response contains
    a Link header with pagination information.
    """
    _pagination_next: Optional[PaginationInfo]
    _pagination_prev: Optional[PaginationInfo]

    def __init__(self, *args, **kwargs):
        """
        Initializes basic list and adds empty pagination information.
        """
        super(PaginatableList, self).__init__(*args, **kwargs)
        self._pagination_next = None
        self._pagination_prev = None 

class NonPaginatableList(List[T], Entity):
    """
    This is just a list, without pagination information but
    annotated for serialization and deserialization.
    """
    def __init__(self, *args, **kwargs):
        super(NonPaginatableList, self).__init__(*args, **kwargs)

EntityList = Union[NonPaginatableList[T], PaginatableList[T]]
"""Lists in Mastodon.py are either regular or paginatable, so this is a union of
   :class:`NonPaginatableList` and :class:`PaginatableList`."""

try:
    OrderedStrDict = OrderedDict[str, Any]
except:
    OrderedStrDict = OrderedDict

class AttribAccessDict(OrderedStrDict, Entity):
    """
    Base return object class for Mastodon.py.

    Inherits from dict, but allows access via attributes as well as if it was a dataclass.

    While the subclasses implement specific fields with proper typing, parsing and documentation,
    they all inherit from this class, and parsing is extremely permissive to allow for forward and
    backward compatibility as well as compatibility with other implementations of the Mastodon API.

    This class can ALSO have pagination information attached, for paginating lists *inside* the object,
    because that's what Mastodon 4.3.0 does for groupee notifications. This is special cased in the class
    definition, though.
    """
    def __init__(self, **kwargs):
        """
        Constructor that calls through to dict constructor and then sets attributes for all keys.
        """
        super(AttribAccessDict, self).__init__()
        if "__union_specializer" in kwargs:
            self.__union_specializer = kwargs["__union_specializer"]
            del kwargs["__union_specializer"]
        if "__annotations__" in self.__class__.__dict__:
            for attr, _ in self.__class__.__annotations__.items():
                attr_name = attr
                if hasattr(self.__class__, "_rename_map"):
                    attr_name = getattr(self.__class__, "_rename_map").get(attr, attr)
                    if attr_name in kwargs:
                        self[attr] = kwargs[attr_name]
                        assert not attr in kwargs, f"Duplicate attribute {attr}"
                elif attr in kwargs:
                    self[attr] = kwargs[attr]
                else:
                    self[attr] = None
        for attr in kwargs:
            if not attr in self:
                self[attr] = kwargs[attr]
                
    def __getattribute__(self, attr):
        """
        Override to force access of normal attributes to go through __getattr__
        """
        if attr in ["_AttribAccessDict__union_specializer", "_mastopy_type", "_async_refresh", "__class__"]:
            return super(AttribAccessDict, self).__getattribute__(attr)
        if attr in self.__class__.__annotations__:
            return self.__getattr__(attr)
        return super(AttribAccessDict, self).__getattribute__(attr)

    def __getattr__(self, attr):
        """
        Basic attribute getter that throws if attribute is not in dict and supports redirecting access.
        """        
        if not hasattr(self.__class__, "_access_map"):
            # Base case: no redirecting
            if attr in self:
                return self[attr]
            else:
                return super(AttribAccessDict, self).__getattribute__(attr)
        else:
            if attr in self and self[attr] is not None:
                return self[attr]
            elif attr in getattr(self.__class__, "_access_map"):
                try:
                    attr_path = getattr(self.__class__, "_access_map")[attr].split('.')
                    cur_attr = self
                    for attr_path_part in attr_path:
                        cur_attr = getattr(cur_attr, attr_path_part)
                    return cur_attr
                except:
                    raise AttributeError(f"Attribute not found: {attr}")
            else:
                return super(AttribAccessDict, self).__getattribute__(attr)
            
    def __setattr__(self, attr, val):
        """
        Attribute setter that calls through to dict setter but will throw if attribute is not in dict
        """
        if attr in self or attr in ["_AttribAccessDict__union_specializer", "_mastopy_type", "_async_refresh"]:
            if attr in ["_mastopy_type", "_async_refresh"]:
                super(AttribAccessDict, self).__setattr__(attr, val)
            else:
                self[attr] = val
        else:
            raise AttributeError(f"Attribute not found: {attr}")

    def __setitem__(self, key, val):
        """
        Dict setter that also sets attributes and tries to typecast if we have an 
        AttribAccessDict, EntityList or MaybeSnowflakeIdType type hint.

        For Unions, we special case explicitly to specialize.
        """
        # If we're already an AttribAccessDict subclass, skip all the casting
        if not isinstance(val, AttribAccessDict):
            # Collate type hints that we may have
            type_hints = {}
            try:
                type_hints = get_type_hints(self.__class__)
            except:
                pass
            init_hints = {}
            try:
                init_hints = get_type_hints(self.__class__.__init__)
            except:
                pass
            type_hints.update(init_hints)

            # Ugly hack: We have to specialize unions by hand because you can't just guess by content generally
            # Note for developers: This means type MUST be set before meta. fortunately, we can enforce this via
            # the type hints (assuming that the order of annotations is not changed, which python does not guarantee,
            # if it ever does: we'll have to add another hack to the constructor)
            from mastodon.return_types import MediaAttachment
            if type(self) == MediaAttachment and key == "type":
                self.__union_specializer = val

            # Do we have a union specializer attribute?
            union_specializer = None
            if hasattr(self, "_AttribAccessDict__union_specializer"):
                union_specializer = self.__union_specializer

            # Do typecasting, possibly iterating over a list or tuple
            if key in type_hints:
                type_hint = type_hints[key]
                val = try_cast_recurse(type_hint, val, union_specializer)
            else:
                if isinstance(val, dict):
                    val = try_cast_recurse(AttribAccessDict, val, union_specializer)
                elif isinstance(val, list):
                    val = try_cast_recurse(EntityList, val, union_specializer)

        # Finally, call out to setattr and setitem proper
        super(AttribAccessDict, self).__setattr__(key, val)
        super(AttribAccessDict, self).__setitem__(key, val)

        # Remove union specializer if we have one
        if "_AttribAccessDict__union_specializer" in self:
            del self["_AttribAccessDict__union_specializer"]

    def __eq__(self, other):
        """
        Equality checker with casting
        """
        if isinstance(other, self.__class__):
            return super(AttribAccessDict, self).__eq__(other)
        else:
            try:
                casted = try_cast_recurse(self.__class__, other)
                if isinstance(casted, self.__class__):
                    return super(AttribAccessDict, self).__eq__(casted)
                else:
                    return False
            except Exception as e:
                pass
        return False

WebpushCryptoParamsPubkey = Dict[str, str]
"""A type containing the parameters for a encrypting webpush data. Considered opaque / implementation detail."""

WebpushCryptoParamsPrivkey = Dict[str, str]
"""A type containing the parameters for a derypting webpush data. Considered opaque / implementation detail."""

AttribAccessList = PaginatableList
"""Backwards compatibility alias"""
