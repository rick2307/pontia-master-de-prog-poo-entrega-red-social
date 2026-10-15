import json
from collections import Counter

from red_social.usuario import Usuario
from red_social.publicacion import Tweet, Respuesta, Retweet


class RedSocial:
    def __init__(self):
        self.usuarios = {}
        self.publicaciones = []

    def anadir(self, usuario):
        if usuario.alias in self.usuarios:
            raise ValueError("Usuario duplicado")
        self.usuarios[usuario.alias] = usuario
        return usuario

    def registrar(self, nombre, alias):
        return self.anadir(Usuario(nombre, alias))

    def publicar(self, publicacion):
        self.publicaciones.append(publicacion)
        return publicacion

    def timeline(self, usuario):
        publis = []
        for pub in self.publicaciones:
            if usuario.sigue_a(pub.autor):
                publis.append(pub)
        return publis[::-1]

    def tendencias(self, n=3):
        list_hashtags = []
        for hashtags in self.publicaciones:
            for hashtag in hashtags.hashtags:
                list_hashtags.append(hashtag)

        c = Counter(list_hashtags)
        return c.most_common(n)

    def mostrar_timeline(self, alias):
        print()
        usuario = self[alias]
        print(f"Timeline de {self.usuarios[alias]}:")
        for pub in self.timeline(usuario):
            print(f"  {pub}  ♥ {pub.me_gusta}")

    @classmethod
    def desde_json(cls, ruta):
        with open(ruta, encoding="utf-8") as f:
            datos = json.load(f)
        red = cls()
        for usuario in datos["usuarios"]:
            user = Usuario.desde_dict(usuario)
            red.anadir(user)
        for seguimiento in datos["seguimientos"]:
            seguidor = red.usuarios[seguimiento[0]]
            seguido = red.usuarios[seguimiento[1]]
            seguidor.seguir(seguido)

        return red

    def __len__(self):
        return len(self.usuarios)

    def __iter__(self):
        return iter(sorted(self.usuarios.values(), key=lambda x: x.alias))

    def __contains__(self, alias):
        return alias in self.usuarios

    def __getitem__(self, alias):
        return self.usuarios[alias]
