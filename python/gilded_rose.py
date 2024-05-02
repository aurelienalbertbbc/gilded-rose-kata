# -*- coding: utf-8 -*-
# Mais d'abord, laissez-moi vous présenter notre système :
#
# - Tous les éléments ont une valeur `sellIn` qui désigne le nombre de jours restant pour vendre l'article.
# - Tous les articles ont une valeur `quality` qui dénote combien l'article est précieux.
# - À la fin de chaque journée, notre système diminue ces deux valeurs pour chaque produit.
#
# Plutôt simple, non ?
#
# Attendez, ça devient intéressant :
#
# - Une fois que la date de péremption est passée, la qualité se dégrade deux fois plus rapidement.
# - La qualité (`quality`) d'un produit ne peut jamais être négative.
# - "Aged Brie" augmente sa qualité (`quality`) plus le temps passe.
# - La qualité d'un produit n'est jamais de plus de 50.
# - "Sulfuras", étant un objet légendaire, n'a pas de date de péremption et ne perd jamais en qualité (`quality`)
# - "Backstage passes", comme le "Aged Brie", augmente sa qualité (`quality`) plus le temps passe (`sellIn`) ; La qualité augmente de 2 quand il reste 10 jours ou moins et de 3 quand il reste 5 jours ou moins, mais la qualité tombe à 0 après le concert.

# Nous avons récemment signé un partenariat avec un fournisseur de produit invoqué ("Conjured"). Cela nécessite une mise à jour de notre système :
#
# les éléments "Conjured" voient leur qualité se dégrader de deux fois plus vite que les objets normaux.

# to do
# Type de produit en châine de caractères -> passer en Enum ?
#



# # At the end of the day: reduce sell date, update quality
# sellDelta = 1
# qualityDelta = 1
#
# if sellDelta < 0:
# 	pass # When sell date is expired, its quality degrades 2 times faster
#
# # Some items have specific rules
# if item.name = "Sulfuras":
# 	sellDelta = 0
# 	qualityDelta = 0
#
#
# item.sellIn -= sellDelta
# item.quality -= qualityDelta
#
# # Quality must be between 0 and 50
# item.quality = max(0, min(item.quality, 50))

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
