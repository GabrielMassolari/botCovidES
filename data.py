import pandas as pd
import requests
from unidecode import unidecode
import folium
from folium.plugins import HeatMap
import selenium
from selenium import webdriver
import pathlib
from time import sleep
import pyscreenshot
from PIL import Image


dados = pd.read_csv("dados.csv", encoding="latin1")


def total_cases(city):
    if city == "es":
        return len(dados)
    else:
        return len(dados[dados['Municipio'] == city])


def active_cases(city):
    if city == "es":
        return len(dados[dados['StatusNotificacao'] == "Em Aberto"])
    else:
        return len(dados[(dados['Municipio'] == city) & (dados['StatusNotificacao'] == "Em Aberto")])


def top_neighborhood(city, info="total"):
    if info == "total":
        return dict(dados[dados['Municipio'] == city]['Bairro'].value_counts()[:10])
    elif info == "active":
        return dict(
            dados[(dados['Municipio'] == city) & (dados['StatusNotificacao'] == "Em Aberto")]['Bairro'].value_counts()[:10])


def cep(cep):
    req = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    resp = req.json()

    city = unidecode(resp["localidade"]).capitalize()

    return city


def lat_lng():
    lat = dados[dados['StatusNotificacao'] == "Em Aberto"].Latitude.to_list()
    lng = dados[dados['StatusNotificacao'] == "Em Aberto"].Longitude.to_list()

    return lat, lng


# def graph(city, info="total", md=None):
#   print(city)


def generate_map():
    lat, lng = lat_lng()

    mapa = folium.Map(
        location=[-19.5446857, -40.5188893],
        tiles='Stamen Terrain',
        zoom_start=8.25
    )

    HeatMap(list(zip(lat, lng)), blur=30).add_to(mapa)
    mapa.save("mapa.html")

    url = str(pathlib.Path().absolute()) + '/mapa.html'
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get(url)
    browser.fullscreen_window()
    sleep(7)
    im = pyscreenshot.grab()
    im.save("mapa.png")
    im = Image.open('mapa.png')
    map_i = im.crop((480, 140, 1420, 920))
    map_i = map_i.save("mapa.png")
    browser.close()
    print()



