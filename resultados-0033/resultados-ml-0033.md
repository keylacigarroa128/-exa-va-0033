# Reporte de Análisis de Datos - Pandas

`Keyla Paola Machine Learning pandas, NC 0033`

## 1. DataFrame Convertido
```text
     Habitacion  Capacidad  Precio_noche
0      Sencilla          2           800
1         Doble          3          1200
2         Suite          4          3500
3      Familiar          6          2000
4  Presidencial          2          8000
5        Junior          3          1800
```

## 2.1 Primeras Filas (head)
```text
  Habitacion  Capacidad  Precio_noche
0   Sencilla          2           800
1      Doble          3          1200
```

## 2.2 Últimas Filas (tail)
```text
     Habitacion  Capacidad  Precio_noche
4  Presidencial          2          8000
5        Junior          3          1800
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Habitacion        str
Capacidad       int64
Precio_noche    int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   Habitacion    6 non-null      str  
 1   Capacidad     6 non-null      int64
 2   Precio_noche  6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Precio_noche'
```text
count       6.000000
mean     2883.333333
std      2671.641193
min       800.000000
25%      1350.000000
50%      1900.000000
75%      3125.000000
max      8000.000000
Name: Precio_noche, dtype: float64
```

## 4. Ordenar Ascendente por Precio_noche
```text
     Habitacion  Capacidad  Precio_noche
0      Sencilla          2           800
1         Doble          3          1200
5        Junior          3          1800
3      Familiar          6          2000
2         Suite          4          3500
4  Presidencial          2          8000
```

## 5. Ordenar Descendente por Capacidad
```text
     Habitacion  Capacidad  Precio_noche
3      Familiar          6          2000
2         Suite          4          3500
5        Junior          3          1800
1         Doble          3          1200
0      Sencilla          2           800
4  Presidencial          2          8000
```

`Keyla Paola Machine Learning pandas, NC 0033`