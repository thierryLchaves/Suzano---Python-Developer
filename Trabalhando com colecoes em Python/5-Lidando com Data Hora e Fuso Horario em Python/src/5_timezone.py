from datetime import datetime, timedelta, timezone


data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))
data_padrao = datetime.now(timezone.utc)

print(data_oslo)
print(data_sao_paulo)
print(data_padrao)