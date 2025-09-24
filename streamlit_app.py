import streamlit as st
import pandas as pd
import os

def main():
    st.set_page_config(
        page_title="Almacén Analítico Confiable",
        page_icon="📊",
        layout="wide"
    )
    
    st.title("📊 De CSVs heterogéneos a un almacén analítico confiable")
    st.markdown("---")
    
    # Sidebar
    st.sidebar.header("Navegación")
    section = st.sidebar.radio(
        "Selecciona una sección:",
        ["🏠 Dashboard", "📈 Calidad de Datos", "🔍 Data Lineage", "📋 Documentación"]
    )
    
    if section == "🏠 Dashboard":
        show_dashboard()
    elif section == "📈 Calidad de Datos":
        show_data_quality()
    elif section == "🔍 Data Lineage":
        show_data_lineage()
    elif section == "📋 Documentación":
        show_documentation()

def show_dashboard():
    st.header("Dashboard Principal")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Archivos Procesados", "0")
    
    with col2:
        st.metric("Tasa de Calidad", "0%")
    
    with col3:
        st.metric("KPIs Calculados", "0")
    
    st.info("🚧 Dashboard en construcción - Implementa las métricas reales aquí")

def show_data_quality():
    st.header("Calidad de Datos")
    st.warning("Implementa los reportes de calidad de datos aquí")

def show_data_lineage():
    st.header("Data Lineage")
    st.info("Aquí se mostrará el trazado de los datos a través del pipeline")

def show_documentation():
    st.header("Documentación del Proyecto")
    st.markdown("""
    ### Estructura del Proyecto
    - **data/raw**: Datos crudos originales
    - **data/bronze**: Datos validados mínimamente
    - **data/silver**: Datos limpios y estandarizados
    - **data/gold**: Datos enriquecidos para análisis
    """)

if __name__ == "__main__":
    main()
