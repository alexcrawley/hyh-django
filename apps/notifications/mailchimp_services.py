# -*- coding: utf-8 -*-

import mailchimp

from django.conf import settings


def get_mailchimp_api():
    return mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY)


def subscribe_email(email, first_name=None, last_name=None):
    api = get_mailchimp_api()

    list_id = settings.MAILCHIMP_MAIN_LIST_ID

    email = {
        'email': email,
    }

    merge_vars = {
        'FNAME': first_name,
        'LNAME': last_name,
    }

    try:
        api.lists.subscribe(
            list_id, email,
            merge_vars=merge_vars,
            double_optin=False,
            update_existing=True
            )
        return True
    except mailchimp.ValidationError as e:
        acceptable_message = 'This email address looks fake or invalid. Please enter a real email address'
        if not str(e) == acceptable_message:
            raise e
        return False
