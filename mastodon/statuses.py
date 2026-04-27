# statuses.py - status endpoints (regular and scheduled)

import collections
from datetime import datetime
import base64

from mastodon.errors import MastodonIllegalArgumentError, MastodonVersionError
from mastodon.utility import api_version

from mastodon.internals import Mastodon as Internals
from mastodon.return_types import Status, IdType, ScheduledStatus, PreviewCard, Context, NonPaginatableList, Account,\
                MediaAttachment, Poll, StatusSource, StatusEdit, PaginatableList, PathOrFile, Translation

from typing import Union, Optional, List, Dict, Any, Tuple

class Mastodon(Internals):
    ###
    # Reading data: Statuses
    ###
    @api_version("1.0.0", "2.0.0")
    def status(self, id: Union[Status, IdType]) -> Status:
        """
        Fetch information about a single toot.

        Does not require authentication for publicly visible statuses.
        """
        pass

    @api_version("4.3.0", "4.3.0")
    def statuses(self, ids: List[Union[Status, IdType]]) -> List[Status]:
        """
        Fetch information from multiple statuses by a list of status `id`.

        Does not require authentication for publicly visible accounts.
        """
        pass

    @api_version("1.0.0", "3.0.0")
    def status_card(self, id: Union[Status, IdType]) -> PreviewCard:
        """
        Fetch a card associated with a status. A card describes an object (such as an
        external video or link) embedded into a status.

        Does not require authentication for publicly visible statuses.

        This function is deprecated as of 3.0.0 and the endpoint does not
        exist anymore - you should just use the "card" field of the status
        instead. Mastodon.py will try to mimic the old behaviour, but this
        is somewhat inefficient and not guaranteed to be the case forever.
        """
        pass

    @api_version("1.0.0", "1.0.0")
    def status_context(self, id: Union[Status, IdType]) -> Context:
        """
        Fetch information about ancestors and descendants of a toot.

        Does not require authentication for publicly visible statuses.
        """
        pass

    @api_version("1.0.0", "2.1.0")
    def status_reblogged_by(self, id: Union[Status, IdType]) -> NonPaginatableList[Account]:
        """
        Fetch a list of users that have reblogged a status.

        Does not require authentication for publicly visible statuses.

        Interesting caveat: If you self-reblog a status with private
        visibility, this endpoint will not return your account as having
        reblogged it.
        """
        pass

    @api_version("1.0.0", "2.1.0")
    def status_favourited_by(self, id: Union[Status, IdType]) -> NonPaginatableList[Account]:
        """
        Fetch a list of users that have favourited a status.

        Does not require authentication for publicly visible statuses.
        """
        pass

    ###
    # Reading data: Scheduled statuses
    ###
    @api_version("2.7.0", "2.7.0")
    def scheduled_statuses(self, max_id: Optional[Union[Status, IdType, datetime]] = None, min_id: Optional[Union[Status, IdType, datetime]] = None, 
                 since_id: Optional[Union[Status, IdType, datetime]] = None, limit: Optional[int] = None) -> PaginatableList[ScheduledStatus]:
        """
        Fetch a list of scheduled statuses
        """
        pass

    @api_version("2.7.0", "2.7.0")
    def scheduled_status(self, id: Union[ScheduledStatus, IdType]) -> ScheduledStatus:
        """
        Fetch information about the scheduled status with the given id.
        """
        pass

    ###
    # Writing data: Statuses
    ###
    def __status_internal(self, status: Optional[str], in_reply_to_id: Optional[Union[Status, IdType]] = None, media_ids: Optional[List[Union[MediaAttachment, IdType]]] = None,
                    sensitive: Optional[bool] = False, visibility: Optional[str] = None, spoiler_text: Optional[str] = None, language: Optional[str] = None, 
                    idempotency_key: Optional[str] = None, content_type: Optional[str] = None, scheduled_at: Optional[datetime] = None, 
                    poll: Optional[Union[Poll, IdType]] = None, quote_id: Optional[Union[Status, IdType]] = None, edit: bool = False,
                    strict_content_type: bool = False, media_attributes: Optional[List[Dict[str, Any]]] = None,
                    quoted_status_id: Optional[Union[Status, IdType]] = None, quote_approval_policy: Optional[str] = None) -> Union[Status, ScheduledStatus]:
        """
        Internal statuses poster helper
        """
        pass

    @api_version("1.0.0", "4.5.0")
    def status_post(self, status: str, in_reply_to_id: Optional[Union[Status, IdType]] = None, media_ids: Optional[List[Union[MediaAttachment, IdType]]] = None,
                    sensitive: bool = False, visibility: Optional[str] = None, spoiler_text: Optional[str] = None, language: Optional[str] = None, 
                    idempotency_key: Optional[str] = None, content_type: Optional[str] = None, scheduled_at: Optional[datetime] = None, 
                    poll: Optional[Union[Poll, IdType]] = None, quote_id: Optional[Union[Status, IdType]] = None, strict_content_type: bool = False,
                    quoted_status_id: Optional[Union[Status, IdType]] = None, quote_approval_policy: Optional[str] = None) -> Union[Status, ScheduledStatus]:
        """
        Post a status. Can optionally be in reply to another status and contain
        media.

        `media_ids` should be a list. (If it's not, the function will turn it
        into one.) It can contain up to four pieces of media (uploaded via
        :ref:`media_post() <media_post()>`). `media_ids` can also be the objects returned
        by :ref:`media_post() <media_post()>` - they are unpacked automatically.

        The `sensitive` boolean decides whether or not media attached to the post
        should be marked as sensitive, which hides it by default on the Mastodon
        web front-end.

        The `visibility` parameter is a string value and accepts any of:
        
        * ``'direct'`` - post will be visible only to **mentioned users**, known in Mastodon's UI as "Mentioned users only"
        * ``'private'`` - post will be visible only to **followers**, known in Mastodon's UI as "Followers only"
        * ``'unlisted'`` - post will be public but **will not appear** on the public timelines
        * ``'public'`` - post will be public and **will appear** on public timelines

\
        If not passed in, `visibility` defaults to match the current account's
        default-privacy setting (starting with Mastodon version 1.6) or its
        locked setting - ``'private'`` if the account is locked, ``'public'`` otherwise
        (for Mastodon versions lower than 1.6).

        The `spoiler_text` parameter is a string to be shown as a warning before
        the text of the status.  If no text is passed in, no warning will be
        displayed.

        Specify `language` to override automatic language detection. The parameter
        accepts all valid ISO 639-1 (2-letter) or for languages where that do not
        have one, 639-3 (three letter) language codes.

        You can set `idempotency_key` to a value to uniquely identify an attempt
        at posting a status. Even if you call this function more than once,
        if you call it with the same `idempotency_key`, only one status will
        be created.

        Pass a datetime as `scheduled_at` to schedule the toot for a specific time
        (the time must be at least 5 minutes into the future). If this is passed,
        status_post returns a `ScheduledStatus` instead.

        Pass `poll` to attach a poll to the status. An appropriate object can be
        constructed using :ref:`make_poll() <make_poll()>` . Note that as of Mastodon version
        2.8.2, you can only have either media or a poll attached, not both at
        the same time.

        Pass `quoted_status_id` to quote another status. The quoted status must
        exist, be accessible to the logged-in user, and the quote policy must
        allow it. If the post body does not contain a link to the quoted post,
        the server will prepend one for backward compatibility. Note that a
        status cannot have both a poll / media and a quote.

        Pass `quote_approval_policy` to set who is allowed to quote this status.
        One of ``'public'``, ``'followers'``, or ``'nobody'``. If omitted, the user's
        default setting is used. Ignored if `visibility` is ``'private'`` or ``'direct'``.

        You can use :ref:`get_status_length() <get_status_length()>` to count how many
        characters a status you want to post would take up in terms of Mastodons character
        limit. The limits can be retrieved from the instance information (`instance_v2()`).

        **Specific to "pleroma" feature set:**: Specify `content_type` to set
        the content type of your post on Pleroma. It accepts 'text/plain' (default),
        'text/markdown', 'text/html' and 'text/bbcode'. This parameter is not
        supported on Mastodon servers, but will be safely ignored if set.
        If you want to throw an error if the content type is not known
        to work on the server, set `strict_content_type` to True.

        **Specific to "fedibird" feature set:**: The `quote_id` parameter is
        a non-standard extension that specifies the id of a quoted status.
        For standard Mastodon 4.5+, use `quoted_status_id` instead, this does
        absolutely nothing.

        Returns the new status.
        """
        pass

    @api_version("1.0.0", "2.8.0")
    def toot(self, status: str) -> Status:
        """
        Synonym for :ref:`status_post() <status_post()>` that only takes the status text as input.

        Usage in production code is not recommended.
        """
        pass


    def generate_media_edit_attributes(self, id: Union[MediaAttachment, IdType], description: Optional[str] = None, 
                                      focus: Optional[Tuple[float, float]] = None, 
                                      thumbnail: Optional[PathOrFile] = None, thumb_mimetype: Optional[str] = None) -> Dict[str, Any]:
        """
        Helper function to generate a single media edit attribute dictionary.
        
        Parameters:
        - `id` (str): The ID of the media attachment (mandatory).
        - `description` (Optional[str]): A new description for the media.
        - `focus` (Optional[Tuple[float, float]]): The focal point of the media.
        - `thumbnail` (Optional[PathOrFile]): The thumbnail to be used.
        """
        pass

    @api_version("3.5.0", "4.1.0")
    def status_update(self, id: Union[Status, IdType], status: str, spoiler_text: Optional[str] = None, 
                      sensitive: Optional[bool] = None, media_ids: Optional[List[Union[MediaAttachment, IdType]]] = None, 
                      poll: Optional[Union[Poll, IdType]] = None, media_attributes: Optional[List[Dict[str, Any]]] = None,
                      quote_approval_policy: Optional[str] = None) -> Status:
        """
        Edit a status. The meanings of the fields are largely the same as in :ref:`status_post() <status_post()>`,
        though not every field can be edited. The `status` parameter is mandatory.

        Note that editing a poll will reset the votes.

        To edit media metadata, pass a list of dictionaries describing the edits as `media_attributes`.
        You can use :meth:`generate_media_edit_attributes`
        to generate these dictionaries.
        """
        pass

    @api_version("3.5.0", "3.5.0")
    def status_history(self, id: Union[StatusEdit, IdType]) -> NonPaginatableList[StatusEdit]:
        """
        Returns the edit history of a status as a list of StatusEdit objects, starting
        from the original form. Note that this means that a status that has been edited
        once will have *two* entries in this list, a status that has been edited twice
        will have three, and so on.
        """
        pass

    def status_source(self, id: Union[Status, IdType]) -> StatusSource:
        """
        Returns the source of a status for editing.

        Return value is a dictionary containing exactly the parameters you could pass to
        :ref:`status_update() <status_update()>` to change nothing about the status, except `status` is `text`
        instead.
        """
        pass

    @api_version("1.0.0", "4.5.0")
    def status_reply(self, to_status: Union[Status, IdType], status: str, media_ids: Optional[List[Union[MediaAttachment, IdType]]] = None,
                    sensitive: bool = False, visibility: Optional[str] = None, spoiler_text: Optional[str] = None, language: Optional[str] = None, 
                    idempotency_key: Optional[str] = None, content_type: Optional[str] = None, scheduled_at: Optional[datetime] = None, 
                    poll: Optional[Union[Poll, IdType]] = None, quote_id: Optional[Union[Status, IdType]] = None, untag: bool = False, 
                    strict_content_type: bool = False, quoted_status_id: Optional[Union[Status, IdType]] = None,
                    quote_approval_policy: Optional[str] = None) -> Status:
        """
        Helper function - acts like status_post, but prepends the name of all
        the users that are being replied to the status text and retains
        CW and visibility if not explicitly overridden.

        Note that `to_status` must be a `Status` and not just an ID. 

        Set `untag` to True if you want the reply to only go to the user you
        are replying to, removing every other mentioned user from the
        conversation.
        """
        pass

    @api_version("1.0.0", "1.0.0")
    def status_delete(self, id: Union[Status, IdType], delete_media: bool = None) -> Status:
        """
        Delete a status

        Returns the now-deleted status, with an added "text" attribute that contains
        the text that was used to compose this status (this can be used to power
        "delete and redraft" functionality) as well as either poll or media_attachments
        set in the same way. Note that when reattaching media, you have to wait up to several
        seconds for the media to be un-attached from the original status - that operation is
        not synchronous with the delete.

        Pass `delete_media=True` to delete the media attachments of the status immediately,
        instead of just scheduling them for deletion as part of the next media cleanup. If you
        set this, you will not be able to reuse them in a new status (so if you're delete-redrafting,
        you should not set this).
        """
        pass

    @api_version("1.0.0", "2.0.0")
    def status_reblog(self, id: Union[Status, IdType], visibility: Optional[str] = None) -> Status:
        """
        Reblog / boost a status.

        The visibility parameter functions the same as in :ref:`status_post() <status_post()>` and
        allows you to reduce the visibility of a reblogged status.

        Returns a new Status that wraps around the reblogged status.
        """
        pass

    @api_version("1.0.0", "2.0.0")
    def status_unreblog(self, id: Union[Status, IdType]) -> Status:
        """
        Un-reblog a status.

        Returns the status that used to be reblogged.
        """
        pass

    @api_version("1.0.0", "2.0.0")
    def status_favourite(self, id: Union[Status, IdType]) -> Status:
        """
        Favourite a status.

        Returns the favourited status.
        """
        pass

    @api_version("1.0.0", "2.0.0")
    def status_unfavourite(self, id: Union[Status, IdType]) -> Status: 
        """
        Un-favourite a status.

        Returns the un-favourited status.
        """
        pass

    @api_version("1.4.0", "2.0.0")
    def status_mute(self, id: Union[Status, IdType]) -> Status:
        """
        Mute notifications for a status.

        Returns the now muted status
        """
        pass

    @api_version("1.4.0", "2.0.0")
    def status_unmute(self, id: Union[Status, IdType]) -> Status:
        """
        Unmute notifications for a status.

        Returns the status that used to be muted.
        """
        pass

    @api_version("2.1.0", "2.1.0")
    def status_pin(self, id: Union[Status, IdType]) -> Status:
        """
        Pin a status for the logged-in user.

        Returns the now pinned status
        """
        pass

    @api_version("2.1.0", "2.1.0")
    def status_unpin(self, id: Union[Status, IdType]) -> Status:
        """
        Unpin a pinned status for the logged-in user.

        Returns the status that used to be pinned.
        """
        pass

    @api_version("3.1.0", "3.1.0")
    def status_bookmark(self, id: Union[Status, IdType]) -> Status:
        """
        Bookmark a status as the logged-in user.

        Returns the now bookmarked status
        """
        pass

    @api_version("3.1.0", "3.1.0")
    def status_unbookmark(self, id: Union[Status, IdType]) -> Status:
        """
        Unbookmark a bookmarked status for the logged-in user.

        Returns the status that used to be bookmarked.
        """
        pass

    ###
    # Writing data: Scheduled statuses
    ###
    @api_version("2.7.0", "2.7.0")
    def scheduled_status_update(self, id: Union[Status, IdType], scheduled_at: datetime) -> ScheduledStatus:
        """
        Update the scheduled time of a scheduled status.

        New time must be at least 5 minutes into the future.

        Returned object reflects the updates to the scheduled status.
        """
        pass

    @api_version("2.7.0", "2.7.0")
    def scheduled_status_delete(self, id: Union[Status, IdType]) -> None:
        """
        Deletes a scheduled status.
        """
        pass

    ##
    # Translation
    ##
    @api_version("4.0.0", "4.0.0")
    def status_translate(self, id: Union[Status, IdType], lang: Optional[str] = None) -> Translation:
        """
        Translate the status content into some language.

        Raises a `MastodonAPIError` if the server can't perform the requested translation, for any
        reason (doesn't support translation, unsupported language pair, etc.).
        """
        pass

    ###
    # Reading data: Quotes
    ###
    @api_version("4.5.0", "4.5.0")
    def status_quotes(self, id: Union[Status, IdType], max_id: Optional[Union[Status, IdType]] = None,
                      since_id: Optional[Union[Status, IdType]] = None, limit: Optional[int] = None) -> PaginatableList[Status]:
        """
        Fetch a list of statuses that quote the given status.

        Requires a logged-in user.
        """
        pass

    ###
    # Writing data: Quotes
    ###
    @api_version("4.5.0", "4.5.0")
    def status_quote_revoke(self, id: Union[Status, IdType], quoting_status_id: Union[Status, IdType]) -> Status:
        """
        Revoke quote authorization of a status that is quoting one of the logged in users statuses.

        `id` is the ID of the status that is being quoted, and `quoting_status_id`
        is the ID of the status that is quoting it. 

        Returns the quoting status with the quote state set to ``'revoked'``.
        """
        pass

    @api_version("4.5.0", "4.5.0")
    def status_update_quote_approval_policy(self, id: Union[Status, IdType], quote_approval_policy: str) -> Status:
        """
        Update the quote approval policy of a status without going through the full edit flow.

        `quote_approval_policy` is one of ``'public'``, ``'followers'``, or ``'nobody'``.

        * ``'public'`` - anyone (except blocked users) can quote and will be automatically accepted
        * ``'followers'`` - only followers and the author can quote
        * ``'nobody'`` - only the author can quote

        If the status has a visibility of ``'private'`` or ``'direct'``, the policy
        will always be set to ``'nobody'`` regardless of the value passed in.
        Changing the policy does not invalidate past quotes, use :meth:`status_quote_revoke`
        for that.

        Returns the updated status.
        """
        pass
