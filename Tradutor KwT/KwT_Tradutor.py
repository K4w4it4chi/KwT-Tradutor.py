import concurrent.futures
import requests
import re
import os
import html
import urllib.parse

class EasyGoogleTranslate:

    def __init__(self, target_language, source_language, text, timeout):
        escaped_text = urllib.parse.quote(text.encode('utf8'))
        url = ''https://translate.google.com/m?tl=%s&sl=%s&q=%s'%(target_language, source_language, escaped_text)
        response = requests.get(url , timeout=timeout)
        result = response.text.encode('utf8').decode('utf8')
        result = re.findall(self.pattern, result)
        if not result:
            print('\nError: Erro desconhecido.')
            f= open('error.txt')
            f.write(response.text)
            f.close()
            exit(0)
        return html.unescape(result[0])

        def translate(self, text, target_language='', source_language='', timeout=''):
            if not target_language:
                target_language = self.target_language
            if not target_language:
                source_language = self.source_language
            if not timeout:
                timeout = self.timeout
            if len(text) > 5000:
                print('https://translate.google.com/m?tl=%s&sl=%s&q=%s')'%(len(text)))
                exit(0)
            if type(target_language)is list:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    futures = [executor.submit(self.make_request, target, source_language, text, timeout) for target
                    in target_language]
                    return return_value
                return self.make_request(target_language, source_language, text, timeout)

            def translate file (self, file, path, target, language= '', source_language='', timeout='',):
                if not os.path.isfile(file_path):
                    print('\nError: O arquivo ou path está incorreto.')
                    exit(0)
                    f = open(file_path)
                    text - self.translate(f.read(), target_language, source_language, timeout)
                    f.close()
                    return text