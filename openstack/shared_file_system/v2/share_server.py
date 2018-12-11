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


class ShareServer(resource.Resource):
    resource_key = "share_server"
    resources_key = "share_servers"

    base_path = "/share-servers"

    # capabilities
    allow_fetch = True
    allow_create = False
    allow_delete = True
    allow_list = True

    #: The UUID of the share server.
    id = resource.body("id")
    #: The project ID.
    project_id = resource.body("project_id")
    #: The share server status.
    status = resource.body("status")
    #: The back-end details for a server.
    backend_details = resource.body("backend_details")
    #: The UUID of a share network that is associated with the share server.
    share_network_id = resource.body("share_network_id")
    #: The name of a share network.
    share_network_name = resource.body("share_network_name")
    #: The share server host name or IP address.
    host = resource.body("host")
    #: The date and time stamp when the share server was created.
    #: The date and time stamp format is ISO 8601.
    created_at = resource.body("created_at")
    #: The date and time stamp when the share server was updated.
    #: The date and time stamp format is ISO 8601:
    updated_at = resource.body("updated_at")
