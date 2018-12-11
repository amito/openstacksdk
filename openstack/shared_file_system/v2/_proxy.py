# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.shared_file_system.v2 import share as _share
from openstack import proxy


class Proxy(proxy.Proxy):

    def get_share(self, share):
        """Get a single share

        :param share: The value can be the ID of a share or a
                       :class:`~openstack.share.v2.share.Share` instance.

        :returns: One :class:`~openstack.share.v2.share.Share`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_share.Share, share)

    def shares(self, details=True, **query):
        """Retrieve a generator of shares

        :param bool details: When set to ``False``
                    :class:`~openstack.shared_file_system.v2.share.Share`
                    objects will be returned. The default, ``True``, will cause
                    :class:`~openstack.shared_file_system.v2.share.ShareDetail`
                    objects to be returned.
        :param kwargs **query: Optional query parameters to be sent to limit
            the shares being returned.  Available parameters include:

            * name: Name of the share as a string.
            * all_tenants: Whether return the shares of all tenants
            * status: Value of the status of the share so that you can filter
                    on "available" for example.

        :returns: A generator of share objects.
        """
        share = _share.ShareDetail if details else _share.Share
        return self._list(share, paginated=True, **query)

    def create_share(self, **attrs):
        """Create a new share from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.share.v2.share.Share`,
                           comprised of the properties on the Share class.

        :returns: The results of share creation
        :rtype: :class:`~openstack.share.v2.share.Share`
        """
        return self._create(_share.Share, **attrs)

    def delete_share(self, share, ignore_missing=True):
        """Delete a share

        :param share: The value can be either the ID of a share or a
                       :class:`~openstack.share.v2.share.Share` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the share does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent share.

        :returns: ``None``
        """
        self._delete(_share.Share, share, ignore_missing=ignore_missing)
