import time

def buscar_duplicados_lento(lista):
    """Abordagem O(n²) usando .count() dentro de um loop."""
    duplicados = []
    for item in lista:
        if lista.count(item) > 1 and item not in duplicados:
            duplicados.append(item)
    return duplicados

def buscar_duplicados_rapido(lista):
    """Abordagem O(n) otimizada usando conjuntos (sets)."""
    vistos = set()
    duplicados = set()
    for item in lista:
        if item in vistos:
            duplicados.add(item)
        else:
            vistos.add(item)
    return list(duplicados)

def testar_eficiencia():
    # Gerando uma lista de teste com 15.000 números
    dados_teste = list(range(15000)) + [5, 99, 1050, 9999]
    
    print("Iniciando teste de eficiência algoritmo...\n")
    
    # Testando a função lenta
    inicio = time.time()
    buscar_duplicados_lento(dados_teste)
    fim = time.time()
    tempo_lento = fim - inicio
    print(f"Tempo da abordagem lenta O(n²): {tempo_lento:.5f} segundos")
    
    # Testando a função rápida
    inicio = time.time()
    buscar_duplicados_rapido(dados_teste)
    fim = time.time()
    tempo_rapido = fim - inicio
    print(f"Tempo da abordagem rápida O(n): {tempo_rapido:.5f} segundos")
    
    # Calculando a diferença
    if tempo_rapido > 0:
        melhoria = tempo_lento / tempo_rapido
        print(f"\nA abordagem otimizada foi {melhoria:.1f}x mais rápida!")

if __name__ == "__main__":
    testar_eficiencia()
