import paralleldots

paralleldots.set_api_key('miA4TUQQ5NP60P6ffTAAo42fnnYCAZ8IUk75FPbxhtY')

def ner(text):
    ner = paralleldots.ner(text)
    return ner
