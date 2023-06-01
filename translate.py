import os

import pyperclip
import deepl

if not os.environ.get("DEEPL_API_KEY"):
    raise RuntimeError("DeepL api key is not set. Please export DEEPL_API_KEY env variable.")

auth_key = os.environ.get("DEEPL_API_KEY")
translator = deepl.Translator(auth_key)

result = translator.translate_text(pyperclip.paste(), target_lang="EN-GB")

pyperclip.copy(result.text)