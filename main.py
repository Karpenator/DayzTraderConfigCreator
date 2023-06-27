import json
from tkinter import *
from tkinter import filedialog
import traceback
import webbrowser


def generate_file():
    try:
        # Читаем значение из поля ввода
        classnames = classnames_text.get("1.0", END).splitlines()
        
        # Создаем список для сохранения данных
        items = []
        
        # Создаем элемент для каждого класснейма
        for classname in classnames:
            item = {
                "ClassName": classname.strip(),
                "MaxPriceThreshold": 6000,
                "MinPriceThreshold": 6000,
                "SellPricePercent": -1,
                "MaxStockThreshold": 999999999,
                "MinStockThreshold": 1,
                "SpawnAttachments": [],
                "Variants": []
            }
            items.append(item)
        
        # Создаем словарь для сохранения данных
        data = {
            "m_Version": 12,
            "DisplayName": "Отображаемое имя категории",
            "Icon": "Deliver",
            "Color": "FBFCFEFF",
            "IsExchange": 0,
            "InitStockPercent": 75.0,
            "Items": items
        }
        
        # Открываем диалог сохранения файла
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        # Записываем данные в файл
        with open(file_path, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print("Файл успешно сохранен")
    except Exception as e:
        traceback.print_exc()
        print(f"Ошибка: {e}")


def generate_txt_file():
    try:
        # Читаем значение из поля ввода
        classnames = classnames_text.get("1.0", END).splitlines()
        
        # Открываем диалог сохранения файла
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("TXT files", "*.txt"), ("All files", "*.*")]
        )
        
        # Записываем данные в файл
        with open(file_path, "w") as f:
            f.write("<Category> Escape From Tarkov\n")
            for classname in classnames:
                f.write(f"  {classname.strip()}, *, 6000, 3000\n")
        print("Файл успешно сохранен")
    except Exception as e:
        traceback.print_exc()
        print(f"Ошибка: {e}")


def generate_json_file():
    try:
        # Читаем значение из поля ввода
        classnames = classnames_text.get("1.0", END).splitlines()
        
        # Создаем список для сохранения данных
        items = []
        
        # Создаем элемент списка для каждого класснейма
        for classname in classnames:
            item = f"{classname.strip()},0.92,-1,1,6000,-1,1"
            items.append(item)
        
        # Создаем словарь для сохранения данных
        data = {
            "CategoryName": "Escape From Tarkov",
            "Products": items
        }
        
        # Открываем диалог сохранения файла
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        # Записываем данные в файл
        with open(file_path, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print("Файл успешно сохранен")
    except Exception as e:
        traceback.print_exc()
        print(f"Ошибка: {e}")


def open_discord():
    webbrowser.open_new("https://discord.gg/Mj7tFHe8Nz")


# Создаем окно
window = Tk()

# Устанавливаем размер окна
window.geometry("800x400")

# Создаем поле для ввода класснеймов
classnames_label = Label(window, text="Classnames:", font=("Arial", 12))
classnames_label.place(x=10, y=10)
classnames_text = Text(window, height=15, width=50, font=("Arial", 12))
classnames_text.place(x=10, y=30)

# Создаем кнопку для генерации файла JSON
generate_button = Button(window, text="Expansion", command=generate_file, font=("Arial", 16))
generate_button.place(x=540, y=80)

# Создаем кнопку для генерации файла txt
txt_button = Button(window, text="Dr.Jones", command=generate_txt_file, font=("Arial", 16))
txt_button.place(x=540, y=140)

# Создаем кнопку для генерации файла json
json_button = Button(window, text="TraderPlus", command=generate_json_file, font=("Arial", 16))
json_button.place(x=540, y=200)

# Создаем кнопку для связи с разработчиком
discord_button = Button(window, text="Связь с разработчиком", command=open_discord, font=("Arial", 16))
discord_button.place(x=540, y=280)

# Запускаем главный цикл окна
window.mainloop()