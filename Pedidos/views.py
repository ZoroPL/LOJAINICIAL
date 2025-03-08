# from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render


# Simulando uma lista de pedidos
def home(request):
    # Exemplo de pedidos simulados
    pedidos = [
        {'id': 1, 'itens': ['Pizza de Calabresa', 'agua com gas', 'suco'],
         'hora': '12:30'},
        {'id': 2, 'itens': ['Hamburguer'], 'hora': '13:00'},
        {'id': 3, 'itens': ['Coca-Cola'], 'hora': '13:15'}]

    # Renderizando a página com a lista de pedidos
    return render(request, 'pedidos.html', {'pedidos': pedidos})


def calcular_total(pedido):
    total_itens = sum(item['quantidade'] * item['preco']
                      for item in pedido['itens'])

    # Adicionar taxa de entrega se for pedido para entrega
    if pedido['entrega']:
        total_itens += 1  # Taxa de entrega R$ 1

    return total_itens


def pedido(request, number):

    pedidos = [
        {
            'id': 1,
            'cliente': {
                'nome': 'João Silva',
                'telefone': '1234-5678',
                'endereco': 'Rua A, 123'
            },
            'itens': [
                {'nome': 'Pizza de Calabresa', 'quantidade': 1, 'preco': 30.00},
                {'nome': 'Água com Gás', 'quantidade': 2, 'preco': 5.00},
                {'nome': 'Suco', 'quantidade': 1, 'preco': 7.00}
            ],
            'hora': '12:30',
            'entrega': True  # Define se o pedido será entregue no endereço do cliente
        },
        {
            'id': 2,
            'cliente': {
                'nome': 'Maria Oliveira',
                'telefone': '9876-5432',
                'endereco': 'Rua B, 456'
            },
            'itens': [
                {'nome': 'Hamburguer', 'quantidade': 2, 'preco': 15.00}
            ],
            'hora': '13:00',
            'entrega': False  # Pedido para retirar no local, sem taxa de entrega
        },
        {
            'id': 3,
            'cliente': {
                'nome': 'Carlos Santos',
                'telefone': '1122-3344',
                'endereco': 'Rua C, 789'
            },
            'itens': [
                {'nome': 'Coca-Cola', 'quantidade': 3, 'preco': 6.00}
            ],
            'hora': '13:15',
            'entrega': True  # Pedido para entrega
        }
    ]

    # pedido = Pedido.objects.get(id=id)  # Busca o pedido no banco de dados
    pedido = next(
        (pedido for pedido in pedidos if pedido['id'] == number),
        None)

    return render(
        request, 'pedido_detail.html',
        context={'pedido': pedido,
                 'total': calcular_total(pedido)})
