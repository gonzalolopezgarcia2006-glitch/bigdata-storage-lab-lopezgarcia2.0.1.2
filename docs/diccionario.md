# Diccionario de Datos

## Estructura del Proyecto

### Capas de Datos

#### Capa Bronze
- **Descripción**: Datos crudos con validación mínima
- **Metadatos agregados**: 
  - `_ingestion_timestamp`: Fecha y hora de ingesta
  - `_source`: Origen del archivo

#### Capa Silver  
- **Descripción**: Datos limpios y estandarizados
- **Transformaciones aplicadas**:
  - Estandarización de formatos
  - Limpieza de valores missing
  - Normalización de textos

#### Capa Gold
- **Descripción**: Datos enriquecidos para análisis
- **Características**:
  - KPIs calculados
  - Métricas de negocio
  - Datos listos para reporting

## Schemas por Fuente

### [Nombre del Dataset 1]
| Columna | Tipo | Descripción | Reglas de Validación |
|---------|------|-------------|---------------------|
| *ejemplo* | *string* | *descripción* | *reglas* |

### [Nombre del Dataset 2]
| Columna | Tipo | Descripción | Reglas de Validación |
|---------|------|-------------|---------------------|
| *ejemplo* | *string* | *descripción* | *reglas* |
