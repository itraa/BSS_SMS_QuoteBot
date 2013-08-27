'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "AC323482260fcfd2a8e99b645f8bbd35f2" 
AUTH_TOKEN = "3910c7132741b59b7e8526a42a771b3a"
BSSSPAM_APP_SID = "AP9f4df1a0df10f601ecfb6943d338d6f8"
BSS_SPAM_ID = "240-752-6723"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
