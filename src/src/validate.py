"""
Módulo de validación de calidad de datos
"""
import pandas as pd
from typing import List


def basic_checks(df: pd.DataFrame) -> List[str]:
    """
    Aplica validaciones básicas sobre un DataFrame en esquema canónico.
    Devuelve lista de errores encontrados.
    """
    errors: List[str] = []
    required_cols = {"date", "partner", "amount"}

    # Verificar columnas
    missing = required_cols - set(df.columns)
    if missing:
        errors.append(f"Faltan columnas requeridas: {missing}")

    # Verificar tipos
    if "amount" in df.columns:
        if not pd.api.types.is_numeric_dtype(df["amount"]):
            errors.append("Columna 'amount' no es numérica")
        if (df["amount"] < 0).any():
            errors.append("Valores negativos en 'amount'")

    if "date" in df.columns:
        if not pd.api.types.is_datetime64_any_dtype(df["date"]):
            errors.append("Columna 'date' no está en formato datetime")

    return errors
