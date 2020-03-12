# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ExtendedLivySessionRequest(Model):
    """ExtendedLivySessionRequest.

    :param tags:
    :type tags: dict[str, str]
    :param artifact_id:
    :type artifact_id: str
    :param name:
    :type name: str
    :param file:
    :type file: str
    :param class_name:
    :type class_name: str
    :param args:
    :type args: list[str]
    :param jars:
    :type jars: list[str]
    :param files:
    :type files: list[str]
    :param archives:
    :type archives: list[str]
    :param conf:
    :type conf: dict[str, str]
    :param driver_memory:
    :type driver_memory: str
    :param driver_cores:
    :type driver_cores: int
    :param executor_memory:
    :type executor_memory: str
    :param executor_cores:
    :type executor_cores: int
    :param num_executors:
    :type num_executors: int
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'file': {'key': 'file', 'type': 'str'},
        'class_name': {'key': 'className', 'type': 'str'},
        'args': {'key': 'args', 'type': '[str]'},
        'jars': {'key': 'jars', 'type': '[str]'},
        'files': {'key': 'files', 'type': '[str]'},
        'archives': {'key': 'archives', 'type': '[str]'},
        'conf': {'key': 'conf', 'type': '{str}'},
        'driver_memory': {'key': 'driverMemory', 'type': 'str'},
        'driver_cores': {'key': 'driverCores', 'type': 'int'},
        'executor_memory': {'key': 'executorMemory', 'type': 'str'},
        'executor_cores': {'key': 'executorCores', 'type': 'int'},
        'num_executors': {'key': 'numExecutors', 'type': 'int'},
    }

    def __init__(self, *, tags=None, artifact_id: str=None, name: str=None, file: str=None, class_name: str=None, args=None, jars=None, files=None, archives=None, conf=None, driver_memory: str=None, driver_cores: int=None, executor_memory: str=None, executor_cores: int=None, num_executors: int=None, **kwargs) -> None:
        super(ExtendedLivySessionRequest, self).__init__(**kwargs)
        self.tags = tags
        self.artifact_id = artifact_id
        self.name = name
        self.file = file
        self.class_name = class_name
        self.args = args
        self.jars = jars
        self.files = files
        self.archives = archives
        self.conf = conf
        self.driver_memory = driver_memory
        self.driver_cores = driver_cores
        self.executor_memory = executor_memory
        self.executor_cores = executor_cores
        self.num_executors = num_executors
