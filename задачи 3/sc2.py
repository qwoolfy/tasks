def replace_end_punctuation(text):
    text = text.rstrip()
    
    while text.endswith('?') or text.endswith('!'):
        if text.endswith('??'):
            text = text[:-2] + '?'
        elif text.endswith('!!'):
            text = text[:-2] + '!'
        elif text.endswith('?'):
            text = text[:-1] + '?'
        elif text.endswith('!'):
            text = text[:-1] + '!'
        else:
            break
    
    return text

a = "Что ты делаешь?????"

print(replace_end_punctuation(a))
