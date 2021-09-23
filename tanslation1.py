from translate import Translator
translator = Translator(from_lang="english", to_lang="arabic")
translation = translator.translate("My Name is Rashad")
print(translation)
