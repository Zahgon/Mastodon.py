# admin.py - admin / moderation endpoints

import time

from mastodon.errors import MastodonVersionError, MastodonAPIError
from mastodon.utility import api_version

from mastodon.internals import Mastodon as Internals
from mastodon.return_types import MediaAttachment, PathOrFile, IdType

from typing import Optional, Union, Tuple, List, Dict, Any

class Mastodon(Internals):
    ###
    # Reading data: Media
    ###
    @api_version("3.1.4", "3.1.4")
    def media(self, id: Union[MediaAttachment, IdType]) -> MediaAttachment:
        """
        Get the updated JSON for one non-attached / in progress media upload belonging
        to the logged-in user.
        """
        pass

    ###
    # Writing data: Media
    ###
    @api_version("1.0.0", "3.2.0")
    def media_post(self, media_file: PathOrFile, mime_type: Optional[str] = None, description: Optional[str] = None, 
                   focus: Optional[Tuple[float, float]] = None, file_name: Optional[str] = None, 
                   thumbnail: Optional[PathOrFile] = None, thumbnail_mime_type: Optional[str] = None, 
                   synchronous: bool = False) -> MediaAttachment:
        """
        Post an image, video or audio file. `media_file` can either be data or
        a file name. If data is passed directly, the mime type has to be specified
        manually, otherwise, it is determined from the file name. `focus` should be a tuple
        of floats between -1 and 1, giving the x and y coordinates of the images
        focus point for cropping (with the origin being the images center).

        Throws a `MastodonIllegalArgumentError` if the mime type of the
        passed data or file can not be determined properly.

        `file_name` can be specified to upload a file with the given name,
        which is ignored by Mastodon, but some other Fediverse server software
        will display it. If no name is specified, a random name will be generated.
        The filename of a file specified in media_file will be ignored.

        Starting with Mastodon 3.2.0, `thumbnail` can be specified in the same way as `media_file`
        to upload a custom thumbnail image for audio and video files.

        When using the v2 API (post Mastodon version 3.1.4), the `url` in the
        returned dict will be `null`, since attachments are processed
        asynchronously. You can fetch an updated dict using `media`. Pass
        "synchronous" to emulate the old behaviour. Not recommended, inefficient
        and deprecated, will eat your API quota, you know the deal.

        The returned value (or its id) can be used in a status post as the `media_ids` parameter.
        """
        pass

    @api_version("2.3.0", "3.2.0")
    def media_update(self, id: Union[MediaAttachment, IdType], description: Optional[str] = None, 
                     focus: Optional[Tuple[float, float]] = None, thumbnail: Optional[PathOrFile] = None, 
                     thumbnail_mime_type=None) -> MediaAttachment:
        """
        Update the metadata of the media file with the given `id`. `description` and
        `focus` and `thumbnail` are as in :ref:`media_post() <media_post()>` .
        
        The returned dict reflects the updates to the media attachment.

        Note: This is for updating the metadata of an *unattached* media attachment (i.e. one that has 
        not been used in a status yet). For editing media attachment metadata after posting, see `status_update` and
        `generate_media_edit_attributes`.
        """
        pass
