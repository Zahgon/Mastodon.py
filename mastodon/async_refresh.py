# async_refresh.py - async refresh endpoints and utilities

import time
import copy

from mastodon.utility import api_version
from mastodon.errors import MastodonIllegalArgumentError, MastodonAPIError
from mastodon.internals import Mastodon as Internals
from mastodon.return_types import AsyncRefresh
from mastodon.types_base import AttribAccessDict, IdType, try_cast_recurse
from typing import Optional, Union, Tuple

class Mastodon(Internals):
    ###
    # Reading data: Async refreshes
    ###
    def get_async_refresh_info(self, result) -> Optional[Tuple[AsyncRefresh, int]]:
        """
        Extract async refresh information from an API result, if present.

        Returns a tuple of (:class:`AsyncRefresh`, retry_seconds) where the entity
        contains the ``id``, ``status`` (always ``"running"``), and optionally
        ``result_count``, and retry_seconds is the server-suggested polling
        interval in seconds.

        Returns None if the result has no async refresh information.
        """
        pass

    @api_version("4.4.0", "4.4.0")
    def get_async_refresh_status(self, result_or_id: Union[IdType, AsyncRefresh, AttribAccessDict]) -> AsyncRefresh:
        """
        Get the status of an async refresh by its ID. The ID can be obtained from
        a previous API response that included the ``Mastodon-Async-Refresh`` header,
        accessible via :meth:`get_async_refresh_info`.

        You can pass in an async refresh ID, an :class:`AsyncRefresh` entity (e.g. from 
        a previous call to this function or from :meth:`get_async_refresh_info`), or 
        an API result that has async refresh information (i.e. a previous API 
        result that had the header set).

        Returns an :class:`AsyncRefresh` dict.
        """
        pass

    @api_version("4.4.0", "4.4.0")
    def await_async_refresh(self, result, timeout: float = 0.0, max_attempts: int = -1) -> Optional[AttribAccessDict]:
        """
        Wait for an async refresh to finish, then re-fetch and return the 
        original resource.

        Polls the async refresh endpoint with backoff as indicated by the 
        server's ``retry`` hint. Once the refresh is ``finished``, re-issues 
        the original API request and returns the refreshed result entity.

        `result` should be a previous API result that has async refresh
        information (i.e. the server returned a ``Mastodon-Async-Refresh`` header
        with that response). If no such information is present, or the refresh
        info indicates the refresh is already finished, this function will
        return the original result as is immediately.

        `timeout` is the maximum total time in seconds to wait for the async refresh 
        to complete. Set to 0 for no timeout. Default is 0 (wait until done).

        `max_attempts` is the maximum number of polling attempts. Set to 0 or 
        negative for no limit. Default is -1 (wait until done).

        Returns the re-fetched original entity on success, or None if the 
        timeout or max attempts was exceeded before the refresh finished.

        Raises `MastodonIllegalArgumentError` if the passed object has async refresh 
        information but is missing the original request information needed to re-fetch.
        Raises `MastodonAPIError` if any of the API requests made during the process 
        fail with an error response.
        """
        pass

    def __get_async_refresh_id(self, result_or_id):
        """
        Internal helper: extract async refresh ID from an ID value or a result object.
        """
        pass
