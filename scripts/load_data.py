#!/usr/bin/env python3
"""
Script para cargar datos CSV a la base de datos PostgreSQL
"""

import sys
import os
import pandas as pd
from datetime import datetime
from sqlmodel import Session, select

# Agregar el directorio raíz al path para importar los módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database.connection import engine, create_db_and_tables
from app.models.all_models import Beneficiario, LicenciaMedica, BeneficioLog

def load_beneficiarios():
    """Cargar datos de beneficiarios desde CSV"""
    print("Cargando beneficiarios...")
    
    # Leer el archivo CSV
    df = pd.read_csv('data/beneficiarios.csv')
    
    # Convertir fecha_nacimiento a datetime
    df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento']).dt.date
    
    with Session(engine) as session:
        # Verificar si ya existen datos
        existing = session.exec(select(Beneficiario)).first()
        if existing:
            print("Los beneficiarios ya están cargados. Saltando...")
            return
        
        # Crea un array y lo llena con todos los elementos del dataframe que viene desde el csv
        beneficiarios = []
        for _, row in df.iterrows():
            beneficiario = Beneficiario(
                beneficiario_id=int(row['beneficiario_id']),
                ccaf=str(row['ccaf']),
                fecha_nacimiento=pd.to_datetime(row['fecha_nacimiento']).item().date(),
                sexo=str(row['sexo'])
            )
            beneficiarios.append(beneficiario)
        
        # Insertar en la base de datos
        session.add_all(beneficiarios)
        session.commit()
        print(f"✅ {len(beneficiarios)} beneficiarios cargados exitosamente")

def load_licencias_medicas():
    """Cargar datos de licencias médicas desde CSV"""
    print("Cargando licencias médicas...")
    
    # Leer el archivo CSV
    df = pd.read_csv('data/licencias_medicas.csv')
    
    # Convertir fechas a datetime
    df['fecha_emision'] = pd.to_datetime(df['fecha_emision']).dt.date
    df['fecha_pago'] = pd.to_datetime(df['fecha_pago'], errors='coerce').dt.date
    
    with Session(engine) as session:
        # Verificar si ya existen datos
        existing = session.exec(select(LicenciaMedica)).first()
        if existing:
            print("Las licencias médicas ya están cargadas. Saltando...")
            return
        
        # Crear objetos LicenciaMedica
        licencias = []
        for _, row in df.iterrows():
            licencia = LicenciaMedica(
                licencia_id=int(row['licencia_id']),
                beneficiario_id=int(row['beneficiario_id']),
                ccaf=str(row['ccaf']),
                fecha_emision=pd.to_datetime(row['fecha_emision']).item().date(),
                dias_licencia=int(row['dias_licencia']),
                causa=str(row['causa']),
                emisor_rut=str(row['emisor_rut']),
                region=str(row['region']),
                monto_subsidio_clp=int(row['monto_subsidio_clp']),
                estado_pago=str(row['estado_pago']),
                fecha_pago=pd.to_datetime(row['fecha_pago']).item().date() if pd.notna(row['fecha_pago']).item() else None
            )
            licencias.append(licencia)
        
        # Insertar en la base de datos
        session.add_all(licencias)
        session.commit()
        print(f"✅ {len(licencias)} licencias médicas cargadas exitosamente")

def load_beneficio_logs():
    """Cargar datos de logs de beneficios desde CSV"""
    print("Cargando logs de beneficios...")
    
    # Leer el archivo CSV
    df = pd.read_csv('data/beneficio_logs.csv')
    
    # Convertir fecha a datetime
    df['fecha'] = pd.to_datetime(df['fecha']).dt.date
    
    with Session(engine) as session:
        # Verificar si ya existen datos
        existing = session.exec(select(BeneficioLog)).first()
        if existing:
            print("Los logs de beneficios ya están cargados. Saltando...")
            return
        
        # Crear objetos BeneficioLog
        logs = []
        for _, row in df.iterrows():
            log = BeneficioLog(
                beneficiario_id=int(row['beneficiario_id']),
                fecha=pd.to_datetime(row['fecha']).item().date(),
                beneficio=str(row['beneficio']),
                monto=int(row['monto'])
            )
            logs.append(log)
        
        # Insertar en la base de datos
        session.add_all(logs)
        session.commit()
        print(f"✅ {len(logs)} logs de beneficios cargados exitosamente")

def main():
    """Función principal para cargar todos los datos"""
    print("🚀 Iniciando carga de datos a la base de datos...")
    
    # Crear tablas si no existen
    create_db_and_tables()
    print("✅ Tablas creadas/verificadas")
    
    # Cargar datos
    load_beneficiarios()
    load_licencias_medicas()
    load_beneficio_logs()
    
    print("🎉 ¡Carga de datos completada exitosamente!")

if __name__ == "__main__":
    main() 