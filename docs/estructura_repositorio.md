# Estructura recomendada del repositorio

Esta actividad usa una organización simple y mantenible:

```text
nombre-del-proyecto/
├── README.md
├── docs/
│   ├── propuesta.md
│   ├── caso_de_uso.md
│   ├── estructura_repositorio.md
│   └── plan_de_pruebas.md
├── src/
│   └── main.py
├── scripts/
│   └── run.sh
└── tests/
    └── test_plan.md
```

## Reglas mínimas
- `docs/`: contiene diseño, decisiones y planeación.
- `src/`: contiene el código ejecutable.
- `scripts/`: automatiza ejecución básica.
- `tests/`: describe y/o implementa pruebas.

## Convenciones sugeridas
- Nombres de archivo en minúsculas y con guion bajo.
- Funciones cortas con una sola responsabilidad.
- Mensajes de error claros para usuario no técnico.
