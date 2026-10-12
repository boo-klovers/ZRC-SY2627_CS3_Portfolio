class PSHSGalaxy:
    def __init__(self, language):
        self._language = language

class Nationality(PSHSGalaxy):
    def __init__(self, language, size, population):
        super().__init__(language)
        self._size = size
        self._population = population

class Aliens(PSHSGalaxy):
    def __init__(self, language, technologyProficiency, isFriendly: bool):
        super().__init__(language)
        self._technologyProficiency = technologyProficiency
        self._isFriendly = isFriendly

class Spaniards(Nationality):
    def __init__(self, language, size, population, dni):
        super().__init__(language, size, population)
        self._dni = dni

    @property
    def dni(self):
        return f'ID Number: {self._dni}'

    @property
    def population(self):
        return f'Population Number: {self._population}'

    @property
    def size(self):
        return f'Size: {self._size}'

    @property
    def language(self):
        return f'Language: {self._language}'

class Filipino(Nationality):
    def __init__(self, language, size, population, philsysID):
        super().__init__(language, size, population)
        self._philsysID = philsysID

    @property
    def philsysID(self):
        return f'ID Number: {self._philsysID}'

    @property
    def population(self):
        return f'Population Number: {self._population}'

    @property
    def size(self):
        return f'Size: {self._size}'

    @property
    def language(self):
        return f'Language: {self._language}'

class Indonesians(Nationality):
    def __init__(self, language, size, population, nik):
        super().__init__(language, size, population)
        self._nik = nik

    @property
    def nik(self):
        return f'ID Number: {self._nik}'

    @property
    def population(self):
        return f'Population Number: {self._population}'

    @property
    def size(self):
        return f'Size: {self._size}'

    @property
    def language(self):
        return f'Language: {self._language}'

class Marvels(Aliens):
    def __init__(self, language, technologyProficiency, isFriendly: bool, designation):
        super().__init__(language, technologyProficiency, isFriendly)
        self._designation = designation

class Avengers(Marvels):
    def __init__(self, language, technologyProficiency, isFriendly: bool, designation, alias):
        super().__init__(language, technologyProficiency, isFriendly, designation)
        self._alias = alias

    @property
    def alias(self):
        return f'Alias: {self._alias}'

    @property
    def designation(self):
        return f'Designation: {self._designation}'

    @property
    def isFriendly(self):
        if self._isfriendly is True:
            return f'They wont attack you twin'
        else:
            return f'brotha run'

    @property
    def technologyProficiency(self):
        return f'Proficiency: {self._technologyProficiency}'

    @property
    def language(self):
        return f'Language: {self._language}'

pinoy = Filipino("Filipino", 300000, 113000000, 748392650173)
indo = Indonesians("Indonesian",  1900000,288000000, 3171015511930002)
espanol = Spaniards("Spanish", 506000, 49000000, 45678901)

print(pinoy.size)
print(indo.population)
print(espanol.dni)