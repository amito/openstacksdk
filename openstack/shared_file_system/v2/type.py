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

from openstack.shared_file_system import shared_file_system_service
from openstack import resource


class Type(resource.Resource):
    resource_key = "share_type"
    resources_key = "share_types"

    base_path = "/types"
    service = shared_file_system_service.SharedFileSystemService()

    # capabilities
    allow_fetch = True
    allow_create = True
    allow_delete = True
    allow_list = True

    #: The UUID of the share type.
    id = resource.body("id")
    #: The required extra specifications for the share type.
    required_extra_specs = resource.body("required_extra_specs")
    #: The extra specifications for the share type.
    extra_specs = resource.body("extra_specs")
    #: An extra specification that defines the driver mode for share server,
    #: or storage, life cycle management.
    driver_handles_share_servers = resource.body(
        "driver_handles_share_servers", type=bool)
    #: An extra specification that filters back ends by whether they do or do
    #: not support share snapshots.
    snapshot_support = resource.body("snapshot_support", type=bool)
    #: Indicates whether a share type is publicly accessible.
    is_public = resource.body("os-share-type-access:is_public", type=bool)
    #: The share type name.
    name = resource.body("name")
    #: The share replication type.
    replication_type = resource.body("replication_type")
    #: Boolean extra spec used for filtering of back ends by their capability
    #: to mount share snapshots.
    mount_snapshot_support = resource.body("mount_snapshot_support", type=bool)
    #: Boolean extra spec used for filtering of back ends by their capability
    #: to revert shares to snapshots.
    revert_to_snapshot_support = resource.body("revert_to_snapshot_support",
                                               type=bool)
    #: Boolean extra spec used for filtering of back ends by their capability
    #: to create shares from snapshots.
    create_share_from_snapshot_support = resource.body(
        "create_share_from_snapshot_support", type=bool)
    #: The description of the share type.
    description = resource.body("description")
    #: Defines the share type created is default or not.
    is_default = resource.body("is_default", type=bool)


class TypeDetail(Type):

    # capabilities
    allow_fetch = False
    allow_create = False
    allow_delete = False
    allow_commit = False
    allow_list = True
