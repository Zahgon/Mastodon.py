# search.py - search endpoints

from mastodon.errors import MastodonVersionError
from mastodon.utility import api_version

from mastodon.internals import Mastodon as Internals
from mastodon.return_types import Search, SearchV2, Account, IdType
from typing import Union, Optional

class Mastodon(Internals):
    ###
    # Reading data: Searching
    ###
    def __ensure_search_params_acceptable(self, account_id, offset, min_id, max_id):
        """
        Internal Helper: Throw a MastodonVersionError if version is < 2.8.0 but parameters
        for search that are available only starting with 2.8.0 are specified.
        """
        pass

    @api_version("1.1.0", "2.8.0")
    def search(self, q: str, resolve: bool = True, result_type: Optional[str] = None, 
               account_id: Optional[Union[Account, IdType]] = None, offset: Optional[int] = None, 
               min_id: Optional[IdType] = None, max_id: Optional[IdType] = None, 
               exclude_unreviewed: bool = True) -> Union[Search, SearchV2]:
        """
        Fetch matching hashtags, accounts and statuses. Will perform webfinger
        lookups if resolve is True. Full-text search is only enabled if
        the instance supports it, and is restricted to statuses the logged-in
        user wrote or was mentioned in.

        `result_type` can be one of "accounts", "hashtags" or "statuses", to only
        search for that type of object.

        Specify `account_id` to only get results from the account with that id.

        `offset`, `min_id` and `max_id` can be used to paginate.

        `exclude_unreviewed` can be used to restrict search results for hashtags to only
        those that have been reviewed by moderators. It is on by default. When using the
        v1 search API (pre 2.4.1), it is ignored.

        Will use search_v1 (no tags in return values) on Mastodon versions before
        2.4.1), search_v2 otherwise. Parameters other than resolve are only available
        on Mastodon 2.8.0 or above - this function will throw a MastodonVersionError
        if you try to use them on versions before that. Note that the cached version
        number will be used for this to avoid uneccesary requests.
        """
        pass

    @api_version("1.1.0", "2.1.0")
    def search_v1(self, q: str, resolve: bool = False) -> Search:
        """
        Identical to `search_v2()`, except in that it does not return
        tags as objects, and doesn't support most of the new parameters.

        Should really not be used anymore.
        """
        pass

    @api_version("2.4.1", "2.8.0")
    def search_v2(self, q, resolve: bool = True, result_type: Optional[str] = None, 
               account_id: Optional[Union[Account, IdType]] = None, offset: Optional[int] = None, 
               min_id: Optional[IdType] = None, max_id: Optional[IdType] = None, 
               exclude_unreviewed: bool = True) -> SearchV2:
        """
        Identical to `search_v1()`, except in that it returns tags as objects, 
        has more parameters, and resolves by default.

        For more details documentation, please see `search()`
        """
        pass
