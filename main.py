import json
from tkinter import *
from tkinter import filedialog
import traceback
import webbrowser

def generate_file():
    try:
        # Читаем значения из полей ввода
        max_price = int(maxprice_entry.get())
        sell_price = int(sellprice_entry.get())
        classnames = classnames_text.get("1.0", END).splitlines()
        
        # Создаем список для сохранения данных
        items = []
        
        # Создаем элемент для каждого класснейма
        for classname in classnames:
            item = {
                "ClassName": classname.strip(),
                "MaxPriceThreshold": max_price,
                "MinPriceThreshold": sell_price,
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
        # Читаем значения из полей ввода
        max_price = int(maxprice_entry.get())
        sell_price = int(sellprice_entry.get())
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
                f.write(f"  {classname.strip()}, *, {max_price}, {sell_price}\n")
        print("Файл успешно сохранен")
    except Exception as e:
        traceback.print_exc()
        print(f"Ошибка: {e}")


def generate_json_file():
    try:
        # Читаем значения из полей ввода
        max_price = int(maxprice_entry.get())
        sell_price = int(sellprice_entry.get())
        classnames = classnames_text.get("1.0", END).splitlines()
        
        # Создаем список для сохранения данных
        items = []
        
        # Создаем элемент списка для каждого класснейма
        for classname in classnames:
            item = f"{classname.strip()},0.92,-1,1,{max_price},-1,1"
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

# Создаем поля для ввода цен
maxprice_label = Label(window, text="By price:", font=("Arial", 12))
maxprice_label.place(x=540, y=10)
maxprice_entry = Entry(window, font=("Arial", 12))
maxprice_entry.place(x=540, y=30)
sellprice_label = Label(window, text="Sell price:", font=("Arial", 12))
sellprice_label.place(x=540, y=70)
sellprice_entry = Entry(window, font=("Arial", 12))
sellprice_entry.place(x=540, y=90)

# Создаем кнопку для генерации файла JSON
generate_button = Button(window, text="Expansion Market", command=generate_file, font=("Arial", 12))
generate_button.place(x=540, y=150)

# Создаем кнопку для генерации файла TXT
generate_txt_button = Button(window, text="Dr.Jones", command=generate_txt_file, font=("Arial", 12))
generate_txt_button.place(x=540, y=190)

# Создаем кнопку для генерации файла JSON для другого сервиса
generate_json_button = Button(window, text="Trader Plus", command=generate_json_file, font=("Arial", 12))
generate_json_button.place(x=540, y=230)

# Создаем кнопку для открытия ссылки на Discord-сервер
discord_button = Button(window, text="Discord", command=open_discord, font=("Arial", 12))
discord_button.place(x=10, y=360)

window.configure(bg="#1C1C1C")
for widget in window.winfo_children():
    widget.configure(bg="#1C1C1C", fg="#FFFFFF")

# Устанавливаем название окна
window.title("DayZ Trader Config Generator")

# Запускаем главный цикл обработки событий окна
window.mainloop()