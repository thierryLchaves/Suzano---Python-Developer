from datetime import date, datetime, timedelta

tipo_carro = input("Digite a o tipo de carro \n => ").upper()
TEMPO_PEQUENO = 30
TEMPO_MEDIO = 45
TEMPO_GRANDE = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=TEMPO_PEQUENO)
    print(f"O carro chegou: {data_atual} \n e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=TEMPO_MEDIO)
    print(f"O carro chegou: {data_atual} \n e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=TEMPO_GRANDE)
    print(f"O carro chegou: {data_atual} \n e ficará pronto às {data_estimada}")


print(date.today() - timedelta(minutes=1))

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())
