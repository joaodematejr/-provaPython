import datetime

""" Decorator permite adicionar comportamento em um objeto em tempo de execução ele acrega responsabilidades a um objeto no exemplo abaixo tem um decorator que mostra o tempo de execução da soma das 4 variaveis  """
""" Padrão de projeto é uma solução geral para os problemas que ocorre com frequencia exemplo validação de CPF será utilizado em toda aplicação. Neste caso o mais apropriado é centralizar o código em vez de ficar criando vários métodos, em várias partes do projeto, apenas para validar o CPF """


def calculate_time_decorator(function):
    def calculate_time():
        print(datetime.datetime.now())
        function()
        print(datetime.datetime.now())

    return calculate_time


@calculate_time_decorator
def my_function():
    number1 = 19999999
    number2 = 6925262
    number3 = 322662626
    number4 = 55215425
    result = number1 + number2 + number3 + number4
    print(result)


my_function()
