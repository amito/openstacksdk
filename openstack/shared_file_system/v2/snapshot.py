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

from openstack import resource


class Snapshot(resource.Resource):
    resource_key = "snapshot"
    resources_key = "snapshots"
    base_path = "/snapshots"

    _query_mapping = resource.QueryParameters(
        'all_tenants', 'name', 'description', 'tenant_id')

    # capabilities
    allow_fetch = True
    allow_create = True
    allow_delete = True
    allow_commit = True
    allow_list = True

    #: The UUID of the snapshot.
    id = resource.body("id")
    #: The UUID of the source share that was used to create the snapshot.
    share_id = resource.body("share_id")
    #: The snapshot status.
    status = resource.body("status")
    #: The snapshot name.
    name = resource.body("name")
    #: The snapshot description.
    description = resource.body("description")
    #: The date and time stamp when the snapshot or snapshot instance was
    #: created. The date and time stamp format is ISO 8601.
    created_at = resource.body("created_at")
    #: The file system protocol of a share snapshot.
    share_proto = resource.body("share_proto")
    #: The share snapshot size, in GBs.
    share_size = resource.body("share_size", type=int)
    #: Provider location of the snapshot on the backend.
    provider_location = resource.body("provider_location")
    #: The snapshot size, in GBs.
    size = resource.body("size", type=int)


class SnapshotDetail(Snapshot):
    base_path = "/snapshots/detail"

    # capabilities
    allow_fetch = False
    allow_create = False
    allow_delete = False
    allow_commit = False
    allow_list = True
