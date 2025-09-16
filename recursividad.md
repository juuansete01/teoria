# Cálculo de Factorial en Kotlin

Un **factorial** es una operación matemática que se denota como `n!` y representa el producto de todos los números enteros positivos desde 1 hasta `n`.

Por ejemplo:
5! = 5 × 4 × 3 × 2 × 1 = 120

## Implementaciones en Kotlin

A continuación se muestran dos formas comunes de calcular el factorial en Kotlin: recursiva e iterativa.

---

### 1. Función Recursiva

```kotlin
fun factorial(n: Int): Long {
    return if (n <= 1) 1L else n * factorial(n - 1)
}
fun main() {
    val numero = 5
    val resultado = factorial(numero)
    println("El factorial de $numero es $resultado")
}
