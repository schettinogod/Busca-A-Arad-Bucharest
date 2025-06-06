# -*- coding: utf-8 -*-
"""Busca_A*.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F5vJpw2AD8xyUV_QB-KCDex5sLIxXYsS
"""

#
#Vincenzo - Inteligência Computacional - 2023
#IFF - Itaperuna - RJ
#Busca A* em Python para resolver o problema Arad Bucharest
import queue

inicio = 'Arad'
final = 'Rimnicu'
result = ''

dict_hn = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}
#HEURÍSTICA
#DISTANCIA EM LINHA RETA

dict_gn = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Bucharest': {'Urziceni': 85, 'Giurgiu': 90, 'Pitesti': 101, 'Fagaras': 211},
    'Craiova': {'Drobeta': 120, 'Pitesti': 138, 'Rimnicu': 146},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Giurgiu': {'Bucharest': 90},
    'Hirsova': {'Eforie': 86, 'Urziceni': 98},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu': 97, 'Bucharest': 101, 'Craiova': 138},
    'Rimnicu': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Sibiu': {'Rimnicu': 80, 'Fagaras': 99, 'Arad': 140, 'Oradea': 151},
    'Timisoara': {'Lugoj': 111, 'Arad': 118},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Zerind': {'Oradea': 71, 'Arad': 75}
}
#custos reais para se deslocar de uma cidade para outra.

def get_fn(cidadestring):
#Essa função vai calcular o custo total estimado (f(n)) para cada caminho representado por :cidadestring, que é a string de todas as cidades visitadas.
#
#Ou seja somando hn + gn

    cities = cidadestring.split(" , ")
    #O método split() é aplicado em uma string e retorna uma lista de substrings.
    #Por exemplo, se cidadestring for "Arad , Sibiu , Bucharest",
    #a linha cities = cidadestring.split(" , ") resultará em cities sendo uma lista ["Arad", "Sibiu", "Bucharest"],
    #onde cada elemento representa uma cidade percorrida no caminho.

    hn = gn = 0
    #Iniciam com zero.
    #'gn = 0' = não há custo acumulado
    #'hn = 0' = não há valor de heurística


    for ctr in range(0, len(cities)-1):
    #o for percorre os índices de todas as cidades na sequência, exceto a última cidade.
    #começa de 0 e vao até o (tamahno da lista - 1)
        gn = gn + dict_gn[cities[ctr]][cities[ctr+1]]
        # a cada iteração do for, o valor de gn = custo acumulado anterior + a distancia entre a cidade atual e a mais próxima em relação ao custo real da distancia entre elas


        #'cities' = lista de cidades. 'ctr' = indice usado para percorrer esta lista. 'cities[ctr]' retorna a cidade na posição ctr da lista.
        #'cities[ctr+1]' retorna a cidade seguinte a cidade atual da lista.



    hn = dict_hn[cities[-1]]
    return hn + gn

def expand(cityq):
    global result
    #declara que a variavel result é global, podendo ser modificada dentro da função.

    while not cityq.empty():
    #cria um loop enqunato a fila "cityq" não estiver vazia, ou seja até todos os nós serem explorados.

        custo_total, cidadestring, cidade_atual = cityq.get()
        #o método "get()" é chamado na fila "cityq" esse método remove e retorna o próximo elemento da fila.
        #porém o elemento que está sendo obtido é uma tupla contendo 3 valores que são atribuídos às variáveis.

        #custo_total = Representa o custo acumulado até o momento para alcançar a cidade atual.
        #cidadestring = É uma string que representa o caminho percorrido até a cidade atual.Concatenação das cidades visitadas separadas por vírgulas.
        #cidade_atual = É a cidade atual que está sendo explorada.

        if cidade_atual == final:
        #verifica se a cidade atual = cidade final.

            result = cidadestring + " : : " + str(custo_total)
            return
        for cty in dict_gn[cidade_atual]:
            cityq.put((get_fn(cidadestring + " , " + cty), cidadestring + " , " + cty, cty))

def main():
    cityq = queue.PriorityQueue()
    cityq.put((get_fn(inicio), inicio, inicio))
    expand(cityq)
    print("O caminho total a partir da origem até o destino por A* é:")
    print(result)

main()
