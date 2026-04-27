# utility.py - utility functions, externally usable

from typing import TypeVar
import sys
import re
import dateutil
import datetime
import copy
import warnings

from mastodon.errors import MastodonAPIError, MastodonIllegalArgumentError, MastodonNotFoundError, MastodonVersionError
from mastodon.compat import IMPL_HAS_BLURHASH, blurhash, IMPL_HAS_GRAPHEME, grapheme
from mastodon.internals import Mastodon as Internals

from mastodon.versions import parse_version_string, max_version, api_version

from typing import Optional, Union, Dict, Iterator, Tuple, List
from mastodon.return_types import PaginatableList, PaginationInfo, PaginatableList, MediaAttachment
from mastodon.types_base import Entity, try_cast

from ._url_regex import url_regex
import unicodedata

_T = TypeVar("_T", bound=Entity)

class Mastodon(Internals):
    def set_language(self, lang: str):
        """
        Set the locale Mastodon will use to generate responses. Valid parameters are all ISO 639-1 (two letter) or, for languages that do
        not have one, 639-3 (three letter) language codes. This affects some error messages (those related to validation) and trends.
        """
        pass

    def retrieve_mastodon_version(self) -> str:
        """
        Determine installed Mastodon version and set major, minor and patch (not including RC info) accordingly.

        Returns the version string, possibly including rc info.
        """
        pass

    def verify_minimum_version(self, version_str: str, cached: bool = False) -> bool:
        """
        Update version info from server and verify that at least the specified version is present.

        If you specify "cached", the version info update part is skipped.

        Returns True if version requirement is satisfied, False if not.
        """
        pass

    def get_approx_server_time(self) -> datetime:
        """
        Retrieve the approximate server time

        We parse this from the hopefully present "Date" header, but make no effort to compensate for latency.
        """
        pass

    ###
    # Blurhash utilities
    ###
    def decode_blurhash(self, media_dict: MediaAttachment, out_size: Tuple[int, int] = (16, 16), size_per_component: bool = True, return_linear: bool = True) -> List[List[List[float]]]:
        """
        Basic media-dict blurhash decoding.

        out_size is the desired result size in pixels, either absolute or per blurhash
        component (this is the default).

        By default, this function will return the image as linear RGB, ready for further
        scaling operations. If you want to display the image directly, set return_linear
        to False.

        Returns the decoded blurhash image as a three-dimensional list: [height][width][3],
        with the last dimension being RGB colours.

        For further info and tips for advanced usage, refer to the documentation for the
        blurhash module: https://github.com/halcy/blurhash-python
        """
        pass

    ###
    # Pagination
    ###
    def fetch_next(self, previous_page: Union[PaginatableList[_T], _T, PaginationInfo]) -> Optional[Union[PaginatableList[_T], _T]]:
        """
        Fetches the next page of results of a paginated request. Pass in the
        previous page in its entirety, or the pagination information dict
        returned as a part of that pages last status ('_pagination_next').

        Returns the next page or None if no further data is available.
        """
        pass

    def fetch_previous(self, next_page: Union[PaginatableList[_T], _T, PaginationInfo]) -> Optional[Union[PaginatableList[_T], _T]]:
        """
        Fetches the previous page of results of a paginated request. Pass in the
        previous page in its entirety, or the pagination information dict
        returned as a part of that pages first status ('_pagination_prev').

        Returns the previous page or None if no further data is available.
        """
        pass

    def fetch_remaining(self, first_page: PaginatableList[_T]) -> PaginatableList[_T]:
        """
        Fetches all the remaining pages of a paginated request starting from a
        first page and returns the entire set of results (including the first page
        that was passed in) as a big list.

        Be careful, as this might generate a lot of requests, depending on what you are
        fetching, and might cause you to run into rate limits very quickly.

        Does not work with grouped notifications, since they use a somewhat weird, inside-out
        pagination scheme. If you need to access these in a paginated way, use fetch_next and fetch_previous
        directly.
        """
        pass

    def get_pagination_info(self, page: PaginatableList[Entity], pagination_direction: str) -> Optional[PaginationInfo]:
        """
        Extracts pagination information from a paginated response.

        Returns a PaginationInfo dictionary containing pagination information, or None if not available.

        The resulting PaginationInfo is best treated as opaque, though is unlikely to change.
        """
        pass

    def pagination_iterator(self, start_page: Union[PaginatableList[_T], PaginationInfo], direction: str = "next", return_pagination_info: bool = False) -> Iterator[_T]:
        """
        Returns an iterator that will yield all entries in a paginated request,
        starting from the given start_page (can also be just the PaginationInfo, in which case the
        first returned thing will be the result of fetch_next or fetch_previous, depending on the direction).
        and fetching new pages as needed, and breaks when no more pages are available.

        Set direction to "next" to iterate forward, or "previous" to iterate backwards.

        If return_pagination_info is True, the iterator will instead yield tuples of (Entity, PaginationInfo),
        where PaginationInfo is a dictionary containing pagination information for the current page and direction.

        Does not work with grouped notifications, since they use a somewhat weird, inside-out
        pagination scheme. If you need to access these in a paginated way, use fetch_next and fetch_previous
        directly.
        """
        pass

    @staticmethod
    def get_status_length(text: str, spoiler_text: str = "") -> int:
        """
        For a given status `text` and `spoiler_text`, return how many characters this status counts as
        when computing the status length and comparing it against the limit.

        Note that there are other limits you may run into, such as the maximum length of a URL, or the
        maximum length of a usernames domain part. But as long as you do *normal* things, this function
        will return the correct length for the status text.
        """
        def countable_text(input_text: str) -> str:
            def _url_repl(m: re.Match) -> str:
                pass
            pass
        pass


