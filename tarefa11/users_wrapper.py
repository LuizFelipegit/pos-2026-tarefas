import requests

URL_BASE = "https://jsonplaceholder.typicode.com"


def listar_usuarios():

    requisicao = requests.get(f"{URL_BASE}/users")

    if requisicao.ok:
        return requisicao.json()

    return []


def buscar_usuario(id_usuario):

    requisicao = requests.get(f"{URL_BASE}/users/{id_usuario}")

    if requisicao.ok:
        return requisicao.json()

    return None


def cadastrar_usuario(dados_usuario):

    requisicao = requests.post(
        f"{URL_BASE}/users",
        json=dados_usuario
    )

    if requisicao.status_code == 201:
        return requisicao.json()

    return None


def atualizar_usuario(id_usuario, novos_dados):

    requisicao = requests.put(
        f"{URL_BASE}/users/{id_usuario}",
        json=novos_dados
    )

    if requisicao.ok:
        return requisicao.json()

    return None


def remover_usuario(id_usuario):

    requisicao = requests.delete(
        f"{URL_BASE}/users/{id_usuario}"
    )

    return requisicao.ok