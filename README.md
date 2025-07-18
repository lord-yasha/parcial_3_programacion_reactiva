# Parcial #3 – Programación Reactiva

## Universidad Nacional de Colombia
### Grupo 15 – Ingeniería Mecatrónica
**Estudiante:** José Yecid Jiménez Buitrago  
**Correo:** jyjimenezb@unal.edu.co  
**Curso:** Programación de Computadores  
**Parcial:** #3  
**Paradigma:** Programación Reactiva

---

## Descripción:

Este es el repositorio con el ejemplo práctico del parcial #3 sobre el paradigma de **programación reactiva**.  
El código está hecho en Python y usa la librería `RxPY`.

---

## Requisitos:

- Python 3.x  
- RxPY (se puede instalar con pip):

## Ejecutar en terminal:

pip install rx


---

## ¿Qué hace el programa?:

1. Toma una lista de números: `[1, 2, 3, 4, 5]`
2. Filtra solo los mayores a 3.
3. Imprime cada número filtrado cuando lo recibe.
4. Al final, dice que el flujo terminó.

---

## ¿Por qué es programación reactiva?:

Porque en vez de procesar los datos directamente, se crea un flujo de eventos y se define cómo reaccionar cuando lleguen.  
El programa reacciona a cada número recibido del flujo, y lo procesa en tiempo real (aunque en este ejemplo el flujo es corto y fijo).

---

## Ejecución:

```bash
$ python apendice_2_parte_practica.py
Recibí el número: 4  
Recibí el número: 5  
Ya no hay más números.
