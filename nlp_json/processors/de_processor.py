from spacy.lang.de.tag_map import TAG_MAP

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
    sentences = nlp(sentences_str).sents
    sentences_tokens = []

    for i, sentence in enumerate(sentences):
        sentence = sentence.as_doc()
        sentences_tokens.append([])

        for token in sentence:
            clean_token = {}
            clean_token['text']     = token.text
            clean_token['norm']     = token.norm_
            clean_token['lemma']    = token.lemma_
            clean_token['pos']      = token.pos_
            clean_token['index']    = token.i
            clean_token['feats']    = TAG_MAP[token.tag_]

            # TODO hack to remove POS/74 key from clean_token['feats'] dict
            clean_token['feats'].pop(74, None)

            sentences_tokens[i].append(clean_token)

    return sentences_tokens
