class Logger:
    def __init__(self, name, format_string="{name} ({index}): {value}"):
        self.name = name
        self.index = 0
        self.format_string = format_string

    def __call__(self, value):
        print(self.format_string.format(name=self.name, index=self.index, value=value))
