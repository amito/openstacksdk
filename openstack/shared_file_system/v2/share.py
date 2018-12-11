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
from openstack import utils


class Share(resource.Resource):
    resource_key = "share"
    resources_key = "shares"

    base_path = "/shares"

    _query_mapping = resource.QueryParameters(
        'all_tenants', 'name', 'description', 'status', 'tenant_id',
        'snapshot_id', 'share_group_id', 'export_location_id',
        'export_location_path')

    # capabilities
    allow_fetch = True
    allow_create = True
    allow_delete = True
    allow_commit = True
    allow_list = True

    #: The UUID of the share.
    id = resource.Body("id")
    #: The share status.
    status = resource.Body("status")
    #: The share links
    links = resource.Body("links", type=list)
    #: The UUID of the project where the share network
    #: was created.
    project_id = resource.Body("project_id")
    #: The Shared File Systems protocol.
    share_proto = resource.Body("share_proto")
    #: The share size, in GBs.
    size = resource.Body("size", type=int)
    #: The share name.
    name = resource.Body("name")
    #: The share description.
    description = resource.Body("description")
    #: The share name.
    display_name = resource.Body("display_name")
    #: The share description.
    display_description = resource.Body("display_description")
    #: The UUID of the share type.
    share_type = resource.Body("share_type")
    #: The share type name.
    share_type_name = resource.Body("share_type_name")
    #: Indicates whether a share has replicas or not.
    has_replicas = resource.Body("has_replicas", type=bool)
    #: The share replication type.
    replication_type = resource.Body("replication_type")
    #: The volume type.
    volume_type = resource.Body("volume_type")
    #: The UUID of the snapshot that was used to create the share.
    snapshot_id = resource.Body("snapshot_id")
    #: The level of visibility for the share.
    is_public = resource.Body("is_public", type=bool)
    #: The UUID of the share group.
    share_group_id = resource.Body("share_group_id")
    #: One or more metadata key and value pairs as a dictionary of strings.
    metadata = resource.Body("metadata")
    #: The share network ID.
    share_network_id = resource.Body("share_network_id")
    #: The availability zone.
    availability_zone = resource.Body("availability_zone")
    #: The export location.
    export_location = resource.Body("export_location")
    #: A list of export locations.
    export_locations = resource.Body("export_locations", type=list)
    #: The share host name.
    host = resource.Body("host")
    #: For the share migration, the migration task state.
    task_state = resource.Body("task_state")
    #: The UUID of the share server.
    share_server_id = resource.Body("share_server_id")
    #: An extra specification that filters back ends by whether they do or do
    #: not support share snapshots.
    snapshot_support = resource.Body("snapshot_support", type=bool)
    #: The date and time stamp when the share was created.
    #: The date and time stamp format is ISO 8601.
    created_at = resource.Body("created_at")

    def _action(self, session, body):
        """Preform share actions given the message body."""
        url = utils.urljoin(Share.base_path, self.id, 'action')
        headers = {'Accept': ''}
        return session.post(url, json=body, headers=headers)


class ShareDetail(Share):
    base_path = "/shares/detail"

    # capabilities
    allow_fetch = False
    allow_create = False
    allow_delete = False
    allow_commit = False
    allow_list = True

    #: The share instance access rules status.
    access_rules_status = resource.Body("access_rules_status")
