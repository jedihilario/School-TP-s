class Book:
    def __init__(self, name: str, author: str, release_date) -> None:
        self.name = name
        self.author = author
        self.release_date = release_date
        self.current_page = 1

    def read_page (self) -> None:
        print(f'El texto de la pagina {self.current_page} dice:\n...\n...\n...')
        self.pass_page()

    def pass_page(self):
        print('Pasando pagina...')
        self.current_page += 1

def main ():
    libro = Book('Las increibles aventuras de tito calderon', 'Benavides, Geronimo', 1945)
    for i in range(3):
        libro.read_page()

if (__name__ == '__main__'):
    main()