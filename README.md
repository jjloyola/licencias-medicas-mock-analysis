# Simulación de Análisis de Licencias Médicas para SUSESO Chile

Análisis de datos de Licencias Médicas usando Python, SQLModel y PostreSQL

## 📋 Descripción

Este proyecto busca simular una fiscalización y análisis del sistema electrónico de licencias médicas. Se proponen algunas análisis de información relacionada con beneficios sociales del Estado y el comportamiento operativo y financiero de las Cajas de Compensación de Asignación Familiar (CCAF).

## 🗂️ Estructura del Proyecto

```
licencias-medicas-mock-analysis/
├── 📁 app/ # Aplicación principal
│ ├── 📁 database/ # Configuración de base de datos
│ └── 📁 models/ # Modelos de datos
├── 📁 data/ # Datos de ejemplo
├── 📁 notebooks/ # Jupyter notebooks para análisis
├── 📁 queries/ # Consultas SQL
├── 📁 scripts/ # Scripts de carga de datos
└── 📄 requirements.txt # Dependencias de Python
```

## 📦 Datos Incluidos

Se generó una base de datos con datos simulados con las siguientes características.

- **beneficiarios.csv:** 2 000 personas afiliadas a una CCAF, con fecha de nacimiento y sexo.
- **licencias_medicas.csv:** ~2 500 licencias (0‑3 por persona). Incluye días, causa, región, RUT del emisor, monto del subsidio y estado/pago.
- **beneficio_logs.csv:** ~10 000 registros históricos de beneficios (incluye licencias, asignación familiar, subsidios, etc.).

**Los datos son completamente ficticios**

## ⚙️ Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/licencias-medicas-mock-analysis.git
cd licencias-medicas-mock-analysis
```

2. Crear entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:

```bash
cp config.env.example config.env
# Editar config.env con tus credenciales de base de datos
```

## Análisis

En el archivo notebooks/analisis_licencias.ipynb se pueden ver algunos métodos usados para realizar los análisis y estadísticas de los datos usando SQLModel. Algunos resultados se acompañaron con gráficos y tablas, usando pandas y matplotlib, para sacar mayor provecho al análisis.

## Trabajo futuro

En el futuro sería ideal expandir los datos generados para incluir una tabla de salidas al extranjero de los beneficiarios, para hacer un cruzamiento con la información de licencias médicas.
