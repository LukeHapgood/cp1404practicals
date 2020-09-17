class ProgrammingLanguage:

    def __init__(self, name='', typing='', reflection='', year=0):
        """Initialise a Programming Language.

        name: string
        typing: string
        reflection: string
        year: integer
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year


    def is_dynamic(self):
        if self.typing == 'Dynamic':
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing,
                                                                           self.reflection, self.year)
