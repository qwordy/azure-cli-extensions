# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ApplyUpdate
    from ._models_py3 import ConfigurationAssignment
    from ._models_py3 import ErrorDetails
    from ._models_py3 import ListConfigurationAssignmentsResult
    from ._models_py3 import ListMaintenanceConfigurationsResult
    from ._models_py3 import ListUpdatesResult
    from ._models_py3 import MaintenanceConfiguration
    from ._models_py3 import MaintenanceError
    from ._models_py3 import Operation
    from ._models_py3 import OperationInfo
    from ._models_py3 import OperationsListResult
    from ._models_py3 import Resource
    from ._models_py3 import Update
except (SyntaxError, ImportError):
    from ._models import ApplyUpdate  # type: ignore
    from ._models import ConfigurationAssignment  # type: ignore
    from ._models import ErrorDetails  # type: ignore
    from ._models import ListConfigurationAssignmentsResult  # type: ignore
    from ._models import ListMaintenanceConfigurationsResult  # type: ignore
    from ._models import ListUpdatesResult  # type: ignore
    from ._models import MaintenanceConfiguration  # type: ignore
    from ._models import MaintenanceError  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationInfo  # type: ignore
    from ._models import OperationsListResult  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import Update  # type: ignore

from ._maintenance_client_enums import (
    ImpactType,
    MaintenanceScope,
    UpdateStatus,
    Visibility,
)

__all__ = [
    'ApplyUpdate',
    'ConfigurationAssignment',
    'ErrorDetails',
    'ListConfigurationAssignmentsResult',
    'ListMaintenanceConfigurationsResult',
    'ListUpdatesResult',
    'MaintenanceConfiguration',
    'MaintenanceError',
    'Operation',
    'OperationInfo',
    'OperationsListResult',
    'Resource',
    'Update',
    'ImpactType',
    'MaintenanceScope',
    'UpdateStatus',
    'Visibility',
]
