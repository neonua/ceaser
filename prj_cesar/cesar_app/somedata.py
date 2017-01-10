# Models
from cesar_app.models import Word

# Constants
DIC = {chr(x): x-97 for x in range(97, 123)}  # dictionary generator English alphabet {'a':0, 'b':1, ... 'z':25}
DIC2 = {x-97: chr(x) for x in range(97, 123)}  # Dictionary generator English alphabet {0:'a', 1:'b', ... 25:'z'}
DIC_CNT = len(DIC)  # number symbols = 26


def crypt(text, shift=3):
    """
    Encryption text with shift
    The input is a words
    """
    output = ''
    for i in text:
        if i == ' ':
            output += ' '
        else:
            output += DIC2[(DIC[i] + shift) % DIC_CNT]
    return output


def encrypt(text, shift=3):
    """
    Cryption text with shift.
    The input is a words
    """
    output = ''
    for i in text:
        if i == ' ':
            output += ' '
        else:
            output += DIC2[(DIC[i] - shift) % DIC_CNT]
    return output


def list_count(cnt):
    """
    Conversion dictionary in to list.
    The input is a dict
    """
    cnt_l = []
    for key, value in cnt.items():
        temp = [key, value]
        cnt_l.append(temp)
    return cnt_l


def count(text):
    """
    Counting characters without spaces.
    The input is a words
    """
    cnt = {}
    for i in text:
        if i != ' ':
            if i not in cnt:
                cnt[i] = 1
            else:
                cnt[i] += 1
    return list_count(cnt)


def find_key(list_text):
    """
    Determining whether the text is encrypted,
    and if so, trying to find a displacement shift.
    The input is a list of words
    """
    n_shift = 0  # start shift (0-25)
    ln_list_text = len(list_text)
    cnt_n = 0  # counter indices in the list
    say = ''  # output string
    if len(list_text) >= 1:
        model = Word.objects.filter(name=list_text[0])  # find first word in list
        if model:
            say = 'Your text not crypted, key = {0}'.format(n_shift)
        else:
            while (not model) and (cnt_n < ln_list_text):
                output_n = encrypt(list_text[cnt_n], n_shift)  # cryption word list index
                model = Word.objects.filter(name=output_n)  # find current index word in list
                if not model:
                    say = 'Not founded'
                else:
                    say = 'Your text is crypted! Try key {0}'.format(n_shift)  # gives shift
                    break  # if word in model found - end cycle
                n_shift += 1
                if n_shift >= 26:
                    cnt_n += 1  # if word not founded - get next word in list
                    n_shift = 0  # zeroing shift
    return say
