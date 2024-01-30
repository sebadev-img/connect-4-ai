# Connect 4 AI

Para ejecutar el bot:

```
python client.py [id_token] [ai_name]
```

El nombre de la AI puede ser:

- simple
- simple-v2
- alphabeta

## El BOT

El bot se programo en python y esta compuesto por los siguientes archivos:

- client.py: implementa websocket para la conexion con el servidor.
- connect4.py: implementa funcionalidades para simular/crear el tablero y las acciones(colocar ficha, eliminar fila o columna), como asi tambien funciones que permiten obtener informacion del tablero.
- simulation_system.py: implementa funcionalidades para simular todas las jugadas posibles (colocar ficha, eliminar fila o columna).
- score_system: sistema de puntajes que evalua un tablero y le asigna una puntuacion.
- simple_ai.py: es el bot que ultilza los sistemas de simulacion de jugadas y puntuacion para elejir el mejor movimiento.
- simple_ai_v2.py : otro bot que funciona similar al anterior pero con un sistema de puntajes mejorado. Este es el bot que se utilizo para el torneo final.
- minimax_ai.py: el bot implementa el algoritmo minimax, es el bot que se utilizo para el torneo de la primera semana.
- /Test: la carpeta con los unit test.

## Estrategia de juego

La estragia que se implemento fue la de simular para cada turno todos los movimientos posibles, colocar ficha, eliminar fila o eliminar columna, y para cada movimiento posible generar el tablero resultante. Luego a cada tablero resultante se le asigna un puntaje con valor positivo para los tableros que mas cerca esten de dar la victoria al bot y valor negativo para los tableros que mas cerca esten de darle la victoria al oponente. De todos los tableros generados se elije el movimiento que genere un tablero con mayor puntaje postivo.
El bot que se llama "simple_ai" y "simple_ai_v2" implementan esta estrategia de juego.

En la primer semana se implemento el algoritmo minimax ("minimax_ai") pero con las reglas de la segunda semana el algoritmo debia simular mas posibles jugadas con lo que habia que pensar metodos para optimizar el algoritmo. Por este motivo se decidio ir con la implementacion del primer bot pero se mejoro el sistema de puntaje para que eligiera la mejor jugada para ganar pero que al mismo tiempo genere la mayor cantidad de puntos.
