# Plan de pruebas de la actividad

## Objetivo
Comprobar que el prototipo mínimo cumple su caso de uso principal.

## Tipos de prueba
1. **Prueba funcional básica**: verifica flujo principal.
2. **Prueba de validación**: revisa entradas inválidas.
3. **Prueba de regresión rápida**: confirma que cambios no rompen lo ya funcional.

## Matriz mínima
| ID | Escenario | Entrada | Resultado esperado |
|----|-----------|---------|--------------------|
| P1 | Ejecución normal | dato válido | salida correcta |
| P2 | Entrada vacía | "" | mensaje de validación |
| P3 | Valor fuera de rango | -1 o texto inválido | manejo de error |

## Evidencia solicitada
- Salida de terminal de al menos 2 pruebas.
- Nota corta: qué falló, qué corregiste y cómo lo verificaste.
