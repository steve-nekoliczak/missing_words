import spacy

from .lang_configs import de_config


# TODO be able to set language somewhere more convenient
lang = 'de'

models = {
    'de': de_config.model
}
nlp = spacy.load(models[lang])

special_cases = {
    'de': de_config.special_cases
}
if lang in special_cases:
    for word, case in special_cases[lang].items():
        nlp.tokenizer.add_special_case(word, case)
