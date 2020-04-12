from nlp_json import nlp, tag_map
import pdb

def generate_tokens(sentences_str):
    sentences = nlp(sentences_str).sents
    sentences_tokens = []

    for i, sentence in enumerate(sentences):
        sentence = sentence.as_doc()
        sentences_tokens.append([])

        for token in sentence:
            word = {}
            word['text'] = token.text

            # if len(token.words) > 1:
            #     word = token.words[1]
            #     word.lemma = token.words[0].norm_ + ' ' + token.words[1].norm_
        # else:
            word['norm'] = token.norm_
            word['lemma'] = token.lemma_
            word['pos'] = token.pos_
            word['index'] = token.i

            word['feats'] = tag_map[token.tag_]
            # TODO hack to remove POS/74 key from word['feats'] dict
            word['feats'].pop(74)

            sentences_tokens[i].append(word)

    return sentences_tokens
