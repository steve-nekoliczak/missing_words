from spacy.symbols import ORTH, NORM, LEMMA


model = 'de_core_news_sm'

# TODO add exhaustive list of custom special cases for article contractions like
# am and zur. These are ones I've personally seen.
special_cases = {
    # an
    'am': [{ORTH: 'am', NORM: 'an dem', LEMMA: 'an der'}],
    'ans': [{ORTH: 'ans', NORM: 'an das', LEMMA: 'an der'}],

    # auf
    'aufs': [{ORTH: 'aufs', NORM: 'auf das', LEMMA: 'auf der'}],

    # bei
    'beim': [{ORTH: 'beim', NORM: 'bei dem', LEMMA: 'bei der'}],

    # darauf
    'drauf': [{ORTH: 'drauf', NORM: 'darauf', LEMMA: 'darauf'}],

    # in
    'im': [{ORTH: 'im', NORM: 'in dem', LEMMA: 'in der'}],
    'ins': [{ORTH: 'ins', NORM: 'in das', LEMMA: 'in der'}],

    # von
    'vom': [{ORTH: 'vom', NORM: 'von dem', LEMMA: 'von der'}],

    # zu
    'zum': [{ORTH: 'zum', NORM: 'zu dem', LEMMA: 'zu der'}],
    'zur': [{ORTH: 'zur', NORM: 'zu der', LEMMA: 'zu der'}]
}
