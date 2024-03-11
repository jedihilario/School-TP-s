from models.persona import Persona

file_name = 'db.txt'

class Query:
    def select_all () -> list:
        data: list = []
        with open(file_name, 'r') as db:
            for i in db:
                data.append(i.split(','))
        return data
    
    def save_data(data: list[Persona]) -> None:
        new = ''

        for i in data:
            new += f'{i.name},{i.surname},{i.dni},{i.age}\n'

        with open(file_name, 'w') as db:
            db.write(new)