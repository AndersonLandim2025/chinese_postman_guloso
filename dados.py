#grafo 1, 2, 3, 4 ....

nova_luz = {
    "num_vertices": 38,
    "arestas": [
        ('1', '2', 50, True),
        ('2', '3', 215, False),
        ('3', '4', 100, False),
        ('3', '17', 85, False),
        ('4', '5', 80, True),
        ('4', '15', 100, True),
        ('4', '6', 105, True),
        ('5', '14', 85, True),
        ('6', '7', 120, True),
        ('6', '9', 100, False),
        ('7', '8', 20, True),
        ('8', '1', 155, True),
        ('8', '10', 30, True),
        ('9', '10', 50, True),
        ('10', '7', 10, True),
        ('9', '11', 70, True),
        ('11', '8', 50, True),
        ('9', '12', 80, True),
        ('12', '13', 90, True),
        ('13', '6', 60, True),
        ('13', '4', 95, True),
        ('14', '15', 90, True),
        ('15', '16', 90, True),
        ('16', '13', 100, True),
        ('16', '19', 90, True),
        ('17', '5', 45, True),
        ('17', '18', 140, True),
        ('18', '14', 85, True),
        ('19', '12', 100, True),
        ('19', '20', 90, True),
        ('20', '21', 120, True),
        ('21', '22', 140, True),
        ('22', '23', 60, True),
        ('23', '11', 40, True),
        ('22', '24', 50, True),
        ('23', '24', 50, True),
        ('24', '20', 100, True),
        ('20', '25', 85, True),
        ('25', '26', 90, True),
        ('26', '19', 80, True),
        ('26', '27', 90, True),
        ('27', '16', 90, True),
        ('27', '28', 90, True),
        ('15', '28', 100, True),
        ('28', '29', 130, True),
        ('29', '30', 110, False),
        ('30', '27', 130, True),
        ('30', '31', 85, False),
        ('31', '26', 135, True),
        ('31', '32', 90, False),
        ('25', '32', 135, True),
        ('32', '33', 120, False),
        ('33', '34', 135, True),
        ('34', '25', 120, True),
        ('34', '32', 80, True),
        ('28', '35', 80, True),
        ('14', '35', 100, True),
        ('35', '36', 125, True),
        ('36', '29', 90, True),
        ('35', '37', 85, True),
        ('37', '38', 125, True),
        ('38', '36', 75, False), # blz
    ]
}

nova_luz2 = {
    "num_vertices": 9,
    "arestas": [
        ('1', '2', 75, False),
        ('2', '3', 90, False),
        ('3', '4', 110, False),
        ('4', '5', 130, True),
        ('5', '6', 90, True),
        ('6', '7', 80, True),
        ('6', '3', 130, True),
        ('7', '8', 85, True),
        ('7', '2', 125, True),
        ('8', '1', 125, True),
    ]
}

nova_luz3 = {
    "num_vertices": 14,
    "arestas": [
        ('1', '2', 75, False),
        ('2', '3', 90, False),
        ('3', '4', 110, False),
        ('4', '5', 130, True),
        ('5', '6', 90, True),
        ('5', '12', 90, True),
        ('6', '7', 80, True),
        ('6', '3', 130, True),
        ('7', '8', 85, True),
        ('7', '2', 125, True),
        ('8', '1', 125, True),
        ('9', '8', 100, True),
        ('9', '10', 85, True),
        ('10', '11', 90, True),
        ('10', '7', 100, True),
        ('11', '6', 100, True),
        ('11', '12', 90, True),
        ('12', '13', 100, True),
        ('13', '14', 95, True),
        ('14', '11', 100, True),
    ]
}

