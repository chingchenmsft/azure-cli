# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class CostThresholdProperties(Model):
    """Properties of a cost threshold item.

    :param threshold_id: The ID of the cost threshold item.
    :type threshold_id: str
    :param percentage_threshold: The value of the percentage cost threshold.
    :type percentage_threshold: :class:`PercentageCostThresholdProperties
     <azure.mgmt.devtestlabs.models.PercentageCostThresholdProperties>`
    :param display_on_chart: Indicates whether this threshold will be
     displayed on cost charts. Possible values include: 'Enabled', 'Disabled'
    :type display_on_chart: str or :class:`CostThresholdStatus
     <azure.mgmt.devtestlabs.models.CostThresholdStatus>`
    :param send_notification_when_exceeded: Indicates whether notifications
     will be sent when this threshold is exceeded. Possible values include:
     'Enabled', 'Disabled'
    :type send_notification_when_exceeded: str or :class:`CostThresholdStatus
     <azure.mgmt.devtestlabs.models.CostThresholdStatus>`
    :param notification_sent: Indicates the datetime when notifications were
     last sent for this threshold.
    :type notification_sent: str
    """

    _attribute_map = {
        'threshold_id': {'key': 'thresholdId', 'type': 'str'},
        'percentage_threshold': {'key': 'percentageThreshold', 'type': 'PercentageCostThresholdProperties'},
        'display_on_chart': {'key': 'displayOnChart', 'type': 'str'},
        'send_notification_when_exceeded': {'key': 'sendNotificationWhenExceeded', 'type': 'str'},
        'notification_sent': {'key': 'NotificationSent', 'type': 'str'},
    }

    def __init__(self, threshold_id=None, percentage_threshold=None, display_on_chart=None, send_notification_when_exceeded=None, notification_sent=None):
        self.threshold_id = threshold_id
        self.percentage_threshold = percentage_threshold
        self.display_on_chart = display_on_chart
        self.send_notification_when_exceeded = send_notification_when_exceeded
        self.notification_sent = notification_sent
