# internals.py - many internal helpers

from datetime import timezone, datetime, timedelta
from contextlib import closing
import mimetypes
import threading
import uuid
import dateutil.parser
import time
import copy
import requests
import re
import collections
import base64
import os
import inspect
import warnings

from mastodon.versions import parse_version_string
from mastodon.errors import MastodonNetworkError, MastodonIllegalArgumentError, MastodonRatelimitError, MastodonNotFoundError, \
                    MastodonUnauthorizedError, MastodonInternalServerError, MastodonBadGatewayError, MastodonServiceUnavailableError, \
                    MastodonGatewayTimeoutError, MastodonServerError, MastodonAPIError, MastodonMalformedEventError, MastodonDeprecationWarning
from mastodon.compat import urlparse, magic, PurePath, Path
from mastodon.defaults import _DEFAULT_STREAM_TIMEOUT, _DEFAULT_STREAM_RECONNECT_WAIT_SEC
from mastodon.return_types import AttribAccessDict, PaginatableList, try_cast_recurse
from mastodon.return_types import *

###
# Internal helpers, dragons probably
###
class Mastodon():
    def __datetime_to_epoch(self, date_time: datetime) -> float:
        """
        Converts a python datetime to unix epoch, accounting for
        time zones and such.

        Assumes UTC if timezone is not given.
        """
        pass

    def __get_logged_in_id(self):
        """
        Fetch the logged in user's ID, with caching. ID is reset on calls to log_in.
        """
        pass

    @staticmethod
    def __consistent_isoformat_utc(datetime_val: datetime) -> str:
        """
        Function that does what isoformat does but it actually does the same
        every time instead of randomly doing different things on some systems
        and also it represents that time as the equivalent UTC time.
        """
        pass

    def __try_cast_to_type(self, value, override_type = None):
        """
        Tries to cast a value to the type of the function two levels up in the call stack.
        Tries to cast to AttribAccessDict if it doesn't know what to cast to.

        This is used internally inside of __api_request.
        """
        pass

    def __api_request(self, method, endpoint, params={}, files={}, headers={}, access_token_override=None, base_url_override=None,
                        do_ratelimiting=True, use_json=False, parse=True, return_response_object=False, skip_error_check=False, lang_override=None, override_type=None,
                        force_pagination=False):
        """
        Internal API request helper.

        Does a large amount of different things that I should document one day, but not today.
        """
        pass

    def __get_streaming_base(self) -> str:
        """
        Internal streaming API helper.

        Returns the correct URL for the streaming API.
        """
        pass

    def __stream(self, endpoint, listener, params={}, run_async=False, timeout=_DEFAULT_STREAM_TIMEOUT, reconnect_async=False, reconnect_async_wait_sec=_DEFAULT_STREAM_RECONNECT_WAIT_SEC):
        """
        Internal streaming API helper.

        Returns a handle to the open connection that the user can close if they
        wish to terminate it.
        """
        def connect_func():
            pass
        class __stream_handle:
            def __init__(self, connection, listener, event_handler, reconnect_async, reconnect_async_mutex):
                pass
            def is_alive(self):
                pass
            def is_receiving(self):
                pass
            def close(self):
                pass
            def _sleep_attentive(self):
                pass
            def _threadproc(self):
                pass
            pass
        pass

    def __generate_params(self, params, exclude=[], dateconv=False, for_json=False):
        """
        Internal named-parameters-to-dict helper.

        Note for developers: If called with locals() as params,
        as is the usual practice in this code, the __generate_params call
        (or at least the locals() call) should generally be the first thing
        in your function.
        """
        pass

    def __unpack_id(self, id, dateconv = False, listify = False, field = "id"):
        """
        Internal object-to-id converter

        Checks if id is a dict that contains id and
        returns the id inside, otherwise just returns
        the id straight.

        Also unpacks datetimes to snowflake IDs if requested.
        """
        pass

    def __decode_webpush_b64(self, data):
        """
        Re-pads and decodes urlsafe base64.
        """
        pass

    def __get_token_expired(self):
        """Internal helper for oauth code"""
        pass

    def __set_token_expired(self, value):
        """Internal helper for oauth code"""
        pass

    def __get_refresh_token(self):
        """Internal helper for oauth code"""
        pass

    def __set_refresh_token(self, value):
        """Internal helper for oauth code"""
        pass

    def __guess_type(self, media_file):
        """Internal helper to guess media file type"""
        pass

    def __load_media_file(self, media_file, mime_type=None, file_name=None):
        """Internal helper to load a media file"""
        pass

    @staticmethod
    def __protocolize(base_url):
        """Internal add-protocol-to-url helper"""
        pass

    @staticmethod
    def __oauth_url_check(oauth_url, allow_http=False):
        """Internal helper to check and normalize OAuth URLs"""
        pass

    @staticmethod
    def __deprotocolize(base_url):
        """Internal helper to strip http and https from a URL"""
        pass

    def __normalize_version_string(self, version_string):
        # Split off everything after the first space, to take care of Pleromalikes so that the parser doesn't get confused in case those have a + somewhere in their version
        pass
