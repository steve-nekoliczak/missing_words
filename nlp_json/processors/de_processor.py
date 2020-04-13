from nlp_json import nlp


# EXAMPLE:
# sentences_str = 'Ich bin ein Hund. Du bist eine Katze.'
# What this arg returns (ignoring details for brevity):
# [
#   [
#     { 'Ich' }, { 'bin' }, { 'ein' }, { 'Hund' }, { '.' }
#   ],
#   [
#     { 'Du' }, { 'bist' }, { 'eine' }, { 'Katze' }, { '.' }
#   ],
# ]
def generate_tokens(sentences_str):
    # return nlp(sentences_str)
    sentences = nlp(sentences_str).sentences

    for sentence in sentences:
        for token in sentence.words:
            if token.feats:
                token.feats = dict(x.split('=') for x in token.feats.split('|') if "=" in x)
            if token.misc:
                token.misc = dict(x.split('=') for x in token.misc.split('|') if "=" in x)

    return sentences
