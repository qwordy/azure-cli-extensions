# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import SwiftletManagementClientConfiguration
from .operations import OperationOperations
from .operations import VirtualMachineOperations
from .operations import VirtualMachineImageOperations
from .operations import VirtualMachineBundleOperations
from .operations import VirtualMachineSnapshotOperations
from .. import models


class SwiftletManagementClient(object):
    """Swiftlet Client.

    :ivar operation: OperationOperations operations
    :vartype operation: swiftlet_management_client.aio.operations.OperationOperations
    :ivar virtual_machine: VirtualMachineOperations operations
    :vartype virtual_machine: swiftlet_management_client.aio.operations.VirtualMachineOperations
    :ivar virtual_machine_image: VirtualMachineImageOperations operations
    :vartype virtual_machine_image: swiftlet_management_client.aio.operations.VirtualMachineImageOperations
    :ivar virtual_machine_bundle: VirtualMachineBundleOperations operations
    :vartype virtual_machine_bundle: swiftlet_management_client.aio.operations.VirtualMachineBundleOperations
    :ivar virtual_machine_snapshot: VirtualMachineSnapshotOperations operations
    :vartype virtual_machine_snapshot: swiftlet_management_client.aio.operations.VirtualMachineSnapshotOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = SwiftletManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine = VirtualMachineOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_image = VirtualMachineImageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_bundle = VirtualMachineBundleOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_snapshot = VirtualMachineSnapshotOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "SwiftletManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
