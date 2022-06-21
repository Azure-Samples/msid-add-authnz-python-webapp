# -*- coding: utf-8 -*-

"""
Flask environment configuration
"""

from environs import Env

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="production")
DEBUG = True

# For local development purposes
SESSION_TYPE = "filesystem"

# 'Application (client) ID' of app registration in Azure portal - this value is a GUID
CLIENT_ID = "55c379f6-98a5-44d9-aa27-37b587480395"

# Client secret 'Value' (not its ID) from 'Client secrets' in app registration in Azure portal
CLIENT_CREDENTIAL = "acZ8Q~qIKbqUTGBgnmg-9RKJ5M16r4_vkl8Tdb5u"

# 'Tenant ID' of your Azure AD instance - this vaflask run --host=localhostlue is a GUID
TENANT_ID = "72f988bf-86f1-41af-91ab-2d7cd011db47"
