# Django
from django.shortcuts import render, HttpResponse

# Forms
from cesar_app.forms import SampleForm

# local constants and functions
from cesar_app.somedata import crypt, encrypt, count, find_key

# standard python library
import re
import json


def index(request):
    """
    Caesar cipher. Draws and takes 2 fields for processing:
    text and shift. It allows you to crypt or encrypt text
    using the shift. The output sends the encrypted or crypted
    text. Just go count the number of incoming letters and
    it is checked whether or not the encrypted code.
    """
    if request.POST and request.is_ajax():
        text = request.POST['text'].strip().lower()  # incoming text
        shift = int(request.POST['shift']) % 25  # incoming shift
        regex = re.search(r'[^a-zA-Z \',.:"?!]', text)  # check regex
        output = ''  # text to be output
        cnt = {}  # count letters
        data = {}  # output data
        say = ''  # response determination test

        if not regex and text != '':
            if 'crypt' == request.POST['name']:
                output = crypt(text, shift)  # decoding text
                cnt = sorted(count(text))  # a list of the number of characters
            elif 'encrypt' == request.POST['name']:
                output = encrypt(text, shift)  # coding text
                cnt = sorted(count(text))  # a list of the number of characters
            elif 'auto' == request.POST['name']:
                list_text = text.split()  # split the text into a list
                if len(list_text) >= 1:
                    cnt = sorted(count(text))  # a list of the number of characters
                    say = find_key(list_text)  # response determination test

        else:
            if regex:
                output = 'error regex: {0}'.format(regex.string)  # gives regex error
            elif text == '':
                output = 'Text is empty'  # gives empty error

        data['cnt'] = cnt
        data['say'] = say
        data['text'] = output
        data['cnt'] = cnt
        data = json.dumps(data)  # packaging to json

        return HttpResponse(data, content_type='application/json')

    else:
        form = SampleForm()  # drawing form
        return render(request, 'index.html', {'form': form})
