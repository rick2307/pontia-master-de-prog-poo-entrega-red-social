from red_social.usuario import Usuario
from red_social.publicacion import Tweet, Respuesta, Retweet
from red_social.red import RedSocial


def main():
    ricardo = Usuario("Ricardo", "rick1")
    ana = Usuario("Ana", "@anita")
    jose = Usuario("Jose", "jj")
    juan = Usuario("Juan", "juan")
    print(ricardo.alias)
    print(ricardo.nombre)
    print(f"imprimiendo objeto ricardo: {ricardo}")
    print(ricardo.seguidos)
    ricardo.seguir(ana)

    ricardo.seguir(jose)
    ricardo.sigue_a(ana)
    # ricardo.seguir(ricardo)
    print(ricardo.seguidos)
    print(ricardo.numero_seguidos)
    print(ricardo.sigue_a(juan))
    print(ricardo.sigue_a(Usuario("Juan", "@juan")))

    print(ricardo.seguidos)
    print(juan == Usuario("Juan", "@juan"))

    tweet = Tweet(
        ricardo,
        "Soy DevOps y estoy cursando el master DE #python #devops #cloud #data #engineering",
    )

    print(tweet)
    print(tweet.autor)
    print(tweet.texto)
    print(tweet.hashtags)

    print(tweet.me_gusta)
    tweet.dar_me_gusta()
    print(tweet.me_gusta)

    resp = Respuesta(ana, "Bienvenido al master #data #engineering", tweet)

    retweet = Retweet(jose, tweet)
    retweet2 = Retweet(ricardo, resp)

    print(resp)
    print(retweet)
    print(retweet2)

    red = RedSocial.desde_json("datos/usuarios.json")
    print(red.usuarios)
    print(red.publicaciones)
    # red.anadir(ana)
    # print(red.usuarios)
    pedro = red.registrar("Pedro", "pedro")
    print(red.usuarios)
    print(pedro)

    hola = red.publicar(Tweet(ricardo, "estoy solo"))

    print(hola)
    print(red.publicaciones)

    luis = red.usuarios["@luis"]
    print(luis.sigue_a(red.usuarios["@ana"]))
    print(luis.numero_seguidos)
    print(len(red))

    for usuario in red:
        print(usuario)

    print("@ana" in red)
    print("@pablo" in red)

    print(red["@ana"])
    red = RedSocial.desde_json("datos/usuarios.json")
    ana = red["@ana"]
    luis = red["@luis"]

    red.publicar(Tweet(ana, "Linda vida #life"))

    print(red.timeline(luis))
    for pub in red.timeline(luis):
        print(pub)

    red.mostrar_timeline("@ana")

    red.tendencias()
    print(red.tendencias())


main()

# from red_social.usuario import Usuario

# ana = Usuario("Ana", "ana")  # sin @
# luis = Usuario("Luis", "@luis")  # con @

# # 1) alias
# assert ana.alias == "@ana"

# # 2) str exacto (como en el enunciado)
# print(repr(str(ana)))  # ¿sale exactamente 'Ana (@ana)' ?

# # 3) seguir / sigue_a / numero
# ana.seguir(luis)
# assert ana.sigue_a(luis) is True
# assert luis.sigue_a(ana) is False
# assert ana.numero_seguidos == 1

# # 4) errores
# try:
#     ana.seguir(luis)
#     print("FALLO: debía lanzar ValueError (ya lo sigue)")
# except ValueError:
#     print("OK: ya lo sigue")

# try:
#     ana.seguir(ana)
#     print("FALLO: debía lanzar ValueError (sí mismo)")
# except ValueError:
#     print("OK: sí mismo")

# # 5) igualdad por alias (objetos distintos, mismo alias)
# ana2 = Usuario("Ana", "@ana")
# assert ana == ana2

# # 6) ida y vuelta dict
# datos = ana.a_dict()
# assert datos == {"nombre": "Ana", "alias": "@ana"}
# ana_recuperada = Usuario.desde_dict(datos)
# assert ana_recuperada == ana
# assert ana_recuperada.nombre == "Ana"
# print("OK: desde_dict")
