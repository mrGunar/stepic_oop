"""Испытание свойствами и методами

Каждый сервер может отправлять пакет любому другому серверу сети.
Для этого у каждого есть свой уникальный IP-адрес. Для простоты -
это просто целое (натуральное) число от 1 и до N, где N - общее
число серверов. Алгоритм, следующий. Предположим, сервер с IP =
2 собирается отправить пакет информации серверу с IP = 3. Для этого,
он сначала отправляет пакет роутеру, а уже тот, смотрит на IP-адрес и
пересылает пакет нужному узлу (серверу).
"""
from copy import copy


class Server:
    """Класс для описания работы серверов в сети"""
    N = 0

    def __new__(cls):
        cls.N += 1
        return super().__new__(cls)

    def __init__(self):
        self._ip = Server.N
        self.buffer = []

    @staticmethod
    def send_data(data):
        """
        для отправки информационного пакета data (объекта класса Data)
        с указанным IP-адресом получателя (пакет отправляется роутеру и
        сохраняется в его буфере - локальном свойстве buffer)
        """
        router = Router()
        router.buffer.append(data)

    def get_data(self):
        """возвращает список принятых пакетов
        (если ничего принято не было, то возвращается пустой список)
         и очищает входной буфер
         """
        if self.buffer:
            _data = copy(self.buffer)
            self.buffer.clear()
            return _data
        return []

    def get_ip(self):
        """возвращает свой IP-адрес"""
        return self._ip


class Router:
    """
    Класс для описания работы роутеров в сети
    (в данной задаче полагается один роутер)
    """
    __instance = None
    servers = []
    buffer = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def link(self, server):
        """
        для присоединения сервера server (объекта класса Server) к роутеру
        """
        self.servers.append(server)

    def unlink(self, server):
        """
        для отсоединения сервера server (объекта класса Server) от роутера
        """
        self.servers.pop(self.servers.index(server))

    def send_data(self):
        """
        для отправки всех пакетов (объектов класса Data) из буфера роутера
        соответствующим серверам (после отправки буфер должен очищаться)
        """
        for server in self.servers:
            for data in self.buffer:
                if server.ip == data.ip:
                    server.buffer.append(data)
        self.buffer.clear()


class Data:
    """Класс для описания пакета информации"""
    def __init__(self, data, _ip):
        self._data = data
        self._ip = _ip

    @property
    def data(self):
        """data"""
        return self._data

    @property
    def ip(self):
        """ip"""
        return self._ip
