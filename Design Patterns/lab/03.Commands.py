import sys


class Window:
    def exit(self):
        sys.exit()


class Document:
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"

    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.contents)


class ToolbarDocument:
    def __init__(self, name, iconname):
        self.name = name
        self.iconname = iconname

    def click(self):
        self.iconname.execute()


class MenuItem:
    def __init__(self, menu_main, item_name):
        self.menu_main = menu_main
        self.item_name = item_name

    def click(self):
        self.item_name.execute()


class KeyboardShortcut:
    def __init__(self, key, modifier):
        self.key = key
        self.modifier = modifier

    def click(self):
        self.modifier.execute()


class SaveCommand:
    def __init__(self, document):
        self.document = document

    def execute(self):
        self.document.save()


class ExitCommand:
    def __init__(self, window):
        self.window = window

    def execute(self):
        self.window.save()
