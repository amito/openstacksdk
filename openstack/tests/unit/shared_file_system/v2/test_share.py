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

from openstack.tests.unit import base

from openstack.shared_file_system.v2 import share


SHARE = {
    "availability_zone": "nova",
    "share_network_id": "713df749-aac0-4a54-af52-10f6c991e80c",
    "export_locations": [],
    "share_server_id": "e268f4aa-d571-43dd-9ab3-f49ad06ffaef",
    "share_group_id": None,
    "snapshot_id": "d38b2430-daaa-11e8-a23e-a4d18cd39344",
    "id": "011d21e2-fbc3-4e4a-9993-9ea223f73264",
    "size": 1,
    "share_type": "25747776-08e5-494f-ab40-a64b9d20d8f7",
    "share_type_name": "default",
    "export_location": "/mnt/export",
    "metadata": {
        "project": "my_app",
        "aim": "doc"
    },
    "status": "available",
    "description": "My custom share London",
    "host": "manila2@generic1#GENERIC1",
    "has_replicas": False,
    "replication_type": None,
    "task_state": None,
    "is_public": True,
    "snapshot_support": True,
    "name": "share_London",
    "created_at": "2015-09-18T10:25:24.000000",
    "share_proto": "NFS",
    "volume_type": "default",
}

DETAILS = {
    "access_rules_status": "active",
}

SHARE_DETAIL = SHARE.copy()
SHARE_DETAIL.update(DETAILS)


class TestShare(base.TestCase):
    _TESTED_CLASS = share.Share
    _BASE_PATH = '/shares'
    _ATTRIBUTES = SHARE

    def _test_expected_attributes(self, sot):
        self.assertTrue(sot.allow_fetch)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_commit)
        self.assertTrue(sot.allow_list)

    def test_basic(self):
        sot = self._TESTED_CLASS(self._ATTRIBUTES)
        self.assertEqual("share", sot.resource_key)
        self.assertEqual("shares", sot.resources_key)
        self.assertEqual(self._BASE_PATH, sot.base_path)

        self._test_expected_attributes(sot)

        self.assertDictEqual({'name': 'name',
                              'description': 'description',
                              'status': 'status',
                              'all_tenants': 'all_tenants',
                              'tenant_id': 'tenant_id',
                              'snapshot_id': 'snapshot_id',
                              'share_group_id': 'share_group_id',
                              'export_location_id': 'export_location_id',
                              'export_location_path': 'export_location_path',
                              'limit': 'limit',
                              'marker': 'marker'},
                             sot._query_mapping._mapping)

    def test_create(self):
        sot = self._TESTED_CLASS(**self._ATTRIBUTES)
        for attribute_name, attribute_expected_value in \
                self._ATTRIBUTES.items():
            self.assertEqual(attribute_expected_value,
                             getattr(sot, attribute_name))


class TestShareDetail(TestShare):
    _TESTED_CLASS = share.ShareDetail
    _BASE_PATH = '/shares/detail'
    _ATTRIBUTES = SHARE_DETAIL

    def _test_expected_attributes(self, sot):
        self.assertFalse(sot.allow_fetch)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_delete)
        self.assertFalse(sot.allow_commit)
        self.assertTrue(sot.allow_list)
