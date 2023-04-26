from time import sleep, perf_counter

def tarefa():
    print("Iniciando tarefa...")
    sleep(1)
    print("Finalizada!")

tempo_inicio = perf_counter()

tarefa()
tarefa()

tempo_final = perf_counter()

tempo_passado = tempo_final - tempo_inicio

print(f"Tempo passado: {tempo_passado: 0.2f}")