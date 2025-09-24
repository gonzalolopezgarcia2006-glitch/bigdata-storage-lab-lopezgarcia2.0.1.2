"""
Módulo de ingesta de datos CSV heterogéneos
"""
import pandas as pd
import os
from pathlib import Path
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataIngestor:
    def __init__(self, raw_data_path: str = "data/raw"):
        self.raw_data_path = Path(raw_data_path)
        self.supported_encodings = ['utf-8', 'latin-1', 'iso-8859-1']
    
    def detect_csv_format(self, file_path: Path) -> dict:
        """
        Detecta automáticamente el formato del CSV
        """
        try:
            # Implementar detección de delimitador, encoding, etc.
            return {"delimiter": ",", "encoding": "utf-8"}
        except Exception as e:
            logger.error(f"Error detectando formato: {e}")
            return {}
    
    def read_heterogeneous_csv(self, file_path: Path) -> pd.DataFrame:
        """
        Lee un CSV con detección automática de formato
        """
        try:
            format_info = self.detect_csv_format(file_path)
            df = pd.read_csv(file_path, **format_info)
            logger.info(f"Archivo {file_path.name} leído exitosamente")
            return df
        except Exception as e:
            logger.error(f"Error leyendo {file_path}: {e}")
            return pd.DataFrame()
    
    def ingest_all_files(self) -> dict:
        """
        Ingresa todos los archivos CSV del directorio raw
        """
        if not self.raw_data_path.exists():
            logger.error(f"Directorio {self.raw_data_path} no existe")
            return {}
        
        csv_files = list(self.raw_data_path.glob("*.csv"))
        ingested_data = {}
        
        for csv_file in csv_files:
            df = self.read_heterogeneous_csv(csv_file)
            if not df.empty:
                ingested_data[csv_file.stem] = df
        
        return ingested_data

def main():
    """Función principal del módulo de ingesta"""
    ingestor = DataIngestor()
    data = ingestor.ingest_all_files()
    print(f"Archivos ingeridos: {list(data.keys())}")

if __name__ == "__main__":
    main()
