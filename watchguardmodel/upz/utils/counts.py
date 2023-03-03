import pandas as pd

from typing import Union

def get_counts(df: pd.DataFrame, severity_data: pd.DataFrame) -> dict:
    query_data = {
        'morning_bicy_m': query(df, 'mañana', 'hurto de bicicletas', ['masculino', '-']),
        'morning_bicy_f': query(df, 'mañana', 'hurto de bicicletas', ['femenino', '-']),
        'aftern_bicy_m': query(df, 'tarde', 'hurto de bicicletas', ['masculino', '-']),
        'aftern_bicy_f': query(df, 'tarde', 'hurto de bicicletas', ['femenino', '-']),
        'night_bicy_m': query(df, 'noche', 'hurto de bicicletas', ['masculino', '-']),
        'night_bicy_f': query(df, 'noche', 'hurto de bicicletas', ['femenino', '-']),
        'morning_walk_m': query(df, 'mañana', ['hurto a personas', 'hurto de celulares'], ['masculino', '-']),
        'morning_walk_f': query(df, 'mañana', ['hurto a personas', 'hurto de celulares'], ['femenino', '-']),
        'aftern_walk_m': query(df, 'tarde', ['hurto a personas', 'hurto de celulares'], ['masculino', '-']),
        'aftern_walk_f': query(df, 'tarde', ['hurto a personas', 'hurto de celulares'], ['femenino', '-']),
        'night_walk_m': query(df, 'noche', ['hurto a personas', 'hurto de celulares'], ['femenino', '-']),
        'night_walk_f': query(df, 'noche', ['hurto a personas', 'hurto de celulares'], ['femenino', '-']),
        'morning_car_m': query(df, 'mañana', 'hurto automotores', ['masculino', '-']),
        'morning_car_f': query(df, 'mañana', 'hurto automotores', ['femenino', '-']),
        'aftern_car_m': query(df, 'tarde', 'hurto automotores', ['masculino', '-']),
        'aftern_car_f': query(df, 'tarde', 'hurto automotores', ['femenino', '-']),
        'night_car_m': query(df, 'noche', 'hurto automotores', ['masculino', '-']),
        'night_car_f': query(df, 'noche', 'hurto automotores', ['femenino', '-']),
        'type_1_events': type_query(df, severity_data, 1),
        'type_2_events': type_query(df, severity_data, 2),
        'type_3_events': type_query(df, severity_data, 3),
        'total_events': df['numero_hechos'].sum()
    }
    return query_data

def type_query(df: pd.DataFrame, severity_df: pd.DataFrame, severity: int) -> int:
    return (
        pd.merge(left=df, right=severity_df, left_on='modalidad', right_on='modality')
        .query('severity == @severity')
        ['numero_hechos'].sum()
    )

def query(df: pd.DataFrame, range: str, crime: Union[str, list], sex: list) -> int:
    if isinstance(crime, str):
        return (
            df
            .query("rango_del_dia == @range & delito == @crime & sexo in @sex")
            ['numero_hechos'].sum()
        )
    elif isinstance(crime, list):
        return (
            df
            .query("rango_del_dia == @range & delito in @crime & sexo in @sex")
            ['numero_hechos'].sum()
        )
    else:
        raise TypeError('crime must be a str or list')
