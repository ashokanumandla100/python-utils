# Command Pattern: Controlling the sequence of operations
from abc import abstractmethod,ABC

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Copy(Command):
    def execute(self):
        print('Copying...')

class Paste(Command):
    def execute(self):
        print('Pasting...')

class Print(Command):
    def execute(self):
        print('Printing...')

class Macro:
    def __init__(self):
        self._seq_commands = []

    def add(self, command):
        self._seq_commands.append(command)

    def run(self):
        for _ in self._seq_commands:
            _.execute()


def main():
    macro = Macro()

    macro.add(Copy())
    macro.add(Paste())
    macro.add(Print())

    macro.run()

if __name__ == '__main__':
    main()
