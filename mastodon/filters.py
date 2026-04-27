# filters.py - Filter-related endpoints

import re

from mastodon.errors import MastodonIllegalArgumentError
from mastodon.utility import api_version

from mastodon.internals import Mastodon as Internals
from mastodon.return_types import Filter, FilterV2, Status, Notification, FilterKeyword, FilterStatus
from mastodon.types_base import PaginatableList, NonPaginatableList, IdType

from typing import Union, Optional, List, Dict


class Mastodon(Internals):
    ###
    # Reading data: Keyword filters
    ###
    @api_version("2.4.3", "2.4.3")
    def filters(self) -> NonPaginatableList[Filter]:
        """
        Fetch all of the logged-in user's filters.
        """
        pass

    @api_version("2.4.3", "2.4.3")
    def filter(self, id: Union[Filter, IdType]) -> Filter:
        """
        Fetches information about the filter with the specified `id`.
        """
        pass

    @api_version("2.4.3", "2.4.3")
    def filters_apply(self, objects: Union[PaginatableList[Status], PaginatableList[Notification]], filters: Union[NonPaginatableList[Filter], NonPaginatableList[FilterV2]], context: str) -> Union[PaginatableList[Status], PaginatableList[Notification]]:
        """
        Helper function: Applies a list of filters to a list of either statuses
        or notifications and returns only those matched by none. This function will
        apply all filters that match the context provided in `context`, i.e.
        if you want to apply only notification-relevant filters, specify
        'notifications'. Valid contexts are 'home', 'notifications', 'public' and 'thread'.

        NB: This is for v1 filters. v2 filters are applied by the server, which adds the "filtered"
        attribute to filtered statuses.
        """
        pass

    ###
    # Writing data: Keyword filters
    ###
    @api_version("2.4.3", "2.4.3")
    def filter_create(self, phrase: str, context: str, irreversible: bool = False, whole_word: bool = True, expires_in: Optional[int] = None) -> Filter:
        """
        Creates a new keyword filter. `phrase` is the phrase that should be
        filtered out, `context` specifies from where to filter the keywords.
        Valid contexts are 'home', 'notifications', 'public' and 'thread'.

        Set `irreversible` to True if you want the filter to just delete statuses
        server side. This works only for the 'home' and 'notifications' contexts.

        Set `whole_word` to False if you want to allow filter matches to
        start or end within a word, not only at word boundaries.

        Set `expires_in` to specify for how many seconds the filter should be
        kept around.

        Returns the newly created filter.
        """
        pass

    @api_version("2.4.3", "2.4.3")
    def filter_update(self, id: Union[Filter, IdType], phrase: Optional[str] = None, context: Optional[str] = None, irreversible: Optional[bool] = None, whole_word: Optional[bool] = None, expires_in: Optional[int] = None) -> Filter:
        """
        Updates the filter with the given `id`. Parameters are the same
        as in `filter_create()`.

        Returns the updated filter.
        """
        pass

    @api_version("2.4.3", "2.4.3")
    def filter_delete(self, id: Union[Filter, FilterV2, IdType]):
        """
        Deletes the filter with the given `id`.
        """
        pass

    ###
    # Filters v2 api
    ###
    @api_version("4.0.0", "4.0.0")
    def filters_v2(self) -> NonPaginatableList[FilterV2]:
        """
        Fetch all filters for the authenticated user.
        """
        pass

    @api_version("4.0.0", "4.0.0")
    def filter_v2(self, filter_id: Union[Filter, IdType]) -> Filter:
        """
        Fetch a specific filter by its ID.
        """
        pass

    @api_version("4.0.0", "4.0.0")
    def create_filter_v2(
        self,
        title: str,
        context: List[str],
        filter_action: str,
        expires_in: Optional[int] = None,
        keywords_attributes: Optional[List[Dict[str, Union[str, bool]]]] = None
    ) -> FilterV2:
        """
        Create a new filter with the given parameters.

        `title` is a human readable name for the filter. 
        
        `context` is list of contexts where the filter should apply. Valid values are:
            - "home": Filter applies to the home timeline.
            - "notifications": Filter applies to notifications. Filtered notifications land in notification requests.
            - "public": Filter applies to the public timelines.
            - "thread": Filter applies to conversations.
            - "account": Filter applies to account timelines.

        `filter_action` gives the policy to be applied when the filter is matched. Valid values are:
            - "warn": The user is warned if the content matches the filter.
            - "hide": The content is completely hidden if it matches the filter.

        NB: Even if you specify "hide", the status will still be returned - it will just have the "filtered" attribute set.
        
        pass a number of seconds as `expires_in` to make the filter expire in that many seconds. Use None for no expiration.
            
        pass a list of keyword dicts to initially as `keywords_attributes`, each with the following values:
            - "keyword": The term to filter on.
            - "whole_word": Whether word boundaries should be considered.
            
        """
        pass

    @api_version("4.0.0", "4.0.0")
    def update_filter_v2(
        self,
        filter_id: Union[FilterV2, IdType],
        title: Optional[str] = None,
        context: Optional[List[str]] = None,
        filter_action: Optional[str] = None,
        expires_in: Optional[int] = None,
        keywords_attributes: Optional[List[Dict[str, Union[str, bool, int]]]] = None
    ) -> FilterV2:
        """
        Update an existing filter with the given parameters.

        Parameters are as in `create_filter_v2()`. Only the parameters you want to update need to be provided.
        """
        pass

    @api_version("4.0.0", "4.0.0")
    def delete_filter_v2(self, filter_id: Union[FilterV2, IdType]) -> None:
        """
        Delete an existing filter.
        """
        pass

    @api_version("4.0.0", "4.0.0")
    def filter_keywords_v2(self, filter_id: Union[FilterV2, IdType]) -> NonPaginatableList[FilterKeyword]:
        """
        Fetch all keywords associated with a given filter.
        """
        pass

    @api_version("4.0.0", "4.0.0")
    def add_filter_keyword_v2(
        self,
        filter_id: Union[FilterV2, IdType],
        keyword: str,
        whole_word: bool = False
    ) -> FilterKeyword:
        """
        Add a single keyword to an existing filter.

        Parameters are as in `create_filter_v2()` `keywords_attributes`.
        """
        pass

    @api_version("4.0.0", "4.0.0")
    def delete_filter_keyword_v2(self, keyword_id: Union[FilterKeyword, IdType]) -> None:
        """
        Delete a single keyword from any filter.
        """
        pass

    @api_version("4.0.0", "4.0.0")
    def filter_statuses_v2(self, filter_id: Union[FilterV2, IdType]) -> List[FilterStatus]:
        """
        Retrieve all status-based filters for a FilterV2.
        """
        pass

    @api_version("4.0.0", "4.0.0")
    def add_filter_status_v2(self, filter_id: Union[FilterV2, IdType], status_id: Union[Status, IdType]) -> FilterStatus:
        """
        Add a status to a filter, which will then match on that status in addition to any keywords.
        Includes reblogs, does not include replies.
        """
        pass

    @api_version("4.0.0", "4.0.0")
    def filter_status_v2(self, filter_status_id: Union[FilterStatus, IdType]) -> FilterStatus:
        """
        Fetch a single status-based filter by its ID.
        """
        pass

    @api_version("4.0.0", "4.0.0")
    def delete_filter_status_v2(self, filter_status_id: Union[FilterStatus, IdType]) -> None:
        """
        Remove a status filter from a FilterV2.
        """
        pass
