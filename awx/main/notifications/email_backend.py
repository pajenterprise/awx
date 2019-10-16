# Copyright (c) 2016 Ansible, Inc.
# All Rights Reserved.

from django.core.mail.backends.smtp import EmailBackend

from awx.main.notifications.custom_notification_base import CustomNotificationBase
from CustomNotificationBase import DEFAULT_MSG, DEFAULT_BODY


class CustomEmailBackend(EmailBackend, CustomNotificationBase):

    init_parameters = {"host": {"label": "Host", "type": "string"},
                       "port": {"label": "Port", "type": "int"},
                       "username": {"label": "Username", "type": "string"},
                       "password": {"label": "Password", "type": "password"},
                       "use_tls": {"label": "Use TLS", "type": "bool"},
                       "use_ssl": {"label": "Use SSL", "type": "bool"},
                       "sender": {"label": "Sender Email", "type": "string"},
                       "recipients": {"label": "Recipient List", "type": "list"},
                       "timeout": {"label": "Timeout", "type": "int", "default": 30}}
    recipient_parameter = "recipients"
    sender_parameter = "sender"

    default_messages = {"started": {"message": DEFAULT_MSG, "body": DEFAULT_BODY},
                        "success": {"message": DEFAULT_MSG, "body": DEFAULT_BODY},
                        "error": {"message": DEFAULT_MSG, "body": DEFAULT_BODY}}

    def format_body(self, body):
        # leave body unchanged (expect a string)
        return body
