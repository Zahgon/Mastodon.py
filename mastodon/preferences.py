# preferences.py - user preferences, markers

import collections

from mastodon.errors import MastodonIllegalArgumentError
from mastodon.utility import api_version

from mastodon.internals import Mastodon as Internals
from mastodon.return_types import Preferences, Marker, Status, IdType
from mastodon.types_base import AttribAccessDict, try_cast_recurse
from typing import Union, List, Dict

class Mastodon(Internals):
    ###
    # Reading data: Preferences
    ###
    @api_version("2.8.0", "2.8.0")
    def preferences(self) -> Preferences:
        """
        Fetch the user's preferences, which can be used to set some default options.
        As of 2.8.0, apps can only fetch, not update preferences.
        """
        pass

    ##
    # Reading data: Read markers
    ##
    @api_version("3.0.0", "3.0.0")
    def markers_get(self, timeline: Union[str, List[str]] = ["home"]) -> Dict[str, Marker]:
        """
        Get the last-read-location markers for the specified timelines. Valid timelines
        are `home` (the home timeline) and `notifications` (the notifications timeline,
        affects which notifications are considered read).

        Note that despite the singular name, `timeline` can be a list.

        Returns a dict with the markers, keyed by timeline name.
        """
        pass

    ##
    # Writing data: Read markers
    ##
    @api_version("3.0.0", "3.0.0")
    def markers_set(self, timelines: Union[str, List[str]], last_read_ids: Union[Status, IdType, List[Status], List[IdType]]) -> Dict[str, Marker]:
        """
        Set the "last read" marker(s) for the given timeline(s) to the given id(s)

        Valid timelines are `home` (the home timeline) and `notifications` (the notifications timeline,
        affects which notifications are considered read).
        
        Note that if you give an invalid timeline name, this will silently do nothing.

        Returns a dict with the updated markers, keyed by timeline name.
        """
        pass
