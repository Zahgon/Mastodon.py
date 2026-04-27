    # relationships.py - endpoints for user and domain blocks and mutes as well as follow requests

from mastodon.errors import MastodonIllegalArgumentError
from mastodon.defaults import _DEFAULT_STREAM_TIMEOUT, _DEFAULT_STREAM_RECONNECT_WAIT_SEC
from mastodon.utility import api_version

from mastodon.internals import Mastodon as Internals


class Mastodon(Internals):
    ###
    # Streaming
    ###
    @api_version("1.1.0", "1.4.2")
    def stream_user(self, listener, run_async=False, timeout=_DEFAULT_STREAM_TIMEOUT, reconnect_async=False, reconnect_async_wait_sec=_DEFAULT_STREAM_RECONNECT_WAIT_SEC):
        """
        Streams events that are relevant to the authorized user, i.e. home
        timeline and notifications.
        """
        pass

    @api_version("1.1.0", "1.4.2")
    def stream_public(self, listener, run_async=False, timeout=_DEFAULT_STREAM_TIMEOUT, reconnect_async=False, reconnect_async_wait_sec=_DEFAULT_STREAM_RECONNECT_WAIT_SEC, local=False, remote=False):
        """
        Streams public events.

        Set `local` to True to only get local statuses.
        Set `remote` to True to only get remote statuses.
        """
        pass

    @api_version("1.1.0", "1.4.2")
    def stream_local(self, listener, run_async=False, timeout=_DEFAULT_STREAM_TIMEOUT, reconnect_async=False, reconnect_async_wait_sec=_DEFAULT_STREAM_RECONNECT_WAIT_SEC):
        """
        Streams local public events.

        This function is deprecated. Please use stream_public() with parameter `local` set to True instead.
        """
        pass

    @api_version("1.1.0", "1.4.2")
    def stream_hashtag(self, tag, listener, local=False, run_async=False, timeout=_DEFAULT_STREAM_TIMEOUT, reconnect_async=False, reconnect_async_wait_sec=_DEFAULT_STREAM_RECONNECT_WAIT_SEC):
        """
        Stream for all public statuses for the hashtag 'tag' seen by the connected
        instance.

        Set `local` to True to only get local statuses.
        """
        pass

    @api_version("2.1.0", "2.1.0")
    def stream_list(self, id, listener, run_async=False, timeout=_DEFAULT_STREAM_TIMEOUT, reconnect_async=False, reconnect_async_wait_sec=_DEFAULT_STREAM_RECONNECT_WAIT_SEC):
        """
        Stream events for the current user, restricted to accounts on the given
        list.
        """
        pass

    @api_version("2.6.0", "2.6.0")
    def stream_direct(self, listener, run_async=False, timeout=_DEFAULT_STREAM_TIMEOUT, reconnect_async=False, reconnect_async_wait_sec=_DEFAULT_STREAM_RECONNECT_WAIT_SEC):
        """
        Streams direct message events for the logged-in user, as conversation events.
        """
        pass

    @api_version("2.5.0", "2.5.0")
    def stream_healthy(self) -> bool:
        """
        Returns True if streaming API is okay, False or raises an error otherwise.
        """
        pass
