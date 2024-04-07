from pydantic import BaseModel
from enum import Enum

from .funcs import remove_custom_bbcodes, remove_bbcode, remove_urls, remove_shiki_smileys, remove_emoji, \
    remove_emoticons, remove_punctuation, remove_multi_spaces, remove_numeric, remove_ratings


class Feature(Enum):
    LOWER_CASE = 'lower_case'
    STRIP = 'strip'
    REMOVE_PUNCTUATION = 'remove_punctuation'
    REMOVE_EMOJI = 'remove_emoji'
    REMOVE_EMOTICONS = 'remove_emoticons'
    REMOVE_MULTI_SPACES = 'remove_multi_spaces'
    REMOVE_URLS = 'remove_urls'
    REMOVE_NONES = 'remove_nones'
    REMOVE_NUMERIC = 'remove_numeric'
    REMOVE_BBCODE = 'remove_bbcode'
    REMOVE_CUSTOM_BBCODES = 'remove_custom_bbcodes'
    REMOVE_RATING = 'remove_rating'
    REMOVE_SHIKI_SMILEYS = 'remove_shiki_smileys'


class CleanUp(BaseModel):
    text: str
    features: str


def clean_text(body: CleanUp):
    if len(body.text) == 0:
        return {"result": "", "empty": True}

    text = body.text
    features = body.features
    if len(features) == 0:
        return {"result": body.text}

    need_to_lower = Feature.LOWER_CASE.value in features
    need_to_remove_punctuation = Feature.REMOVE_PUNCTUATION.value in features
    need_to_remove_emoji = Feature.REMOVE_EMOJI.value in features
    need_to_remove_emoticons = Feature.REMOVE_EMOTICONS.value in features
    need_to_remove_multi_spaces = Feature.REMOVE_MULTI_SPACES.value in features
    need_to_remove_urls = Feature.REMOVE_URLS.value in features
    need_to_strip = Feature.STRIP.value in features
    need_to_remove_numeric = Feature.REMOVE_NUMERIC.value in features
    need_to_remove_bbcode = Feature.REMOVE_BBCODE.value in features
    need_to_remove_custom_bbcodes = Feature.REMOVE_CUSTOM_BBCODES.value in features
    need_to_remove_ratings = Feature.REMOVE_RATING.value in features
    need_to_remove_shiki_smileys = Feature.REMOVE_SHIKI_SMILEYS.value in features

    if need_to_lower:
        text = text.lower()

    if need_to_remove_custom_bbcodes:
        text = remove_custom_bbcodes(text)

    if need_to_remove_bbcode:
        text = remove_bbcode(text)

    if need_to_remove_urls:
        text = remove_urls(text)

    if need_to_remove_shiki_smileys:
        text = remove_shiki_smileys(text)

    if need_to_remove_emoji:
        text = remove_emoji(text)

    if need_to_remove_emoticons:
        text = remove_emoticons(text)

    if need_to_remove_punctuation:
        text = remove_punctuation(text)

    if need_to_remove_multi_spaces:
        text = remove_multi_spaces(text)

    if need_to_strip:
        text = text.strip()

    if need_to_remove_numeric:
        text = remove_numeric(text)

    if need_to_remove_ratings:
        text = remove_ratings(text)

    return {"result": text}
