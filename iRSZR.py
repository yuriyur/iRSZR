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

while True:
    event, values = window.read()
    if event is None or event == 'Exit':
        break

    input_directory, size = values[0], values[1]

    d = datetime.strftime(datetime.now(), "%Y-%m-%d")
    output_directory=input_directory+'/'+d+'/'
    progress_bar = window.FindElement('progress')
    progress_bar.UpdateBar(0, 50)

    files=[]
    for file in os.listdir(input_directory):
        if file.endswith(".jpg"):
            files.append(os.path.join(file))
            print(os.path.join(input_directory, file))

    print(input_directory, size, output_directory, files)

    if os.path.exists(output_directory):
        print('Path found')
    else:
        print('Сreate folder')
        os.mkdir(str(output_directory))

    def resize_image(input_image_path,
                    output_image_path,
                    size):
        original_image = Image.open(input_image_path)
        width, height = original_image.size
        scale = size / max(width, height)
        print('The original image size is {wide} wide x {height} '
            'high'.format(wide=width, height=height))
    
        resized_image = original_image.resize((int(width * scale), int(height * scale)), Image.ANTIALIAS)
        width, height = resized_image.size
        print('The resized image size is {wide} wide x {height} '
            'high'.format(wide=width, height=height))
        #resized_image.show()
        resized_image.save(output_image_path, "jpeg")
    
    if __name__ == '__main__':
        i = 0
        while i < len(files):
            p = len(files)
            progress_bar.UpdateBar(i, p)
            print(files[i])
            resize_image(input_image_path=input_directory+'/'+files[i],
                        output_image_path=output_directory+'/'+d+'-'+str(i)+'.jpg',
                        size=int(size))
            i += 1
        progress_bar.UpdateBar(p, p)

window.close()