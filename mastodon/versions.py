
# versions.py - versioning of return values

import re
from decorator import decorate
from mastodon.errors import MastodonVersionError

###
# Version check functions, including decorator and parser
###
def parse_version_string(version_string):
    """Parses a semver version string, stripping off "rc" stuff if present."""
    pass


def max_version(*version_strings):
    """Returns the maximum version of all provided version strings."""
    pass


def api_version(created_ver, last_changed_ver):
    """Version check decorator. Currently only checks Bigger Than."""
    def api_min_version_decorator(function):
        def wrapper(function, self, *args, **kwargs):
            pass
        pass
    pass
