from abc import ABC, abstractmethod

LIMITE_CATACTERES = 280


class Publicacion(ABC):
    @abstractmethod
    def __init__(self, autor, texto):

        self.me_gusta = 0

        if texto.strip() == "":
            raise ValueError("Texto no puede estar vacio")
        if len(texto) > LIMITE_CATACTERES:
            raise ValueError(f"Contiene mas de {LIMITE_CATACTERES} caracteres")

        self.autor = autor
        self.texto = texto

    def dar_me_gusta(self):
        self.me_gusta = self.me_gusta + 1

    @property
    def hashtags(self):
        return self.extraer_hashtags(self.texto)

    @staticmethod
    def extraer_hashtags(texto):
        list_hashtags = []
        for palabra in texto.split():
            if not palabra.startswith("#") or palabra == "#":
                continue
            hashtag = palabra.lower().rstrip(",.;:!?¡¿")
            if hashtag != "#" and hashtag not in list_hashtags:
                list_hashtags.append(hashtag)
        return list_hashtags

    @abstractmethod
    def __str__(self):
        pass


class Tweet(Publicacion):
    def __init__(self, autor, texto):
        super().__init__(autor, texto)

    def __str__(self):
        return f"{self.autor.alias}: {self.texto}"


class Respuesta(Publicacion):
    def __init__(self, autor, texto, original):
        super().__init__(autor, texto)

        self.original = original

    def __str__(self):
        return f"{self.autor.alias} ↩ {self.original.autor.alias}: {self.texto}"


class Retweet(Publicacion):
    def __init__(self, autor, original):
        super().__init__(autor, original.texto)
        self.original = original

    def __str__(self):
        return f"{self.autor.alias} 🔁 {self.original}"
