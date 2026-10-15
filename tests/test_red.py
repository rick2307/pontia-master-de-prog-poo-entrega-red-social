import json

from red_social.publicacion import Tweet
from red_social.red import RedSocial


def test_timeline_solo_tiene_publicaciones_de_los_seguidos(red):
    ana = red["@ana"]
    luis = red["@luis"]
    t1 = red.publicar(Tweet(ana, "primero"))
    t2 = red.publicar(Tweet(ana, "segundo"))
    red.publicar(Tweet(luis, "de luis"))

    assert red.timeline(luis) == [t2, t1]
    assert red.timeline(ana) == []


def test_desde_json_construye_usuarios_y_seguimientos(mocker):
    contenido = json.dumps(
        {
            "usuarios": [
                {"nombre": "Ana", "alias": "@ana"},
                {"nombre": "Luis", "alias": "@luis"},
            ],
            "seguimientos": [["@luis", "@ana"]],
        }
    )
    ruta = "cualquier/ruta.json"
    abrir_falso = mocker.patch("builtins.open", mocker.mock_open(read_data=contenido))

    red = RedSocial.desde_json(ruta)

    abrir_falso.assert_called_once_with(ruta, encoding="utf-8")
    assert len(red) == 2
    assert red["@luis"].sigue_a(red["@ana"])
    assert red["@ana"].sigue_a(red["@luis"]) is False
