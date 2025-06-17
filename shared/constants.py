"""
Shared constants for the Synth911 application.
Contains configuration values and options used across multiple modules.
"""

# Default and supported locales for Faker data generation
DEFAULT_LOCALE = "en_US"
SUPPORTED_LOCALES = [
    "en_US",  # American English
    "en_GB",  # British English
    "fr_FR",  # French
    "de_DE",  # German
    "es_ES",  # Spanish
    "it_IT",  # Italian
    "pt_BR",  # Brazilian Portuguese
    "nl_NL",  # Dutch
    "pl_PL",  # Polish
    "ru_RU",  # Russian
    "ja_JP",  # Japanese
    "ko_KR",  # Korean
    "zh_CN",  # Chinese (Simplified)
    "ar_SA",  # Arabic
]

def validate_locale(locale):
    """
    Validate if a given locale is supported.
    
    Args:
        locale (str): The locale string to validate
        
    Returns:
        bool: True if the locale is supported, False otherwise
    """
    return locale in SUPPORTED_LOCALES
