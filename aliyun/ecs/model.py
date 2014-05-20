# Copyright 2014, Quixey Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

class Region(object):

    def __init__(self, region_id, local_name):
        """Constructor.

        Args:
            region_id (str): The id of the region.
            local_name (str): The local name of the region.
        """
        self.region_id = region_id
        self.local_name = local_name

    def __repr__(self):
        return u'<Region %s (%s) at %s>' % (
            self.region_id, self.local_name, id(self))

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.__dict__ == other.__dict__)


class Instance(object):

    """An Aliyun ECS instance."""

    def __init__(
            self, instance_id, name, image_id, region_id, instance_type,
            hostname, status, security_group_ids, public_ip_addresses,
            internal_ip_addresses, internet_charge_type,
            internet_max_bandwidth_in, internet_max_bandwidth_out,
            creation_time):
        """"Constructor.

        Args:
            instance_id (str): The id of the instance.
            name (str): The name of the instance.
            image_id (str): The id of the image used to create the instance.
            region_id (str): The id of the region in which the instance lies.
            instance_type (str): The type of the instance.
            hostname (str): The hostname of the instance.
            status (str): The status of the instance.
            security_group_ids (list): The security group ids for the instance.
            public_ip_addresses (list): Its public ip addresses.
            internal_ip_addresses (list): Its internal ip addresses.
            internet_charge_type (str): The accounting method of network use.
            internet_max_bandwidth_in (int): The max incoming bandwidth.
            internet_max_bandwidth_out (int): The max outgoing bandwidth.
            creation_time (datetime): Its creation time.
        """
        self.instance_id = instance_id
        self.name = name
        self.image_id = image_id
        self.region_id = region_id
        self.instance_type = instance_type
        self.hostname = hostname
        self.status = status
        self.security_group_ids = security_group_ids
        self.public_ip_addresses = public_ip_addresses
        self.internal_ip_addresses = internal_ip_addresses
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.creation_time = creation_time

    def __repr__(self):
        return '<Instance %s at %s>' % (self.instance_id, id(self))

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.__dict__ == other.__dict__)


class InstanceStatus(object):

    def __init__(self, instance_id, status):
        """Constructor.

        Args:
            instance_id (str): The id of the instance.
            status (str): The status of the instance.
        """
        self.instance_id = instance_id
        self.status = status

    def __repr__(self):
        return u'<InstanceId %s is %s at %s>' % (
            self.instance_id, self.status, id(self))

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.__dict__ == other.__dict__)


class InstanceType(object):

    def __init__(self, instance_type_id, cpu_core_count, memory_size):
        """Constructor.

        Args:
            instance_type_id (str): The instance type id.
            cpu_core_count (int): The number of cpus.
            memory_size (int): The memory size in GB.
        """
        self.instance_type_id = instance_type_id
        self.cpu_core_count = cpu_core_count
        self.memory_size = memory_size

    def __repr__(self):
        return u'<InstanceType %s has %s cores and %sGB memory at %s>' % (
            self.instance_type_id, self.cpu_core_count, self.memory_size,
            id(self))

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.__dict__ == other.__dict__)


class Snapshot(object):

    def __init__(self, snapshot_id, snapshot_name, progress, creation_time):
        """Constructor.

        snapshot_id (str): The id of the snapshot.
        snapshot_name (str): The name of the snapshot.
        progress (int): The progress ready percentage.
        creation_time (datetime): Its creation time.
        """
        self.snapshot_id = snapshot_id
        self.snapshot_name = snapshot_name
        self.progress = progress
        self.creation_time = creation_time

    def __repr__(self):
        return u'<Snapshot %s is %s%% ready at %s>' % (
            self.snapshot_id, self.progress, id(self))

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.__dict__ == other.__dict__)


class Disk(object):

    def __init__(self, disk_id, disk_type, disk_category, disk_size):
        """Constructor.

        Args:
            disk_id (str): The id of the disk.
            disk_type (str): The type of disk.
                Values can be system or data.
            disk_category (str): The category of the disk.
                Values can be cloud, ephemeral or ephemeral_hio.
            disk_size (int): Its size in GB.
        """
        self.disk_id = disk_id
        self.disk_type = disk_type
        self.disk_category = disk_category
        self.disk_size = disk_size

    def __repr__(self):
        return u'<Disk %s of type %s is %sGB at %s>' % (
            self.disk_id, self.disk_type, self.disk_size, id(self))

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.__dict__ == other.__dict__)


class Image(object):

    def __init__(self, image_id, image_version, platform, description,
                 size, architecture, owner_alias, os_name, visibility):
        """Constructor.

        Args:
            image_id (str): The id of the image.
            image_version (str): The version of the image.
            platform (str): The platform.
            description (str): The description.
            size (int): Its size in GB.
            architecture (str): The architecture - either i386 or x86_64.
            owner_alias (str): system, else or others.
            os_name (str): The os name.
            visibility (str): Either public or private.
        """
        self.image_id = image_id
        self.image_version = image_version
        self.platform = platform
        self.description = description
        self.size = size
        self.architecture = architecture
        self.owner_alias = owner_alias
        self.os_name = os_name
        self.visibility = visibility

    def __repr__(self):
        return u'<Image %s(%s) for platform %s and arch %s at %s>' % (
            self.image_id, self.description, self.platform, self.architecture,
            id(self))

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.__dict__ == other.__dict__)


class SecurityGroupInfo(object):

    def __init__(self, security_group_id, description):
        """Constructor.

        Args:
            security_group_id (str): The id of the security group.
            description (str): The description of the security group.
        """
        self.security_group_id = security_group_id
        self.description = description

    def __repr__(self):
        return u'<SecurityGroupInfo %s, %s at %s>' % (
            self.security_group_id, self.description, id(self))

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.__dict__ == other.__dict__)


class SecurityGroupPermission(object):

    def __init__(self, ip_protocol, port_range, source_cidr_ip,
                 source_group_id, policy, nic_type):
        """Constructor.

        Args:
            ip_protocol (str): TCP, UDP, ICMP, GRE or ALL
            port_range (str): For tcp/udp range is 1 to 65535. Else -1/-1.
            source_cidr_ip (str): Source IP address range.
            source_group_id (str): Source security group.
            policy (str): Accept, Drop or Reject.
            nic_type (str): internet or intranet.
        """
        self.ip_protocol = ip_protocol
        self.port_range = port_range
        self.source_cidr_ip = source_cidr_ip
        self.source_group_id = source_group_id
        self.policy = policy
        self.nic_type = nic_type

    def __repr__(self):
        return u'<SecurityGroupPermission %s %s %s from %s at %s>' % (
            self.policy, self.ip_protocol, self.port_range,
            self.source_cidr_ip
            if self.source_cidr_ip else self.source_group_id,
            id(self))

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.__dict__ == other.__dict__)


class SecurityGroup(object):

    def __init__(self, region_id, security_group_id, description, permissions):
        """Constructor.

        Args:
            region_id (str): The id of the region for the security group.
            security_group_id (str): The id of the security group.
            description (str): The description of the security group.
            permission (list): List of SecurityGroupPermission.
        """
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.description = description
        self.permissions = permissions

    def __repr__(self):
        return u'<SecurityGroup %s, %s at %s>' % (
            self.security_group_id, self.description, id(self))

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.__dict__ == other.__dict__)
