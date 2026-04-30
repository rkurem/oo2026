#Koosta klass Jook, millel on nimetus, liitri omahind ning erikaal. Koosta klass Joogipudel, millel on maht,
#pudelityyp, mass ning taara maksumus. Samuti sees olev Jook, mis võib ka puududa. Koosta Joogipudeli jaoks käsklus, mis leiaks Joogipudeli massi koos Joogiga
#(juhul kui see olemas), samuti käsklus sellise komplekti omahinna leidmiseks. Koosta tööks automaattestid.

class Jook:
    def __init__(self, nimetus, liitri_omahind, erikaal):
        self.nimetus = nimetus
        self.liitri_omahind = liitri_omahind
        self.erikaal = erikaal


class Joogipudel:
    def __init__(self, maht, pudelityyp, mass, taara_maksumus, jook=None):
        self.maht = maht
        self.pudelityyp = pudelityyp
        self.mass = mass
        self.taara_maksumus = taara_maksumus
        self.jook = jook

    def leiaMass(self):
        if self.jook is not None:
            return self.mass + self.maht * self.jook.erikaal
        return self.mass

    def leiaOmahind(self):
        hind = self.taara_maksumus
        if self.jook is not None:
            hind += self.maht * self.jook.liitri_omahind
        return hind

#Koosta klass Joogivaat, millel on ruumala ning sees oleva Joogi kogus liitrites. Koosta käsk etteantud Joogipudeli täitmiseks (juhul kui Jooki jagub).
#Koosta käsklus kogu Joogivaaditäie Joogi villimiseks Joogipudelitesse, tühjad pudelid tuleb käsule ette anda. Koosta töö kontrolliks automaattestid.

class Joogivaat:
    def __init__(self, ruumala, kogus_L, jook):
        self.ruumala = ruumala
        self.kogus_L = kogus_L
        self.jook = jook

    def t2ida_pudel(self, pudel):
        if pudel.jook is not None:
            return False

        if self.kogus_L >= pudel.maht:
            pudel.jook = self.jook
            self.kogus_L -= pudel.maht
            return True

        return False

    def villi_pudelitesse(self, pudelid):
        for pudel in pudelid:
            self.t2ida_pudel(pudel)
            
#Koosta Joogipudelite Kasti jaoks klass. Väljadeks kastityyp, kastihind, kastimass ning pesade arv (mitu pudelit mahub).
#Loo käsklused kasti ja sinna kuuluvate pudelite ühise massi ja omahinna arvutamiseks. Loo käsklus Joogivaadist Kasti sisse pudelite villimiseks. Koosta automaattestid.

class joogipudelite_kast:
    def __init__(self, kastityyp, kastihind, kastimass, pesade_arv):
        self.kastityyp=kastityyp
        self.kastimass=kastimass
        self.pesade_arv=pesade_arv

import unittest


class TestJoogid(unittest.TestCase):

    def test_pudel_ilma_joogita(self):
        pudel = Joogipudel(1.5, "plast", 0.2, 0.1, None)
        self.assertEqual(pudel.leiaMass(), 0.2)
        self.assertEqual(pudel.leiaOmahind(), 0.1)

    def test_pudel_joogiga(self):
        jook = Jook("Fanta", 1.99, 1.99)
        pudel = Joogipudel(2, "plast", 0.2, 0.1, jook)

        self.assertAlmostEqual(pudel.leiaMass(), 0.2 + 2 * 1.99)
        self.assertAlmostEqual(pudel.leiaOmahind(), 0.1 + 2 * 1.99)

    def test_villi_pudelitesse(self):
        jook = Jook("Fanta", 2.0, 1.0)
        vaat = Joogivaat(10, 5, jook)

        pudelid = [
            Joogipudel(1, "Plast", 0.2, 0.1),
            Joogipudel(1, "Plast", 0.2, 0.1),
            Joogipudel(1, "Plast", 0.2, 0.1)
        ]

        vaat.villi_pudelitesse(pudelid)

        self.assertEqual(vaat.kogus_L, 2)

        for p in pudelid:
            self.assertIsNotNone(p.jook)


if __name__ == "__main__":
    unittest.main()
