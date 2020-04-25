from django.http import HttpResponse
from rest_framework.decorators import api_view

from nlp_json import lang
from .processors import de_processor


@api_view(['GET'])
def process_sentences(request):
    sentences = request.GET.get('sentences')
    tokens = ''
    if lang == 'de':
        tokens = de_processor.generate_tokens(sentences)
    else:
        pass
        # return HttpResponse(404 or something like that)
    return HttpResponse(tokens)