data = {
    1: {
        "vertices": ['A', 'B', 'C', 'D', 'E'],
        "arestas": [
            ('A', 'D', 1, True), ('B', 'A', 5, True), ('B', 'C', 3, True), ('C', 'D', 8, True), ('D', 'B', 2, True),
            ('D', 'A', 3, True) , ('B', 'E', 2, True), ('E', 'C', 4, True)
        ],
        "descricao": "grafo 100% Direcionado"
    },
    2: {
        "vertices": ['A', 'B', 'C', 'D', 'E'],
        "arestas": [
            ('A', 'D', 1, False), ('B', 'A', 5, False), ('B', 'C', 3, False), ('C', 'D', 8, False), ('D', 'B', 2, False),
            ('D', 'A', 3, False), ('B', 'E', 2, False), ('E', 'C', 4, False)
        ],
        "descricao": "grafo 100% não Direcionado"
    },
    3: {
        "vertices": ['A', 'B', 'C', 'D'],
        "arestas": [
            ('A', 'B', 3, True), ('A', 'D', 4, False), ('B', 'A', 1, True), ('B', 'C', 2, False), ('D', 'C', 2, True)
        ],
        "descricao": "grafo misto simples"
    },
    4: {
        "vertices": ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        "arestas": [
            ('A', 'C', 7, True), ('B', 'A', 6, True), ('B', 'G', 5, False), ('C', 'B', 6, False), ('C', 'D', 5, False),('D', 'E', 5, True),
            ('E', 'B', 4, True), ('E', 'F', 5, False), ('F', 'G', 20, False)
        ],
        "descricao": "grafo misto mais complexo"
    },
    5: {
        "vertices": ['A', 'B', 'C', 'D'],
        "arestas": [
            ('A', 'B', 1, True), ('B', 'C', 5, True), ('C', 'D', 3, True), ('C', 'A', 3, True), ('D', 'A', 8, True)
        ],
        "descricao": "grafo 100% Direcionado"
    },
}

grafo_luan1 = {
    "num_vertices": 3,
    "arestas":  [('0', '1', 4, True), ('0', '2', 7, False), ('1', '0', 8, True), ('1', '2', 5, True), ('2', '0', 7, False)]
}

grafo_luan2 = {
    "num_vertices": 4,
    "arestas":  [('0', '1', 3, True), ('0', '3', 4, False), ('1', '0', 1, True), ('1', '2', 2, False), ('3', '2', 2, False)]
}

grafo_luan3 = {
    "num_vertices": 5,
    "arestas":  [('0', '1', 4, False), ('0', '2', 8, False), ('0', '3', 5, True), ('1', '0', 4, False), ('1', '4', 3, False), ('2', '0', 8, False),
                 ('2', '4', 1, True), ('3', '4', 2, True), ('4', '1', 3, False)]
}
grafo_luan4 = {
    "num_vertices": 5,
    "arestas":  [('0', '2', 3, True), ('0', '3', 4, True), ('1', '0', 2, True), ('2', '1', 1, True), ('2', '3', 5, False),
                 ('3', '2', 5, False), ('3', '4', 6, True), ('4', '0', 2, True)]
}
grafo_luan5 = {
    "num_vertices": 6,
    "arestas":  [('0', '1', 1, False), ('0', '3', 2, False), ('1', '0', 1, False), ('1', '3', 2, True), ('1', '5', 3, False),
('2', '1', 2, True), ('3', '0', 2, False), ('3', '4', 1, True), ('4', '5', 1, True), ('5', '1', 3, False), ('5', '2', 4, True)]
}

grafo_luan6 = {
    "num_vertices": 7,
    "arestas":  [('0', '2', 7, True), ('1', '0', 6, True), ('1', '2', 6, False), ('1', '6', 5, False), ('2', '1', 6, False),
                 ('2', '3', 5, False), ('3', '2', 5, False), ('3', '4', 5, True), ('4', '1', 4, True), ('4', '5', 5, False),
                 ('5', '4', 5, False), ('5', '6', 20, False), ('6', '1', 5, False), ('6', '5', 20, False)]
}


