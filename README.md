## S-CAD

Aplicación multipágina creada con Streamlit para presentar asignaciones y parciales con material visual (imágenes, videos y visores embebidos de Shapr3D/Autodesk).

### Requisitos

- Python 3.10 o 3.11 (recomendado)
- pip

### Instalación

1. Crear y activar un entorno virtual (opcional pero recomendado)
   - Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
2. Instalar dependencias
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución local

```bash
streamlit run app.py
```

La app abrirá en `http://localhost:8501`.

### Estructura del proyecto

```
S-CAD/
├─ app.py              # Entrypoint de Streamlit (navegación principal)
├─ pages/              # Páginas de Asignaciones/Parciales
├─ img/                # Recursos estáticos (imágenes y videos)
├─ mejoras.md          # Notas y mejoras sugeridas
├─ requirements.txt    # Dependencias
└─ README.md           # Este archivo
```

### Despliegue (Streamlit Community Cloud)

1. Sube el repositorio a GitHub.
2. En Streamlit Community Cloud, crea una nueva app seleccionando tu repo y `app.py` como archivo principal.
3. Asegúrate de incluir `requirements.txt` (ya provisto) y la carpeta `img/` con todos los assets necesarios.

Notas:
- Los visores embebidos (iframes) requieren conexión a internet para cargar contenido externo.
- Si alguna URL externa falla, abre el enlace alternativo provisto en cada página.