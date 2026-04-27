# relationships.py - endpoints for user and domain blocks and mutes as well as follow requests

from mastodon.utility import api_version

from mastodon.internals import Mastodon as Internals
from mastodon.return_types import Account, Relationship, PaginatableList, IdType
from typing import Optional, Union

class Mastodon(Internals):
    ###
    # Reading data: Mutes and Blocks
    ###
    @api_version("1.1.0", "2.6.0")
    def mutes(self, max_id: Optional[IdType] = None, min_id: Optional[IdType] = None, since_id: 
              Optional[IdType] = None, limit: Optional[int] = None) -> PaginatableList[Account]:
        """
        Fetch a list of users muted by the logged-in user.
        """
        pass

    @api_version("1.0.0", "2.6.0")
    def blocks(self, max_id: Optional[IdType] = None, min_id: Optional[IdType] = None, since_id: 
              Optional[IdType] = None, limit: Optional[int] = None) -> PaginatableList[Account]:
        """
        Fetch a list of users blocked by the logged-in user.
        """
        pass

    ###
    # Reading data: Follow requests
    ###
    @api_version("1.0.0", "2.6.0")
    def follow_requests(self, max_id: Optional[IdType] = None, min_id: Optional[IdType] = None, since_id: 
              Optional[IdType] = None, limit: Optional[int] = None) -> PaginatableList[Account]:
        """
        Fetch the logged-in user's incoming follow requests.
        """
        pass

    ###
    # Reading data: Domain blocks
    ###
    @api_version("1.4.0", "2.6.0")
    def domain_blocks(self, max_id: Optional[IdType] = None, min_id: Optional[IdType] = None, since_id: 
              Optional[IdType] = None, limit: Optional[int] = None) -> PaginatableList[str]:
        """
        Fetch the logged-in user's blocked domains.

        Returns a list of blocked domain URLs (as strings, without protocol specifier).
        """
        pass

    ###
    # Writing data: Follow requests
    ###
    @api_version("1.0.0", "3.0.0")
    def follow_request_authorize(self, id: Union[Account, IdType]) -> Relationship:
        """
        Accept an incoming follow request from the given Account and returns the updated Relationship.
        """
        pass

    @api_version("1.0.0", "3.0.0")
    def follow_request_reject(self, id: Union[Account, IdType]) -> Relationship:
        """
        Reject an incoming follow request from the given Account and returns the updated Relationship.
        """
        pass

    ###
    # Writing data: Domain blocks
    ###
    @api_version("1.4.0", "1.4.0")
    def domain_block(self, domain: str) -> None:
        """
        Add a block for all statuses originating from the specified domain for the logged-in user.
        """
        pass

    @api_version("1.4.0", "1.4.0")
    def domain_unblock(self, domain: str) -> None:
        """
        Remove a domain block for the logged-in user.
        """
        pass
