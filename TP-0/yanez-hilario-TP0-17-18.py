class BankAccount:
    def __init__(self, owner: str = 'Dardo', start_money: int = 0) -> None:
        # Atributos teoricamente privados
        self.owner = owner
        self.money = start_money

    # Getters
    def get_owner (self) -> str: return self.owner

    def get_money (self) -> int: return self.money

    # Setters
    def set_owner (self, new_owner: str) -> None:
        self.owner = new_owner if (type(new_owner) == str) else self.owner

    def set_money (self, new_money: int) -> None:
        if (type(new_money) != int): return

        self.money = new_money

    # Retirar y depositar
        
    def retirar (self, amount: int = 0) -> str:
        new_money = self.money - amount

        if (new_money < 0): return 'Fondos insuficientes'

        self.money = new_money
        return f'Retiro de ${amount} ejecutado con exito'
    
    def depositar (self, amount: int = 0) -> str:
        self.money += amount
        return 'Despito realizado con exito'

def main ():
    account = BankAccount('Hilario', 1000)
    print(f'Dinero actual: {account.get_money()}')
    print(f'Deposito de $10:\n{account.depositar(100)}')
    print(f'Dinero actual: {account.get_money()}')
    print(f'Retiro de $600:\n{account.retirar(600)}')
    print(f'Dinero actual: {account.get_money()}')
    print(f'Retiro de $600:\n{account.retirar(600)}')
    print(f'Dinero actual: {account.get_money()}')
    print(f'Cambiando de duenio a Dardo...')
    account.set_owner('Dardo')
    print(f'Duenio actual: {account.get_owner()}')
    print(f'Restableciendo dinero a $1000...')
    account.set_money(1000)
    print(f'Dinero actual: {account.get_money()}')

if (__name__ == '__main__'):
    main()