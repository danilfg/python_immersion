class PetExport:
    def export(self, dog):
        raise NotImplementedError

class ExportJSON(Pet):
    def export(self, dog):
        pass

class ExportXML(Pet):
    def export(self, dog):
        pass

class Pet:
    def __init__(self, name):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

class ExDog(Dog):
    def __init__(self, name, breed=None, exporter=None):
        super().__init__(name, breed=None)
        self._exporter = exporter

    def export(self):
        return self._exporter.export(self)