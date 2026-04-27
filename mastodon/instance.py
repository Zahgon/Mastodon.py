# instance.py - instance-level endpoints, directory, emoji, announcements
from mastodon.errors import MastodonDeprecationWarning, MastodonIllegalArgumentError, MastodonNotFoundError
from mastodon.utility import api_version
from mastodon.compat import urlparse

from mastodon.internals import Mastodon as Internals
from mastodon.return_types import Instance, InstanceV2, NonPaginatableList, Activity, Nodeinfo, AttribAccessDict, Rule, Announcement, CustomEmoji, Account, IdType, ExtendedDescription, DomainBlock, SupportedLocale, TermsOfService

from typing import Union, Optional, Dict, List

import datetime
import warnings

class Mastodon(Internals):
    ###
    # Reading data: Instances
    ###
    @api_version("1.1.0", "2.3.0")
    def instance_v1(self) -> Instance:
        """
        Retrieve basic information about the instance, including the URI and administrative contact email.

        Does not require authentication unless locked down by the administrator.

        This is the explicit v1 version of this function. The v2 version is available through instance_v2().
        It contains a bit more information than this one, but does not include whether invites are enabled.
        """
        pass

    def __instance(self) -> Instance:
        """
        Internal, non-version-checking helper that does the same as instance_v1()

        Silences the deprecation warnning, we are careful about fallbacks anywhere this is used.
        If you are using this, this is your notice to do that.
        """
        pass

    @api_version("4.0.0", "4.0.0")
    def instance_v2(self) -> InstanceV2:
        """
        Retrieve basic information about the instance, including the URI and administrative contact email.

        Does not require authentication unless locked down by the administrator. This is the explicit v2 variant.
        """
        pass

    def __instance_v2(self) -> InstanceV2:
        """
        Internal, non-version-checking helper that does the same as instance_v2()
        """
        pass

    @api_version("1.1.0", "4.0.0")
    def instance(self) -> Union[InstanceV2, Instance]:
        """
        Retrieve basic information about the instance, including the URI and administrative contact email.

        Does not require authentication unless locked down by the administrator.

        Will return the latest available version of the instance information. If you want a specific one,
        call the _v1 or _v2 variants
        """
        pass

    @api_version("2.1.2", "2.1.2")
    def instance_activity(self) -> NonPaginatableList[Activity]:
        """
        Retrieve activity stats about the instance. May be disabled by the instance administrator - throws
        a MastodonNotFoundError in that case.

        Activity is returned for 12 weeks going back from the current week.
        """
        pass

    @api_version("2.1.2", "2.1.2")
    def instance_peers(self) -> NonPaginatableList[str]:
        """
        Retrieve the instances that this instance knows about. May be disabled by the instance administrator - throws
        a MastodonNotFoundError in that case.

        Returns a list of URL strings.
        """
        pass

    @api_version("3.0.0", "3.0.0")
    def instance_health(self) -> bool:
        """
        Basic health check. Returns True if healthy, False if not.
        """
        pass

    @api_version("3.0.0", "3.0.0")
    def instance_nodeinfo(self, schema: str = "http://nodeinfo.diaspora.software/ns/schema/2.0") -> Nodeinfo:
        """
        Retrieves the instance's nodeinfo information.

        For information on what the nodeinfo can contain, see the nodeinfo
        specification: https://github.com/jhass/nodeinfo . By default,
        Mastodon.py will try to retrieve the version 2.0 schema nodeinfo, for which
        we have a well defined return object. If you go outside of that, all bets
        are off.

        To override the schema, specify the desired schema with the `schema`
        parameter.
        """
        pass

    @api_version("3.4.0", "3.4.0")
    def instance_rules(self) -> NonPaginatableList[Rule]:
        """
        Retrieve instance rules.
        """
        pass

    @api_version("4.4.0", "4.4.0")
    def instance_terms_of_service(self, date: Optional[datetime.date] = None) -> TermsOfService:
        """
        Retrieve the instance's terms of service.

        If `date` is specified, it will return the terms of service that were put in effect on that date.

        NB: This is not (currently?) a range lookup, you can only get the terms of service for a specific, exact date.
        """
        pass

    ###
    # Reading data: Directory
    ###
    @api_version("3.0.0", "3.0.0")
    def directory(self, offset: Optional[int] = None, limit: Optional[int] = None, 
                  order: Optional[str] = None, local: Optional[bool] = None) -> NonPaginatableList[Account]:
        """
        Fetch the contents of the profile directory, if enabled on the server.

        `offset` how many accounts to skip before returning results. Default 0.

        `limit` how many accounts to load. Default 40.

        `order` "active" to sort by most recently posted statuses (usually the default) or
                "new" to sort by most recently created profiles.

        `local` True to return only local accounts.

        Uses offset/limit pagination, not currently handled by the pagination utility functions,
        do it manually if you have to.
        """
        pass

    ###
    # Reading data: Emoji
    ###
    @api_version("2.1.0", "2.1.0")
    def custom_emojis(self) -> NonPaginatableList[CustomEmoji]:
        """
        Fetch the list of custom emoji the instance has installed.

        Does not require authentication unless locked down by the administrator.
        """
        pass

    ##
    # Reading data: Announcements
    ##
    @api_version("3.1.0", "3.1.0")
    def announcements(self) -> NonPaginatableList[Announcement]:
        """
        Fetch currently active announcements.
        """
        pass

    ###
    # Writing data: Annoucements
    ###
    @api_version("3.1.0", "3.1.0")
    def announcement_dismiss(self, id: Union[Announcement, IdType]):
        """
        Set the given annoucement to read.
        """
        pass

    @api_version("3.1.0", "3.1.0")
    def announcement_reaction_create(self, id: Union[Announcement, IdType], reaction: str):
        """
        Add a reaction to an announcement. `reaction` can either be a unicode emoji
        or the name of one of the instances custom emoji.

        Will throw an API error if the reaction name is not one of the allowed things
        or when trying to add a reaction that the user has already added (adding a
        reaction that a different user added is legal and increments the count).
        """
        pass

    @api_version("3.1.0", "3.1.0")
    def announcement_reaction_delete(self, id: Union[Announcement, IdType], reaction: str):
        """
        Remove a reaction to an announcement.

        Will throw an API error if the reaction does not exist.
        """
        pass

    @api_version("4.0.0", "4.0.0")
    def instance_extended_description(self) -> ExtendedDescription:
        """
        Retrieve the instance's extended description.
        """
        pass

    def instance_translation_languages(self) -> Dict[str, List[str]]:
        """
        Retrieve the instance's translation languages.

        Returns a dict with language pairs, where the key is the language code and the value is a list of language codes that the instance can translate that language to.
        """
        pass
        
    @api_version("4.0.0", "4.0.0")
    def instance_domain_blocks(self) -> NonPaginatableList[DomainBlock]:
        """
        Fetch a list of domains that have been blocked by the instance. Public endpoint, requires authentication if limited to users.

        Returns a MastodonAPIError if the admin has chosen to not make the list public, or to now show it at all.
        """
        pass

    @api_version("4.2.0", "4.2.0")
    def instance_languages(self) -> NonPaginatableList[SupportedLocale]:
        """
        Fetch a list of languages that the instance supports.
        """
        pass
    