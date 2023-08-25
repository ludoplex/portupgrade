import singleton
import enumerable
import PkgDBTools

class PortsDB(singleton, enumerable, PkgDBTools):
    DB_VERSION = [:FreeBSD, 4]

    LANGUAGE_SPECIFIC_CATEGORIES = {
        "arabic": "ar-",
        "chinese": "zh-",
        "french": "fr-",
        "german": "de-",
        "hebrew": "iw-",
        "hungarian": "hu-",
        "japanese": "ja-",
        "korean": "ko-",
        "polish": "pl-",
        "portuguese": "pt-",
        "russian": "ru-",
        "ukrainian": "uk-",
        "vietnamese": "vi-",
    }

    MY_PORT = 'ports-mgmt/portupgrade'

    LOCK_FILE = '/var/run/portsdb.lock'

    def __init__(self):
        self.ignore_categories = None
        self.extra_categories = None
        self.moved = None

    # Add the rest of the methods from the Ruby class, translated to Python
