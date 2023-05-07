import threading

from easyjobs import *

config = {
    "inputs": {
        "keywords": ['seo', 'webmarketing', 'wordpress', 'e-commerce'],
        "localization": "Ile-de-France",
        "excluded_keywords": ['stag'],
        "included_keywords": [],
        "contract_type": [],
        "remote": False,
        "minium_salary": 0
    },
    "options": {
        "hide_jobs": False,
        "message_to_recruiter": False,
        "DEBUG": True,
        "headless": False,
        "infinite": True,
        "safe_mode": False
    },
    "presets": {
        "phone": "0665774180",
        "name": "Tom",
        "nom": "Tom",
        "pays": "fr",
        "mail": "zaptom.pro@gmail.com",
        "twitter": "https://twitter.com/tom_zapico",
        "linkedin": "https://www.linkedin.com/in/tom-zapico/",
        "internet": "https://tom-zapico.com"
    },
}


class AutoApply(threading.Thread):
    def __init__(self, name=None, kwargs=None):
        super().__init__()
        if name == "linkedin":
            self.bot = LinkedIn(kwargs)
        elif name == "indeed":
            self.bot = Indeed(kwargs)
        return

    def run(self):
        self.bot.application_loop()
        print('run')
        return


config['user'] = {
    "email": "zaptom.pro@gmail.com",
    "password": "Tom01032000",
    "phone": "0665774180"
}
AutoApply(name="linkedin", kwargs=config).start()

config['user'] = {
    "email": "t.zapico@ldeclic.fr",
    "password": "Tom01032000",
    "phone": "0665774180"
}
AutoApply(name="indeed", kwargs=config).start()


print('hello')
print('hello')
print('hello')
print('hello')
print('hello')
print('hello')
print('hello')

