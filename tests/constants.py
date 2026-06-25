URL_BASE = 'https://marceloterencianiifpr.github.io/calculo-combustivel/'

TEST_CASES = [
    {"distancia": -1, "litros": 1, "consumo": "Inválido!", "classificacao": "Não foi possível calcular o consumo para os valores informados!"},
    {"distancia": 0, "litros": 1, "consumo": "Inválido!", "classificacao": "Não foi possível calcular o consumo para os valores informados!"},
    {"distancia": 1, "litros": 1, "consumo": "1.00 km/L", "classificacao": "Alto consumo"},
    {"distancia": 7, "litros": 1, "consumo": "7.00 km/L", "classificacao": "Alto consumo"},
    {"distancia": 8, "litros": 1, "consumo": "8.00 km/L", "classificacao": "Consumo normal"},
    {"distancia": 9, "litros": 1, "consumo": "9.00 km/L", "classificacao": "Consumo normal"},
    {"distancia": 11, "litros": 1, "consumo": "11.00 km/L", "classificacao": "Consumo normal"},
    {"distancia": 12, "litros": 1, "consumo": "12.00 km/L", "classificacao": "Consumo normal"},
    {"distancia": 13, "litros": 1, "consumo": "13.00 km/L", "classificacao": "Econômico"},
]