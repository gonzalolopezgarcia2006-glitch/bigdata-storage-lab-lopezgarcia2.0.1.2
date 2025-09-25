"""
Aplicación Streamlit para el laboratorio de arquitectura de datos.

Permite:
- Subir múltiples CSV.
- Normalizar columnas a esquema canónico (date, partner, amount).
- Añadir metadatos de linaje.
- Validar datos básicos.
- Derivar capa Silver (partner × mes).
- Visualizar KPIs y gráficos.
- Descargar resultados como CSV.
"""

import io
import pandas as pd
import streamlit as st

from src.transform import normalize_columns, to_silver
from src.validate import basic_checks
from src.ingest import tag_lineage, concat_bronze


# -------------------
# Configuración básica
# -------------------
st.set_page_config(page_title="Data Lab", layout="wide")
st.title("🗂️ Laboratorio de Datos")


# -------------------
# Barra lateral
# -------------------
st.sidebar.header("Configuración de columnas origen")
col_date = st.sidebar.text_input("Columna de fecha (origen)", "date")
col_partner = st.sidebar.text_input("Columna de partner (origen)", "partner")
col_amount = st.sidebar.text_input("Columna de monto (origen)", "amount")

mapping = {
    col_date: "date",
    col_partner: "partner",
    col_amount: "amount",
}

uploaded_files = st.file_uploader(
    "Sube uno o más archivos CSV",
    type=["csv"],
    accept_multiple_files=True,
)


# -------------------
# Procesamiento
# -------------------
bronze_frames = []

if uploaded_files:
    for file in uploaded_files:
        try:
            df = pd.read_csv(file, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(file, encoding="latin-1")

        # Normalizar columnas y añadir linaje
        df_norm = normalize_columns(df, mapping)
        df_tagged = tag_lineage(df_norm, source_name=file.name)
        bronze_frames.append(df_tagged)

    # Concatenar resultados
    bronze = concat_bronze(bronze_frames)

    st.subheader("Bronze (unificado)")
    st.dataframe(bronze.head(50))

    # Validaciones
    errors = basic_checks(bronze)
    if errors:
        st.error("❌ Se encontraron problemas en los datos:")
        for e in errors:
            st.write(f"- {e}")
    else:
        st.success("✅ Validaciones básicas superadas")

        # Derivar Silver
        silver = to_silver(bronze)

        st.subheader("Silver (partner × mes)")
        st.dataframe(silver.head(50))

        # KPIs simples
        total_amount = silver["total_amount"].sum()
        n_partners = silver["partner"].nunique()
        n_months = silver["month"].nunique()

        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric("Monto total (EUR)", f"{total_amount:,.2f}")
        kpi2.metric("Partners únicos", str(n_partners))
        kpi3.metric("Meses cubiertos", str(n_months))

        # Gráfico
        st.bar_chart(silver.set_index("month")["total_amount"])

        # Descargas
        st.subheader("Descargar resultados")
        bronze_csv = bronze.to_csv(index=False).encode("utf-8")
        silver_csv = silver.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇️ Descargar Bronze CSV",
            data=bronze_csv,
            file_name="bronze.csv",
            mime="text/csv",
        )
        st.download_button(
            "⬇️ Descargar Silver CSV",
            data=silver_csv,
            file_name="silver.csv",
            mime="text/csv",
        )
