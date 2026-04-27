
# reports.py - report endpoints

from mastodon.errors import MastodonVersionError, MastodonIllegalArgumentError
from mastodon.utility import api_version

from mastodon.internals import Mastodon as Internals
from mastodon.return_types import NonPaginatableList, Report, Account, IdType, Status, Rule
from typing import Union, Optional, List

class Mastodon(Internals):
    ###
    # Reading data: Reports
    ###
    @api_version("1.1.0", "1.1.0")
    def reports(self) -> NonPaginatableList[Report]:
        """
        Fetch a list of reports made by the logged-in user.

        Warning: This method has now finally been removed, and will not
        work on Mastodon versions 2.5.0 and above.
        """
        pass

    ###
    # Writing data: Reports
    ###
    @api_version("1.1.0", "3.5.0")
    def report(self, account_id: Union[Account, IdType], status_ids: Optional[Union[Status, IdType]] = None, comment: Optional[str] = None, 
               forward: bool = False, category: Optional[str] = None, rule_ids: Optional[List[Union[Rule, IdType]]] = None, forward_to_domains: Optional[List[str]] = None) -> Report:
        """
        Report statuses to the instances administrators.

        Accepts a list of toot IDs associated with the report, and a comment.

        Starting with Mastodon 3.5.0, you can also pass a `category` (one out of
        "spam", "violation" or "other") and `rule_ids` (a list of rule IDs corresponding
        to the rules returned by the :ref:`instance() <instance()>` API).

        Set `forward` to True to forward a report of a remote user to that users
        instance as well as sending it to the instance local administrators. Set
        forward_to_domains to a list of domains to forward the report to (only domains of
        people mentioned in the status), or omitto forward to the domain of the reported status.
        """
        pass
