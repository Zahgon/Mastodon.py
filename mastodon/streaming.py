"""
Handlers for the Streaming API:
https://github.com/mastodon/documentation/blob/master/content/en/methods/timelines/streaming.md
"""

import json
try:
    from inspect import signature
except:
    pass

from mastodon import Mastodon
from mastodon.Mastodon import MastodonMalformedEventError, MastodonNetworkError, MastodonReadTimeout
from mastodon.return_types import AttribAccessDict, Status, Notification, IdType, Conversation, Announcement, StreamReaction, try_cast_recurse
from typing import Optional, Any

from requests.exceptions import ChunkedEncodingError, ReadTimeout, ConnectionError

class StreamListener(object):
    """Callbacks for the streaming API. Create a subclass, override the on_xxx
    methods for the kinds of events you're interested in, then pass an instance
    of your subclass to Mastodon.user_stream(), Mastodon.public_stream(), or
    Mastodon.hashtag_stream()."""

    __EVENT_NAME_TO_TYPE = {
        "update": Status,
        "delete": IdType,
        "notification": Notification,
        "filters_changed": None,
        "conversation": Conversation,
        "announcement": Announcement,
        "announcement_reaction": StreamReaction,
        "announcement_delete": IdType,
        "status_update": Status,
        "encrypted_message": AttribAccessDict,
    }

    def on_update(self, status: Status):
        """A new status has appeared. `status` is the parsed `status dict`
        describing the status."""
        pass

    def on_delete(self, status_id: IdType):
        """A status has been deleted. `status_id` is the status' integer ID."""
        pass

    def on_notification(self, notification: Notification):
        """A new notification. `notification` is the object
        describing the notification. For more information, see the documentation
        for the notifications() method."""
        pass

    def on_filters_changed(self):
        """Filters have changed. Does not contain a payload, you will have to
           refetch filters yourself."""
        pass

    def on_conversation(self, conversation: Conversation):
        """A direct message (in the direct stream) has been received. `conversation`
        is the parsed `conversation dict` dictionary describing the conversation"""
        pass

    def on_announcement(self, annoucement: Announcement):
        """A new announcement has been published. `announcement` is the parsed
        `announcement dict` describing the newly posted announcement."""
        pass

    def on_announcement_reaction(self, reaction: StreamReaction):
        """Someone has reacted to an announcement."""
        pass

    def on_announcement_delete(self, annoucement_id: IdType):
        """An announcement has been deleted. `annoucement_id` is the id of the
        deleted announcement."""
        pass

    def on_status_update(self, status: Status):
        """A status has been edited. 'status' is the parsed JSON dictionary
        describing the updated status."""
        pass

    def on_encrypted_message(self, unclear):
        """An encrypted message has been received. Currently unused."""
        pass

    def on_abort(self, err):
        """There was a connection error, read timeout or other error fatal to
        the streaming connection. The exception object about to be raised
        is passed to this function for reference.

        Note that the exception will be raised properly once you return from this
        function, so if you are using this handler to reconnect, either never
        return or start a thread and then catch and ignore the exception.
        """
        pass

    def on_unknown_event(self, name, unknown_event=None):
        """An unknown mastodon API event has been received. The name contains the event-name and unknown_event
        contains the content of the unknown event.
        """
        pass

    def handle_heartbeat(self):
        """The server has sent us a keep-alive message. This callback may be
        useful to carry out periodic housekeeping tasks, or just to confirm
        that the connection is still open."""
        pass
    
    def on_any_event(self, name: str, data: Optional[Any] = None, for_stream: Optional[str] = None):
        """A generic event handler that is called for every event received.
        The name contains the event name and data contains the content of the event.

        for_stream is currently unused, but might be added in the future if we ever add websocket support.

        Called before the more specific on_xxx handlers.
        """
        pass

    def handle_stream(self, response):
        """
        Handles a stream of events from the Mastodon server. When each event
        is received, the corresponding .on_[name]() method is called.

        When the Mastodon API changes, the on_unknown_event(name, content)
        function is called.
        The default behavior is to throw an error. Define a callback handler
        to intercept unknown events if needed (and avoid errors)

        response; a requests response object with the open stream for reading.
        """
        pass

    def _parse_line(self, line, event):
        pass

    def _dispatch(self, event):
        pass


class CallbackStreamListener(StreamListener):
    """
    Simple callback stream handler class.
    Can optionally additionally send local update events to a separate handler.
    Define an unknown_event_handler for new Mastodon API events. This handler is
    *not* guaranteed to receive these events forever, and should only be used
    for diagnostics.
    """

    def __init__(self,
                 update_handler=None,
                 local_update_handler=None,
                 delete_handler=None,
                 notification_handler=None,
                 conversation_handler=None,
                 unknown_event_handler=None,
                 status_update_handler=None,
                 filters_changed_handler=None,
                 announcement_handler=None,
                 announcement_reaction_handler=None,
                 announcement_delete_handler=None,
                 encryted_message_handler=None
                 ):
        super(CallbackStreamListener, self).__init__()
        self.update_handler = update_handler
        self.local_update_handler = local_update_handler
        self.delete_handler = delete_handler
        self.notification_handler = notification_handler
        self.filters_changed_handler = filters_changed_handler
        self.conversation_handler = conversation_handler
        self.unknown_event_handler = unknown_event_handler
        self.status_update_handler = status_update_handler
        self.announcement_handler = announcement_handler
        self.announcement_reaction_handler = announcement_reaction_handler
        self.announcement_delete_handler = announcement_delete_handler
        self.encryted_message_handler = encryted_message_handler

    def on_update(self, status):
        pass

    def on_delete(self, deleted_id: IdType):
        pass

    def on_notification(self, notification: Notification):
        pass

    def on_filters_changed(self):
        pass

    def on_conversation(self, conversation: Conversation):
        pass

    def on_announcement(self, annoucement: Announcement):
        pass

    def on_announcement_reaction(self, reaction: StreamReaction):
        pass

    def on_announcement_delete(self, annoucement_id: IdType):
        pass

    def on_status_update(self, status: Status):
        pass

    def on_encrypted_message(self, unclear):
        pass

    def on_unknown_event(self, name: str, unknown_event: Optional[Any] = None):
        pass
