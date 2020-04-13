import stanza

from .lang_configs import de_config


# TODO be able to set language somewhere more convenient
lang = 'de'

processors = {
    'de': de_config.processors
}
nlp = stanza.Pipeline(lang=lang, processors=processors[lang])
