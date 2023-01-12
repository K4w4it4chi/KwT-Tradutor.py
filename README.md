


# KwT!-Tradutor.py
*EM DEV* Este é um tradutor em python com o plugin Easy google translate, basicamente eu fiz para eu estudar e traduzir com meus pdfs e ebooks ^^,

'------'  '-----'--------------------------'------'  '------'

 API não oficial do Google Tradutor.
 Esta biblioteca não precisa de uma chave de api ou outra coisa para usar, é gratuita e simples.
 Você pode usar uma cadeia de caracteres ou um arquivo para traduzir, mas o texto deve ser igual ou inferior a 5000 caracteres.
 Você pode dividir seu texto em 5000 caracteres para traduzir mais.
 O Google Tradutor é compatível com 108 idiomas diferentes. Você pode usar qualquer um deles como idioma de origem e de destino neste aplicativo.
 Se o idioma de origem não for especificado, ele detectará o idioma de origem automaticamente.
 Este aplicativo suporta tradução multi thread, você pode usá-lo para traduzir vários idiomas de uma só vez.
 A lista detalhada de idiomas pode ser encontrada aqui: https://cloud.google.com/translate/docs/languages
 Exemplos:
 # 1: Especifique o idioma de origem e de destino padrão no início e use-o a qualquer momento.
 tradutor = GoogleTranslateRequest(
 source_language='in',
                    target_language='de',
 tempo limite=10
                )
 result = translator.translate('Este é um exemplo.')
 impressão(resultado)
 # 2: Não especifique parâmetros padrão.
 tradutor = GoogleTranslateRequest()
 result = translator.translate('Este é um exemplo.', target_language='tr')
 impressão(resultado)
 # 2: Substitua os parâmetros padrão.
 tradutor = GoogleTranslateRequest(target_language='tr')
 result = translator.translate('Este é um exemplo.', target_language='fr')
 impressão(resultado)
 # 4: Traduza um texto em vários idiomas ao mesmo tempo via multi-threading.
 tradutor = GoogleTranslateRequest()

 result = translator.translate(text='Este é um exemplo.', target_language=['tr', 'fr', 'de'])
 impressão(resultado)
 # 5: Traduza um arquivo em vários idiomas de uma só vez via multi-threading.
 tradutor = GoogleTranslateRequest()
 resultado = translator.translate_file(file_path='text.txt', target_language=['tr', 'fr', 'de'])
 impressão(resultado)
 
 Obrigado pela atenção ! <3
 [07008a0341d125fcccd77ad7a77acbfd](https://user-images.githubusercontent.com/122295876/212157597-3e33a387-26b2-4e9a-bfe3-656300437d7c.gif)
