KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.luku_jono = [0] * self.kapasiteetti

        self.alkioiden_maara = 0

    def kuuluu(self, luku):
        if luku in self.luku_jono:
            return True

    def lisaa(self, luku):
        if self.alkioiden_maara == 0:
            self.luku_jono[0] = luku
            self.alkioiden_maara += 1
            return True

        if not self.kuuluu(luku):
            self.luku_jono[self.alkioiden_maara] = luku
            self.alkioiden_maara += 1

            if self.alkioiden_maara % len(self.luku_jono) == 0:
                taulukko_old = self.luku_jono
                self.luku_jono = [0] * (self.alkioiden_maara + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old)

            return True

        return False

    def poista(self, luku):
        kohta = -1
        #self.luku_jono = list(map(lambda x: x.replace(luku,0),self.luku_jono))
        #apu = 0
        for i, c in enumerate(self.luku_jono):
            if luku == c:
                self.luku_jono[i] = 0
                break

        #for i in range(0, self.alkioiden_maara):
        #    if n == self.luku_jono[i]:
        #        kohta = i  # siis luku löytyy tuosta kohdasta :D
        #        self.luku_jono[kohta] = 0
        #        break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_maara - 1):
                apu = self.luku_jono[j]
                self.luku_jono[j] = self.luku_jono[j + 1]
                self.luku_jono[j + 1] = apu

            self.alkioiden_maara = self.alkioiden_maara - 1
            return True

        return False

    def kopioi_taulukko(self, taulukko_old):
        for i, c in enumerate(taulukko_old):
            self.luku_jono[i] = c

    def mahtavuus(self):
        return self.alkioiden_maara

    def to_int_list(self):
        taulu = [0] * self.alkioiden_maara

        for i in range(0, len(taulu)):
            taulu[i] = self.luku_jono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_maara == 0:
            return "{}"
        elif self.alkioiden_maara == 1:
            return "{" + str(self.luku_jono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_maara - 1):
                tuotos = tuotos + str(self.luku_jono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.luku_jono[self.alkioiden_maara - 1])
            tuotos = tuotos + "}"
            return tuotos
