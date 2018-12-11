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


class ShareNetwork(resource.Resource):
    resource_key = "share_network"
    resources_key = "share_networks"

    base_path = "/share-networks"

    # capabilities
    allow_fetch = True
    allow_create = True
    allow_delete = True
    allow_list = True

    #: The share network ID.
    id = resource.body("id")
    #: The UUID of the project where the share network was created.
    project_id = resource.body("project_id")
    #: The neutron network ID.
    neutron_net_id = resource.body("neutron_net_id")
    #: The neutron subnet ID.
    neutron_subnet_id = resource.body("neutron_subnet_id")
    #: The network type.
    network_type = resource.body("network_type")
    #: The segmentation ID. This parameter is automatically set to a value
    #: determined by the network provider.
    segmentation_id = resource.body("segmentation_id", type=int)
    #: The IP block from which to allocate the network, in CIDR notation.
    cidr = resource.body("cidr")
    #: The IP version of the network.
    ip_version = resource.body("ip_version", type=int)
    #: The name of a share network.
    name = resource.body("name")
    #: The share network description.
    description = resource.body("description")
    #: The date and time stamp when the share network was created.
    #: The date and time stamp format is ISO 8601.
    created_at = resource.body("created_at")
    #: The date and time stamp when the share network was updated.
    #: The date and time stamp format is ISO 8601.
    updated_at = resource.body("updated_at")
    #: The gateway of a share network.
    gateway = resource.body("gateway")
    #: The MTU value of a share network.
    mtu = resource.body("mtu", type=int)


class ShareNetworkDetail(ShareNetwork):

    # capabilities
    allow_fetch = False
    allow_create = False
    allow_delete = False
    allow_commit = False
    allow_list = True
