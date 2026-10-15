class Usuario:
    def __init__(self, nombre, alias):
        self.nombre = nombre
        if alias[0] != "@":
            alias = "@" + alias
        self.alias = alias
        self.seguidos = []

    def seguir(self, otro):
        if otro in self.seguidos:
            raise ValueError("ya lo sigue")
        elif otro == self:
            raise ValueError(f"{otro} es él mismo")
        else:
            self.seguidos.append(otro)

    def sigue_a(self, otro):
        return otro in self.seguidos

    def a_dict(self):
        return {"nombre": self.nombre, "alias": self.alias}

    @property
    def numero_seguidos(self):
        return len(self.seguidos)

    @classmethod
    def desde_dict(cls, user):
        nombre, alias = user.values()
        return cls(nombre, alias)

    def __str__(self):
        return f"{self.nombre} ({self.alias})"

    def __eq__(self, otro):
        return self.alias == otro
