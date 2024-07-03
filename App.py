import justpy as jp
from translate import Translator

def translate_text(text, dest_lang='en'):
    translator = Translator(to_lang=dest_lang)
    try:
        # Attempt to translate the text directly (if within 500 characters)
        return translator.translate(text)
    except Exception as e:
        print(f"Translation error: {str(e)}")
        return "Translation failed."

'''
if text exceeds 500 characters use this: 
def split_text(text, limit=500):
    # Splits the text into chunks of a specified size
    return [text[i:i+limit] for i in range(0, len(text), limit)]

def process_text(text, dest_lang):
    # Split text into manageable parts
    parts = split_text(text)
    results = []
    # Process each part using the API
    for part in parts:
        result = translate_text(part, dest_lang)  # Process each chunk
        results.append(result)
    # Combine the results back into one response
    return " ".join(results)
'''
def create_header():
    header = jp.Div(classes="w-full bg-blue-900 text-white py-4")
    jp.H1(a=header, text="Text Translator App", classes="text-4xl font-bold text-center")
    nav = jp.Div(a=header, classes="flex justify-center space-x-4 mt-2")
    jp.A(a=nav, text="Home", href="/", classes="text-white hover:text-gray-200")
    jp.A(a=nav, text="About", href="/about", classes="text-white hover:text-gray-200")
    return header

def create_footer():
    footer = jp.Div(classes="w-full bg-gray-800 text-white py-3")
    jp.P(a=footer, text="Author: Maheen Asim", classes="text-center")
    return footer

def main_page():
    wp = jp.WebPage()
    wp.add(create_header())
    wp.body_style = 'background: linear-gradient(to right, #dae2f8, #d6a4a4);'  
    main_container = jp.Div(a=wp, classes="flex justify-center items-center h-screen")
    yellow_square = jp.Div(a=main_container, style="width: auto; height: auto; background-color: lightblue; border: 2px solid black; padding: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.5); border-radius: 15px;", classes="flex flex-col items-center")

    jp.Div(a=yellow_square, text="Please write the text you want to translate in English and specify the destination language code. For more information on each language's code, please view the About section.", classes="m-2 text-lg text-center")
    input_box = jp.Input(a=yellow_square, placeholder="Enter text in English to translate", classes="m-2 p-2 w-full")
    lang_input = jp.Input(a=yellow_square, placeholder="Enter destination language code (e.g., 'es')", classes="m-2 p-2 w-full")
    output = jp.Div(a=yellow_square, text="Translation appears here", classes="m-2 p-2 text-red-700 text-2xl")
    button = jp.Button(a=yellow_square, text='Translate', classes="m-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded")

    def on_click(self, msg):
        translated_text = translate_text(input_box.value, lang_input.value)
        output.text = translated_text

    button.on('click', on_click)
    wp.add(create_footer())
    return wp

def about_page():
    wp = jp.WebPage()
    wp.add(create_header())
    wp.body_style = 'background: linear-gradient(to right, #dae2f8, #d6a4a4);'
    content = jp.Div(a=wp, classes="m-4 p-4", style="max-width: 800px; margin: auto;")
    jp.H2(a=content, text="Supported Languages", classes="text-2xl font-bold")
  #could add more langaugaes here
    languages_info = """ Here are the codes:english - en, chinese - zh, arabic - ar, russian - ru, french - fr, german - de, spanish - es, portuguese - pt, 
    italian - it, japanese - ja, korean - ko, greek - el, dutch - nl, hindi - hi, turkish - tr,
    malay - ms, thai - th, vietnamese - vi, indonesian - id, hebrew - he, polish - pl, mongolian - mn, czech - cs, 
    hungarian - hu, estonian - et, bulgarian - bg, 
    danish - da, finnish - fi, romanian - ro, swedish - sv, slovenian - sl, persian/farsi - fa, 
    bosnian - bs, serbian - sr, fijian - fj, filipino - tl, haitian creole - ht, catalan - ca, croatian - hr, latvian - lv, lithuanian - lt, 
    urdu - ur, ukrainian - uk, welsh - cy, tahiti - ty, tongan - to, swahili - sw, samoan - sm, slovak - sk, afrikaans - af, norwegian - no, bengali - bn, malagasy - mg, maltese - mt, 
    quechua otomi - otq, klingon/tlhingan hol - tlh, 
    gujarati - gu, tamil - ta, telugu - te, punjabi - pa, amharic - am, azerbaijani - az, bashkir - ba, belarusian - be, cebuano - ceb, 
    chuvash - cv, esperanto - eo, basque - eu, irish - ga, emoji - emj, and more."""
    languages_div = jp.Div(a=content, text=languages_info, classes="overflow-auto h-64 border-2 border-gray-400 p-2", style="background-color: #f0f0f0;")
    wp.add(create_footer())
    return wp

# Routes
jp.Route("/", main_page)
jp.Route("/about", about_page)

# Run the JustPy app
jp.justpy(port=8000)
