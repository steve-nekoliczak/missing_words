import spacy
from spacy.lang.de.tag_map import TAG_MAP as tag_map

nlp = spacy.load('de_core_news_sm')

# TODO add custom special cases for article contractions like zum and zur
