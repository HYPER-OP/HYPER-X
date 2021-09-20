import os
import sys

import heroku3

from HYPERX import HEROKU_API_KEY, HEROKU_APP_NAME, DEV_USERS
from HYPERX.events import register
from HYPERX.pyrogramee.heroku_helper import HerokuHelper

Heroku = heroku3.from_key(HEROKU_API_KEY)


@register(pattern="^/restart$")
async def _(event):
    if event.fwd_from:
        return
    if event.sender_id == DEV_USERS:
        pass
    else:
        return
    await event.edit("**Restarted HYPER X 👀**")
    try:
        herokuHelper = HerokuHelper(HEROKU_APP_NAME, HEROKU_API_KEY)
        herokuHelper.restart()
    except:
        await borg.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
