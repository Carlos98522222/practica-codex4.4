# Ideas de pruebas básicas

## Pruebas manuales recomendadas
1. Ejecutar `bash scripts/run.sh` y capturar salida con nombre válido.
2. Ejecutar y enviar entrada vacía para validar mensaje de error.
3. Ejecutar con espacios alrededor del nombre para confirmar limpieza de entrada.

## Casos ejemplo
- Entrada: `Ana` -> Salida esperada: saludo con confirmación de funcionamiento.
- Entrada: `` (vacía) -> Salida esperada: mensaje de validación.
- Entrada: `  Luis  ` -> Salida esperada: saludo sin espacios extra.

## Mejora opcional
Crear pruebas automatizadas con `pytest` para la función `construir_mensaje`.
