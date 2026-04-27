# push.py - webpush endpoints and tooling

import base64
import os
import json

from mastodon.errors import MastodonIllegalArgumentError
from mastodon.utility import api_version
from mastodon.compat import IMPL_HAS_CRYPTO, ec, serialization, default_backend
from mastodon.compat import IMPL_HAS_ECE, http_ece

from mastodon.internals import Mastodon as Internals
from mastodon.return_types import WebpushCryptoParamsPubkey, WebpushCryptoParamsPrivkey, WebPushSubscription, PushNotification, try_cast_recurse
from typing import Optional, Tuple

class Mastodon(Internals):
    ###
    # Reading data: Webpush subscriptions
    ###
    @api_version("2.4.0", "2.4.0")
    def push_subscription(self) -> WebPushSubscription:
        """
        Fetch the current push subscription the logged-in user has for this app.

        Only one webpush subscription can be active at a time for any given app.
        """
        pass

    ###
    # Writing data: Push subscriptions
    ###
    @api_version("2.4.0", "4..0")
    def push_subscription_set(self, endpoint: str, encrypt_params: WebpushCryptoParamsPubkey, follow_events: Optional[bool] = None,
                              favourite_events: Optional[bool] = None, reblog_events: Optional[bool] = None,
                              mention_events: Optional[bool] = None, poll_events: Optional[bool] = None,
                              follow_request_events: Optional[bool] = None, status_events: Optional[bool] = None, 
                              policy: str = 'all', update_events: Optional[bool] = None, admin_sign_up_events: Optional[bool] = None,
                              admin_report_events: Optional[bool] = None, quote_events: Optional[bool] = None,
                              quoted_update_events: Optional[bool] = None, standard: bool = None) -> WebPushSubscription:
        """
        Sets up or modifies the push subscription the logged-in user has for this app.

        `endpoint` is the endpoint URL mastodon should call for pushes. Note that mastodon
        requires https for this URL. `encrypt_params` is a dict with key parameters that allow
        the server to encrypt data for you: A public key `pubkey` and a shared secret `auth`.
        You can generate this as well as the corresponding private key using the
        :ref:`push_subscription_generate_keys() <push_subscription_generate_keys()>` function.

        `policy` controls what sources will generate webpush events. Valid values are
        `all`, `none`, `follower` and `followed`.

        The rest of the parameters controls what kind of events you wish to subscribe to.
        Events whose names start with "admin" require admin privileges to subscribe to.

        * `follow_events` controls whether you receive events when someone follows the logged in user.
        * `favourite_events` controls whether you receive events when someone favourites one of the logged in users statuses.
        * `reblog_events` controls whether you receive events when someone boosts one of the logged in users statuses.
        * `mention_events` controls whether you receive events when someone mentions the logged in user in a status.
        * `poll_events` controls whether you receive events when a poll the logged in user has voted in has ended.
        * `follow_request_events` controls whether you receive events when someone requests to follow the logged in user.
        * `status_events` controls whether you receive events when someone the logged in user has subscribed to notifications for posts a new status.
        * `update_events` controls whether you receive events when a status that the logged in user has boosted has been edited.
        * `admin_sign_up_events` controls whether you receive events when a new user signs up.
        * `admin_report_events` controls whether you receive events when a new report is received.
        * `quote_events` controls whether you receive events when someone quotes one of the logged in user's statuses.
        * `quoted_update_events` controls whether you receive events when a status the logged in user has quoted has been edited.

        Pass `standard=True` to use the standard webpush subscription format, instead of the pre-release RFC format
        mastodon was using before.
        """
        pass

    @api_version("2.4.0", "2.4.0")
    def push_subscription_update(self, follow_events: Optional[bool] = None,
                              favourite_events: Optional[bool] = None, reblog_events: Optional[bool] = None,
                              mention_events: Optional[bool] = None, poll_events: Optional[bool] = None,
                              follow_request_events: Optional[bool] = None, status_events: Optional[bool] = None, 
                              policy: Optional[str] = 'all', update_events: Optional[bool] = None, admin_sign_up_events: Optional[bool] = None,
                              admin_report_events: Optional[bool] = None, quote_events: Optional[bool] = None,
                              quoted_update_events: Optional[bool] = None) -> WebPushSubscription:
        """
        Modifies what kind of events the app wishes to subscribe to.

        Parameters are as in push_subscription_set().

        Returned object reflects the updated push subscription.
        """
        pass

    @api_version("2.4.0", "2.4.0")
    def push_subscription_delete(self) -> None:
        """
        Remove the current push subscription the logged-in user has for this app.
        """
        pass

    ###
    # Push subscription crypto utilities
    ###
    def push_subscription_generate_keys(self) -> Tuple[WebpushCryptoParamsPubkey, WebpushCryptoParamsPrivkey]:
        """
        Generates a private key, public key and shared secret for use in webpush subscriptions.

        Returns two dicts: One with the private key and shared secret and another with the
        public key and shared secret.
        """
        pass

    @api_version("2.4.0", "2.4.0")
    def push_subscription_decrypt_push(self, data: bytes, decrypt_params: WebpushCryptoParamsPrivkey, encryption_header: str, crypto_key_header: str) -> PushNotification:
        """
        Decrypts `data` received in a webpush request. Requires the private key dict
        from :ref:`push_subscription_generate_keys() <push_subscription_generate_keys()>` (`decrypt_params`) as well as the
        Encryption and server Crypto-Key headers from the received webpush
        """
        pass
