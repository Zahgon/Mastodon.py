# hashtags.py - hashtag and featured-hashtag endpoints
from mastodon.utility import api_version

from mastodon.internals import Mastodon as Internals
from mastodon.return_types import Tag, NonPaginatableList, PaginatableList, FeaturedTag, IdType
from mastodon.errors import MastodonIllegalArgumentError

from typing import Union, Optional
from datetime import datetime

class Mastodon(Internals):
    ###
    # Reading data: Featured hashtags
    ###
    @api_version("3.0.0", "3.0.0")
    def featured_tags(self) -> NonPaginatableList[FeaturedTag]:
        """
        Return the hashtags the logged-in user has set to be featured on
        their profile.
        """
        pass

    @api_version("3.0.0", "3.0.0")
    def featured_tag_suggestions(self) -> NonPaginatableList[FeaturedTag]:
        """
        Returns the logged-in user's 10 most commonly-used hashtags.
        """
        pass

    ###
    # Writing data: Featured hashtags
    ###
    @api_version("3.0.0", "3.0.0")
    def featured_tag_create(self, name: str) -> FeaturedTag:
        """
        Creates a new featured hashtag displayed on the logged-in user's profile.

        The returned object is the newly featured tag.

        Obsoleted by `tag_feature` / `tag_unfeature`.
        """
        pass

    @api_version("3.0.0", "3.0.0")
    def featured_tag_delete(self, id: Union[FeaturedTag, IdType]) -> None:
        """
        Deletes one of the logged-in user's featured hashtags.

        Obsoleted by `tag_feature` / `tag_unfeature`.
        """
        pass

    @api_version("4.4.0", "4.4.0")
    def tag_feature(self, name: str) -> Tag:
        """
        Creates a new featured hashtag displayed on the logged-in user's profile.

        Same effect as above, but newer. Likely obsoletes `featured_tag_create`.
        """
        pass
    
    @api_version("4.4.0", "4.4.0")
    def tag_unfeature(self, name: str) -> Tag:
        """
        Deletes one of the logged-in user's featured hashtags.

        Same effect as above, but newer. Likely obsoletes `featured_tag_delete`.
        """
        pass

    ###
    # Reading data: Followed tags
    ###
    @api_version("4.0.0", "4.0.0")
    def followed_tags(self, max_id: Optional[Union[Tag, IdType, datetime]] = None, 
                      min_id: Optional[Union[Tag, IdType, datetime]] = None, since_id: Optional[Union[Tag, IdType, datetime]] = None, 
                      limit: Optional[int] = None) -> PaginatableList[Tag]:
        """
        Returns the logged-in user's followed tags.
        """
        pass
    
    
    @api_version("4.0.0", "4.0.0")
    def tag(self, hashtag: Union[Tag, str]) -> Tag:
        """
        Get information about a single tag.
        """
        pass
    
    ###
    # Writing data: Followed tags
    ###
    @api_version("4.0.0", "4.0.0")
    def tag_follow(self, hashtag: Union[Tag, str]) -> Tag:
        """
        Follow a tag.

        Returns the newly followed tag.
        """
        pass
    
    @api_version("4.0.0", "4.0.0")
    def tag_unfollow(self, hashtag: Union[Tag, str]) -> Tag:
        """
        Unfollow a tag.

        Returns the previously followed tag.
        """
        pass
    
