cinema = [[0] * 8 for _ in range(5)]

def reservar_assento(fileira, assento):
    cinema[fileira - 1][assento - 1] = 1

def cancelar_reserva(fileira, assento):
    cinema[fileira 1][assento 1] = 0

def exibir_mapa():
    for fileira in cinema:
        print(fileira)

reservar_assento(0, 2)
reservar_assento(1, 4)
reservar_assento(3, 6)

cancelar_reserva(1, 4)

exibir_mapa()
