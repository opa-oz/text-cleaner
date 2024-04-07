import re

import bbcode

from .consts import ratings, custom_bbcodes, emoticon_pattern, emoji_pattern, punct_to_remove, smiley_groups


def remove_ratings(text):
    for regex in ratings:
        text = regex.sub('', text)
    return text


def remove_custom_bbcodes(text):
    for regex in custom_bbcodes:
        text = regex.sub('', text)

    return text


def remove_urls(text):
    return re.sub(r'^https?://.*[\r\n]*', '', text, flags=re.MULTILINE)


def remove_numeric(text):
    if text.isnumeric():
        return None

    return text


def remove_multi_spaces(text):
    return ' '.join(text.split())


def remove_emoticons(text):
    return emoticon_pattern.sub(r'', text)


# Reference : https://gist.github.com/slowkow/7a7f61f495e3dbb7e3d767f97bd7304b
def remove_emoji(text):
    return emoji_pattern.sub(r'', text)


def remove_punctuation(text):
    return text.translate(str.maketrans('', '', punct_to_remove))


def remove_bbcode(text):
    parser = bbcode.Parser()

    return parser.strip(text)


def remove_shiki_smileys(text):
    for smile_group in smiley_groups:
        for smile in smile_group:
            text = text.replace(smile, '')

    return text
