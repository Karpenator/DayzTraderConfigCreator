import json
from tkinter import *
from tkinter import filedialog
import traceback
import webbrowser
from tkinter import ttk

classnames = ""

# Функция выбора папки с файлом
def open_file():
    global classnames
    classnames_file = filedialog.askopenfilename(title="Select an Classnames File")
    with open(classnames_file, "r") as f:
        classnames = f.read()
    classnames_text.delete("1.0", END)
    classnames_text.insert(END, classnames)

def generate_file():
    try:
        # Читаем значения из полей ввода
        max_price = int(maxprice_entry.get())
        sell_price = int(sellprice_entry.get())
        max_stock = int(max_stock_entry.get())
        min_stock = int(min_stock_entry.get())
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
                "MaxStockThreshold": max_stock,
                "MinStockThreshold": min_stock,
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
        max_price = int(maxprice_entry_tab2.get())
        sell_price = int(sellprice_entry_tab2.get())
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
        max_price = int(maxprice_entry_tab3.get())
        sell_price = int(sellprice_entry_tab3.get())
        classnames = classnames_text.get("1.0", END).splitlines()
        
        # Создаем список для сохранения данных
        items = []
        
        # Создаем элемент списка для каждого класснейма
        for classname in classnames:
            item = f"{classname.strip()},1,-1,1,{max_price},{sell_price}"
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

def generate_ultima_file():
    try:
        # Читаем значения из полей ввода
        max_price = int(maxprice_entry_tab4.get())
        sell_price = int(sellprice_entry_tab4.get())
        max_stock = int(max_stock_entry_tab4.get())
        tradersids = int(tradersids_entry_tab4.get())
        section = str(section_entry_tab4.get())
        classnames = classnames_text.get("1.0", END).splitlines()
        
        # Создаем список для сохранения данных
        items = []
        
        # Создаем элемент для каждого класснейма
        for index in range(len(classnames)):
            item = {
                "m_ArrayIndex": -1,
                "m_Section": section,
                "m_Classname": classnames[index],
                "m_TradersIds": [tradersids],
                "m_IsBuy": 1,
                "m_IsSell": 1,
                "m_PriceBuy": max_price,
                "m_PriceSell": sell_price,
                "m_ReputationNeed": 0,
                "m_ReputationCostBuy": 0,
                "m_ReputationCostSell": 0,
                "m_ReputationAddBuy": 0,
                "m_ReputationAddSell": 0,
                "m_Fraction": "-",
                "m_Amount": max_stock,
                "m_IsScript": 0,
                "m_DisplayClassname": "",
                "m_DisplaySectionName": "",
                "m_MinAmountTo": 0,
                "m_AmountTo": 0
            }
            items.append(item)       
            # Создаем список словарей
            data = items
        
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

def open_donate():
    webbrowser.open_new("https://boosty.to/karpenator/donate")

# Создаем окно программы
root = Tk()
root.title("DayZ Trader Config Generator")
root.configure(background="#1C1C1C")

# Создаем виджет Notebook, в котором будут находиться вкладки
notebook = ttk.Notebook(root)
notebook.pack(side=RIGHT, fill=BOTH, expand=True)

# Создаем левую часть интерфейса с окном для класснеймов
left_frame = Frame(root, bg="#1C1C1C")
left_frame.pack(side=LEFT, fill=Y, pady=20, padx=20)

