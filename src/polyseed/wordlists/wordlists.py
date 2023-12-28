import os


# This Library is heavily based on the trezor python mnemonic library 
# https://github.com/trezor/python-mnemonic/blob/master/src/mnemonic/mnemonic.py#L81


from typing import AnyStr, List, TypeVar, Union


class ConfigurationError(Exception):
    pass

class wordlists():
    def __init__(self, language: str = "english"):
        self.language = language 
        self.radix = 2048        
        d = os.path.join(os.path.dirname(__file__), f"{language}.txt")
        if os.path.exists(d) and os.path.isfile(d):
            with open(d, "r", encoding="utf-8") as f:
                self.wordlist = [w.strip() for w in f.readlines()]
            if len(self.wordlist) != self.radix:
                raise ConfigurationError(
                    f"Wordlist should contain {self.radix} words, but it's {len(self.wordlist)} words long instead."
                )
        else:
            raise ConfigurationError("Language not detected")
        # Japanese must be joined by ideographic space
        self.delimiter = "\u3000" if language == "japanese" else " "
    
    @staticmethod
    def normalize_string(txt: AnyStr) -> str:
        if isinstance(txt, bytes):
            utxt = txt.decode("utf8")
        elif isinstance(txt, str):
            utxt = txt
        else:
            raise TypeError("String value expected")

        return unicodedata.normalize("NFKD", utxt)
