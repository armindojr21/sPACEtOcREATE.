import datetime
agora = datetime.datetime.now()
agora_sem_micsec = agora.strftime('%Y-%m-%d %H:%M:%S')
print(agora_sem_micsec)