from guloso import Grafo, Vertice
import matplotlib.pyplot as plt
import time
import dados

# listas para plotar grafico
tempos = list()
arestas = list()


inicio = time.time()

# iniciando grafo com dataset nova_luz2 (limitado a poucos quarteiroes)
g = Grafo()
dataset = dados.nova_luz2["arestas"]
for i in range(9):
    g.adiciona_vertice(Vertice(str(i+1)))
for i in dataset:
    g.adiciona_aresta(i[0], i[1], i[2], i[3])
g.encontra_caminho('1')

print(f'Caminho percorrido: {g.caminho}')
print(f'Custo total: {g.custo}')
print(f'Numero arestas total: {g.numero_arestas_total}')

# adicionando as metricas na lista
arestas.append(g.numero_arestas_total)
tempos.append(time.time() - inicio)

# # iniciando grafo com dataset nova_luz completo
g1 = Grafo()
dataset2 = dados.nova_luz["arestas"]
for i2 in range(38):
    g1.adiciona_vertice(Vertice(str(i2+1)))
for i2 in dataset2:
    g1.adiciona_aresta(i2[0], i2[1], i2[2], i2[3])
g1.encontra_caminho('1')

print(f'Caminho percorrido: {g1.caminho}')
print(f'Custo total: {g1.custo}')
print(f'Numero arestas total: {g1.numero_arestas_total}')

# adicionando as metricas na lista
arestas.append(g1.numero_arestas_total)
tempos.append(time.time() - inicio)

# gerando grafico
plt.xlabel('Número de Arestas')
plt.ylabel('Tempo')
plt.plot(arestas, tempos, label='Tempo em x número de Arestas - Algoritmo Guloso')
plt.grid()
plt.legend()
plt.show()