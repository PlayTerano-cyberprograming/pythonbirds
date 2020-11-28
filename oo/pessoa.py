class Pessoa:
    def comprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(p.comprimentar())
    print(id(p))