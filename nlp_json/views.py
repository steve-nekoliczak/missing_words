from rest_framework.decorators import api_view
from django.http import HttpResponse

from .processor import generate_tokens

@api_view(['GET'])
def process_sentence(request, sentence):
    tokens = generate_tokens(sentence)
    return HttpResponse(tokens)