classnames_text = Text(left_frame, height=root.winfo_height()//20, width=50, font=("Comic Sans MS", 12))
classnames_text.pack(side=LEFT, padx=10, pady=10, fill=Y)
open_file_button = Button(left_frame, text="Open Classnames File", command=open_file, font=("Comic Sans MS", 12))
open_file_button.pack(side=TOP, padx=10, pady=10)
open_discord_button = Button(left_frame, text="DISCORD", command=open_discord, font=("Comic Sans MS", 14))
open_discord_button.pack(side=TOP, padx=10, pady=10)
open_donate_button = Button(left_frame, text="Donate", command=open_donate, font=("Comic Sans MS", 14))
open_donate_button.pack(side=BOTTOM, padx=10, pady=10)


# Создаем первую вкладку
tab1 = Frame(notebook, bg="#1C1C1C")
tab1.pack(fill=BOTH, expand=True)

maxprice_label = Label(tab1, text="Max Price Threshold:", font=("Comic Sans MS", 12))
maxprice_label.pack(side=TOP, padx=10, pady=10)
maxprice_entry = Entry(tab1, font=("Comic Sans MS", 12))
maxprice_entry.insert(0, "0")  # устанавливаем значение по умолчанию
maxprice_entry.pack(side=TOP, padx=10, pady=10)

sellprice_label = Label(tab1, text="Min Price Threshold:", font=("Comic Sans MS", 12))
sellprice_label.pack(side=TOP, padx=10, pady=10)
sellprice_entry = Entry(tab1, font=("Comic Sans MS", 12))
sellprice_entry.insert(0, "0")  # устанавливаем значение по умолчанию
sellprice_entry.pack(side=TOP, padx=10, pady=10)

max_stock_label = Label(tab1, text="Max Stock Threshold:", font=("Comic Sans MS", 12))
max_stock_label.pack(side=TOP, padx=10, pady=10)
max_stock_entry= Entry(tab1, font=("Comic Sans MS", 12))
max_stock_entry.insert(0, "0")
max_stock_entry.pack(side=TOP, padx=10, pady=10)

min_stock_label = Label(tab1, text="Min Stock Threshold:", font=("Comic Sans MS", 12))
min_stock_label.pack(side=TOP, padx=10, pady=10)
min_stock_entry= Entry(tab1, font=("Comic Sans MS", 12))
min_stock_entry.insert(0, "0")
min_stock_entry.pack(side=TOP, padx=10, pady=10)

generate_button = Button(tab1, text="Generate Config", command=generate_file, font=("Comic Sans MS", 12))
generate_button.pack(side=TOP, padx=10, pady=10)


# Создаем вторую вкладку
tab2 = Frame(notebook, bg="#1C1C1C")
tab2.pack(fill=BOTH, expand=True)

maxprice_label_tab2 = Label(tab2, text="By price:", font=("Comic Sans MS", 12))
maxprice_label_tab2.pack(side=TOP, padx=10, pady=10)
maxprice_entry_tab2 = Entry(tab2, font=("Comic Sans MS", 12))
maxprice_entry_tab2.insert(0, "0")  # устанавливаем значение по умолчанию
maxprice_entry_tab2.pack(side=TOP, padx=10, pady=10)

sellprice_label_tab2 = Label(tab2, text="Sell price:", font=("Comic Sans MS", 12))
sellprice_label_tab2.pack(side=TOP, padx=10, pady=10)
sellprice_entry_tab2 = Entry(tab2, font=("Comic Sans MS", 12))
sellprice_entry_tab2.insert(0, "0")  # устанавливаем значение по умолчанию
sellprice_entry_tab2.pack(side=TOP, padx=10, pady=10)

generate_txt_button = Button(tab2, text="Generate TXT Config", command=generate_txt_file, font=("Comic Sans MS", 12))
generate_txt_button.pack(side=TOP, padx=10, pady=10)

# Создаем третью вкладку
tab3 = Frame(notebook, bg="#1C1C1C")
tab3.pack(fill=BOTH, expand=True)

maxprice_label_tab3 = Label(tab3, text="By price:", font=("Comic Sans MS", 12))
maxprice_label_tab3.pack(side=TOP, padx=10, pady=10)
maxprice_entry_tab3 = Entry(tab3, font=("Comic Sans MS", 12))
maxprice_entry_tab3.insert(0, "0")  # устанавливаем значение по умолчанию
maxprice_entry_tab3.pack(side=TOP, padx=10, pady=10)

sellprice_label_tab3 = Label(tab3, text="Sell price:", font=("Comic Sans MS", 12))
sellprice_label_tab3.pack(side=TOP, padx=10, pady=10)
sellprice_entry_tab3 = Entry(tab3, font=("Comic Sans MS", 12))
sellprice_entry_tab3.insert(0, "0")  # устанавливаем значение по умолчанию
sellprice_entry_tab3.pack(side=TOP, padx=10, pady=10)

generate_json_button = Button(tab3, text="Generation JSON Config", command=generate_json_file, font=("Comic Sans MS", 12))
generate_json_button.pack(side=TOP, padx=10, pady=10)

# Создаем четвёртую вкладку
tab4 = Frame(notebook, bg="#1C1C1C")
tab4.pack(fill=BOTH, expand=True)

section_label_tab4 = Label(tab4, text="Section:", font=("Comic Sans MS", 12))
section_label_tab4.pack(side=TOP, padx=10, pady=10)
section_entry_tab4 = Entry(tab4, font=("Comic Sans MS", 12))
section_entry_tab4.insert(0, "#STR_ULTIMA_TRADE_SECTION_FOOD")  # устанавливаем значение по умолчанию
section_entry_tab4.pack(side=TOP, padx=10, pady=10)

tradersids_label_tab4 = Label(tab4, text="Traders ID:", font=("Comic Sans MS", 12))
tradersids_label_tab4.pack(side=TOP, padx=10, pady=10)
tradersids_entry_tab4 = Entry(tab4, font=("Comic Sans MS", 12))
tradersids_entry_tab4.insert(0, "0")  # устанавливаем значение по умолчанию
tradersids_entry_tab4.pack(side=TOP, padx=10, pady=10)


max_stock_label_tab4 = Label(tab4, text="Amount:", font=("Comic Sans MS", 12))
max_stock_label_tab4.pack(side=TOP, padx=10, pady=10)
max_stock_entry_tab4= Entry(tab4, font=("Comic Sans MS", 12))
max_stock_entry_tab4.insert(0, "0")
max_stock_entry_tab4.pack(side=TOP, padx=10, pady=10)

maxprice_label_tab4 = Label(tab4, text="Price Buy:", font=("Comic Sans MS", 12))
maxprice_label_tab4.pack(side=TOP, padx=10, pady=10)
maxprice_entry_tab4 = Entry(tab4, font=("Comic Sans MS", 12))
maxprice_entry_tab4.insert(0, "0")  # устанавливаем значение по умолчанию
maxprice_entry_tab4.pack(side=TOP, padx=10, pady=10)

sellprice_label_tab4 = Label(tab4, text="Price Sell:", font=("Comic Sans MS", 12))
sellprice_label_tab4.pack(side=TOP, padx=10, pady=10)
sellprice_entry_tab4 = Entry(tab4, font=("Comic Sans MS", 12))
sellprice_entry_tab4.insert(0, "0")  # устанавливаем значение по умолчанию
sellprice_entry_tab4.pack(side=TOP, padx=10, pady=10)

amount_label_tab4 = Label(tab4, text="Amount:", font=("Comic Sans MS", 12))
amount_label_tab4.pack(side=TOP, padx=10, pady=10)
amount_entry_tab4= Entry(tab4, font=("Comic Sans MS", 12))
amount_entry_tab4.insert(0, "0")
amount_entry_tab4.pack(side=TOP, padx=10, pady=10)

generate_button_tab4 = Button(tab4, text="Generate Config", command=generate_ultima_file, font=("Comic Sans MS", 12))
generate_button_tab4.pack(side=TOP, padx=10, pady=10)

# Добавляем вкладки в виджет Notebook
notebook.add(tab1, text="Expansion Trader")
notebook.add(tab2, text="Dr.Jones")
notebook.add(tab3, text="Trader Plus")
notebook.add(tab4, text="Ultima")

# Получаем желаемую ширину правой части окна программы
right_frame_width = max(
    maxprice_label.winfo_reqwidth(),
    maxprice_entry.winfo_reqwidth(),
    sellprice_label.winfo_reqwidth(),
    sellprice_entry.winfo_reqwidth(),
    generate_button.winfo_reqwidth(),
    maxprice_label_tab2.winfo_reqwidth(),
    maxprice_entry_tab2.winfo_reqwidth(),
    sellprice_label_tab2.winfo_reqwidth(),
    sellprice_entry_tab2.winfo_reqwidth(),
    generate_txt_button.winfo_reqwidth(),
    maxprice_label_tab3.winfo_reqwidth(),
    maxprice_entry_tab3.winfo_reqwidth(),
    generate_json_button.winfo_reqwidth()
)


# Запускаем главный цикл приложения
root.mainloop()