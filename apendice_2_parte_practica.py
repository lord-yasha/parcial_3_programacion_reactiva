# Se importa RxPY
from rx import from_iterable
from rx import operators as ops

# Lista a usar de ejemplo
numeros = [1, 2, 3, 4, 5]

# Se crea el flujo a partir de la lista
flujo = from_iterable(numeros)

# Filtro que solo deja pasar números > 3
flujo_filtrado = flujo.pipe(
    ops.filter(lambda x: x > 3)
)

# Suscripción para cada vez que un número > 3 se imprima
flujo_filtrado.subscribe(
    on_next=lambda n: print("Recibí el número:", n),
    on_completed=lambda: print("Ya no hay más números.")
)