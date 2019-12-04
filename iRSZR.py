from datetime import datetime, date, time
import os
from PIL import Image
import PySimpleGUI as sg

layout = [  [sg.Text('Выберите папку:', size=(20, 1)), sg.InputText(), sg.FolderBrowse('...')],
            [sg.Text('Размер изображений по максимальной стороне в px:', size=(40, 1)), sg.Input(1600, size=(10, 1))], 
            [sg.Text('Прогресс'), sg.ProgressBar(1, orientation='h', size=(44, 20), key='progress')],
            [sg.Button('Ок', size=(10, 1)), sg.Cancel('Exit')]
         ]

window = sg.Window('iRSZR - изменение размера изображений пакетно', layout)