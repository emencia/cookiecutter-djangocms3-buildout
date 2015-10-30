# -*- coding: utf-8 -*-
"""
Django-xiti settings
"""
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'xiti')

# xiti_serverid and xtsite are required values
XITI_CONF = {
    'xiti_serverid': '', # Xiti server ID for usage on http protocole
    'xiti_serverid_secure': '', # Xiti server ID for usage on https protocole
    'xtsite': '', # Xiti site ID, also named 's'
    'xtn2': '', # level 2 site ID, also named 's2'
    'xtpage': '', # page name (with the use of :: to create chapters), also named 'p'
    'xtdi': '', # implication degree, also named 'di'
    'xt_an': '', # user ID, also named 'an'
    'xt_ac': '', # category ID, also named 'ac'
    'xt_multc': '', # all the xi indicators (like "&x1=...&x2=....&x3=...")
}