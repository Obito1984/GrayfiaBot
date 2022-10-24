import sentry_sdk
from sentry_sdk.integrations.redis import RedisIntegration

from Bestie_Robot.config import get_str_key
from Bestie_Robot.utils.logger import log

log.info("Starting sentry.io integraion...")

sentry_sdk.init(get_str_key("SENTRY_API_KEY"), integrations=[RedisIntegration()])
