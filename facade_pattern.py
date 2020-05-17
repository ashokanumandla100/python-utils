"""
Facade Pattern: Hide subsystem complexity and provide smooth client interface
Ex: Car
"""

class SubSystemA:
    def ignition(self):
        print("Ignition...")

class SubSystemB:
    def lighting(self):
        print("Lighting...")

class Facade:
    def __init__(self):
        self._subSystemA = SubSystemA()
        self._subSystemB = SubSystemB()

    def exec_method(self):
        self._subSystemA.ignition()
        self._subSystemB.lighting()

def main():
    facade = Facade()
    facade.exec_method()

if __name__ == '__main__':
    main()