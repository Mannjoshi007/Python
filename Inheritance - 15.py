class Domestic:
    classification="These animals can be kept at home."

class dogs(Domestic):
    typeof="Dogs are a part of the domestic animals."

class labrador(dogs):
    info="labarador is a kind of dog."

owner=labrador()
print(labrador.classification)
print(labrador.typeof)
print(labrador.info)