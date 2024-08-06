from time import sleep
from collections import Counter
from typing import List
import os
import json

try:
    import urllib3
except ModuleNotFoundError or ImportError:
    os.system('pip install urllib3')
import re
import random
import string

url_pattern = r'^(https?:\/\/|ftp:\/\/|www\.)([a-zA-Z0-9-]+\.[a-zA-Z0-9-]+)(\/[^\s]*)?$'
os.system('git pull')
banner = """8888888 8888888b.   .d8888b.  
  888   888  "Y88b d88P  Y88b 
  888   888    888 Y88b.      
  888   888    888  "Y888b.   
  888   888    888     "Y88b. 
  888   888    888       "888 
  888   888  .d88P Y88b  d88P 
8888888 8888888P"   "Y8888P"  
       @By Br3k Albany"""


def Random_string() -> str:
    a = random.choices(string.ascii_uppercase + string.digits, k=8)
    b = ''.join(a)
    return b


def is_valid_url(url):
    return re.match(url_pattern, url) is not None


try:
    import requests
    from requests import Session
except ModuleNotFoundError or ImportError:
    os.system('pip install requests')
try:
    import rich
except ModuleNotFoundError or ImportError:
    os.system('pip install rich')
finally:
    from rich.console import Console

    console = Console()
try:
    import bs4
except ModuleNotFoundError or ImportError:
    os.system('pip install bs4')
finally:
    from bs4 import BeautifulSoup
BR3k = b''


def Manipulate_bytes() -> bytes:
    return BR3k


class Sanityze_File:
    def __init__(self, *filename):
        if not Manipulate_bytes() == b'OSX':
            exit('')
        console.print(banner, style="bold green3 underline")
        self.req: Session = requests.Session()
        self.index_problems: List = []
        self.index_problems_without_split: List = []
        self.filename = filename[0]
        self.check_file: bool = self.valid_file
        self.data_file_splitlines: List = []
        self.lab_file: str = "/sdcard/BR3K/Br3k.Txt"
        self.final_file: str = "/sdcard/BR3K/Fuck_You.txt"
        self.fix_prob: List = []
        self.indexes_ready: List = []
        self.json_file = "/sdcard/BR3K/data.json"
        self.Sterilization_IDS_File(self.filename, self.lab_file)
        self.data_file: str = self.valid_lab_file  # this for read file and readlines
        # for analyze results
        self.values: List = []
        self.set_values()
        # this for store analyze data
        #
        data = self.catch_duplicating(self.data_file_splitlines)
        ids_Structure = {"DATA": {}}
        index = 1
        count: List = []
        for number, indices in data.items():
            ids_Structure["DATA"][number] = indices
            count_kr = len(indices)
            print(f"[{index}]-ID: {number} Repeat : {count_kr}")
            count.append(count_kr)
            index += 1
        print("\n")
        console.print(f"Total Repeat IDS : {sum(count)}", style="bold green3 underline")
        x: str = str(input("\033[1;34mDELETE REPEAT IDS ? [Y/N] : "))
        if x in ['ya', 'y', 'yes', 'Y', 'YES', 'YE', '', ' ']:
            with open(self.json_file, 'w', encoding='utf-8') as json_file:
                json.dump(ids_Structure, json_file, ensure_ascii=False, indent=4)
            console.print("Removing Now !!")
            self.extract_all_ids_from_file()
        else:
            exit('\033[1;32mbye bye nothing fix it')
        os.system('clear')
        x: str = str(input("\033[1;34mSTART VALID IDS|PASSWORDS [Y/N]"))
        if x not in ['ya', 'y', 'yes', 'Y', 'YES', 'YE', '', ' ']:
            exit(f'bye bye save file in {self.lab_file}')
        check_file: bool = self.Check_IS_Ids_File_Or_No()
        if check_file:
            if len(self.index_problems) > 0:
                print("#" * 30)
                self.fix_prob.append("SHORT")
                console.print("IDS WITH Very SHORT PASSWORD !", style="bold green3")
                for index in self.index_problems:
                    print("\033[1;32m" + self.data_file_splitlines[index] + f" LINE [{index + 1}]")
                print("\033[1;32m+" * 20)
            if len(self.index_problems_without_split) > 0:
                print("#" * 30)
                self.fix_prob.append("SHORT2")
                console.print("IDS WITHOUT [|] SPLIT !", style="bold green3")
                for index in self.index_problems_without_split:
                    print("\033[1;32m" + self.data_file_splitlines[index] + f" LINE [{index + 1}]")
                print("\033[1;32m+" * 20)
            x: str = str(input("\033[1;34mDO YOU WANT FIX PROBLEMS ? [y/n]"))
            if x in ['ya', 'y', 'yes', 'Y', 'YES', 'YE', '', ' ']:
                self.fix_all_problems()
            else:
                exit(f'\033[1;32mbye bye nothing fix it {self.lab_file}')

    def extract_all_ids_from_file(self):
        extracted_ids: List = []
        with open(self.json_file, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        for key in data["DATA"]:
            ids_list = data["DATA"][key]
            if len(ids_list) > 1:
                extracted_ids.extend(ids_list[1:])
        for index in sorted(extracted_ids, reverse=True):
            del self.data_file_splitlines[index]
        self.data_file = '\n'.join(self.data_file_splitlines)
        with open(self.lab_file, 'w', encoding="utf-8") as newfile:
            newfile.write(self.data_file)

    def fix_all_problems(self):
        if len(self.fix_prob) == 2:
            self.SHORT()
            self.SHORT2()
        else:
            if self.fix_prob[0] == "SHORT":
                self.SHORT()
            elif self.fix_prob[0] == "SHORT2":
                self.SHORT2()
        if len(self.indexes_ready) > 0:
            for index in sorted(self.indexes_ready, reverse=True):
                del self.data_file_splitlines[index]
            file: str = '\n'.join(self.data_file_splitlines)
            open(self.final_file, 'w', encoding="utf-8").write(file)
            print("\n")
            os.system('clear')
            console.print(banner, style="bold green3 underline")
            console.print(f"OLD Line : {self.values[1]}", style="bold green3")
            console.print(f"New Lines : {len(self.data_file_splitlines)}", style="bold green3")
            console.print(f"Old Size : {self.convert_size(self.values[0])}", style="bold green3")
            console.print(f"New Sizes : {self.convert_size(os.path.getsize(self.final_file))}", style="bold green3")
            exit(f"\033[1;32mfile save in [{self.final_file}]")

    def SHORT(self):
        print("+" * 30)
        for index in self.index_problems:
            try:
                catch_id: str = self.data_file_splitlines[index].split("|")[0]
                int(catch_id)
                password = self.Send_Req_To_Account(catch_id)
                if password == "Facebook":
                    console.print(f"ID : {catch_id} is Closed Account | Line {index}", style="bold red3")
                    self.indexes_ready.append(index)
                else:
                    console.print(f"[+]-ID : {catch_id} Is Account New Password is {password} Line {index}",
                                  style="bold green3")
                    self.data_file_splitlines[index] = f"{catch_id}|{password}"
            except ValueError:
                print(
                    f"\033[1;31m ID : {self.data_file_splitlines[index].split('|')[0]} not Account removed now Line {index}")
                self.indexes_ready.append(index)

    def SHORT2(self):
        print("+" * 30)
        for index in self.index_problems_without_split:
            try:
                catch_id: str = self.data_file_splitlines[index]
                int(catch_id)
                password = self.Send_Req_To_Account(catch_id)
                if password == "Facebook":
                    console.print(f"ID : {catch_id} is Closed Account | Line {index}", style="bold red3")
                    self.indexes_ready.append(index)
                else:
                    console.print(f"[+]-ID : {catch_id} Is Account New Password is {password} Line {index}",
                                  style="bold green3")
                    self.data_file_splitlines[index] = f"{catch_id}|{password}"
            except ValueError:
                self.indexes_ready.append(index)

    def Check_IS_Ids_File_Or_No(self) -> bool:
        if len(self.data_file_splitlines) < 10:
            exit("\033[1;32mSmall_Ids_File")
        for index, lines in enumerate(self.data_file_splitlines):
            try:
                checkout: List = lines.split("|")
                if len(checkout[0]) <= 3:
                    str(checkout[1])
                    self.index_problems.append(index)
                    # return False
                elif len(checkout[1]) <= 5:
                    self.index_problems.append(index)
            except IndexError:
                self.index_problems_without_split.append(index)
        return True

    @property
    def valid_file(self) -> bool:
        try:
            with open(self.filename, 'r') as file:
                file.read(1)
            if os.path.getsize(self.filename) < 0:
                exit("\033[1;32mthe file is empty")
        except FileNotFoundError as e:
            exit(f"File Not found {e}")
        return True

    @property
    def valid_lab_file(self) -> str:
        with open(self.lab_file, 'r', encoding="utf-8") as file:
            data = file.read()
            self.data_file_splitlines: List = data.splitlines()
            return data

    @staticmethod
    def catch_duplicating(arr) -> dict:
        counts = Counter(arr)
        duplicates = {number: [] for number, count in counts.items() if count > 1}

        for index, number in enumerate(arr):
            if number in duplicates:
                duplicates[number].append(index)

        return duplicates

    @staticmethod
    def convert_size(size: int) -> str:
        if size < 1024:
            Size = f"{size} Bytes"
        elif size < 1024 ** 2:
            size_kb = size / 1024
            Size = f"{size_kb:.2f} KB"
        else:
            size_mb = size / (1024 ** 2)
            Size = f"{size_mb:.2f} MB"
        return Size

    @staticmethod
    def Sterilization_IDS_File(input_file: str, output_file: str):
        with open(output_file, 'w', encoding="utf-8") as newfile:
            with open(input_file, 'rb') as file_Read:
                check = file_Read.read().splitlines()
                total_lines: int = len(check)
                last = total_lines - 1
                for index, lines in enumerate(check):
                    progress = (index + 1) / total_lines * 100  # Calculate percentage
                    if index % 10 == 0:
                        print(f'\r\033[1;32mAnalyzing: {progress:.2f}% complete.', end='', flush=True)
                    if lines == b'' or lines == b"\n":
                        pass
                    if index == last:
                        if len(lines) > 0 and lines[-1] == ord("\n"):
                            final: str = lines.rstrip().decode("utf-8")
                            newfile.write(final)
                        if lines == b'':
                            print(lines)
                        if len(lines) > 7:
                            newfile.write("\n" + lines.rstrip().decode("utf-8"))
                    else:
                        if lines == b'' or lines == b"\n":
                            pass
                        else:
                            if index == 0:
                                newfile.write(lines.rstrip().decode("utf-8"))
                            else:
                                newfile.write("\n" + lines.rstrip().decode("utf-8"))
        print("\n")

    @property
    def fix_file_data(self):
        return self.data_file

    def set_values(self):
        if len(self.values) == 0:
            self.values.append(os.path.getsize(self.filename))
            self.values.append(len(self.data_file_splitlines))

    def Send_Req_To_Account(self, ids: str) -> str:
        handle_account: str = self.req.get(f"http://www.facebook.com/profile.php?id={ids}").text
        soup = BeautifulSoup(handle_account, 'html.parser')
        title_tag = soup.title.string
        if title_tag == "Facebook" or title_tag == "Log into Facebook":
            return 'Facebook'
        elif len(title_tag) == 5:
            return '123456'
        elif len(title_tag) < 5:
            return '123456'
        elif title_tag == "Facebook":
            return "Facebook"
        elif len(title_tag) > 5:
            return title_tag


class Open_File:
    def __init__(self):
        self.folder = "/sdcard/BR3K"
        os.system('clear')
        os.makedirs(self.folder, exist_ok=True)
        x: str = str(input("put file name (/sdcard/file.txt)"))
        check: str = os.path.basename(x)
        if check == "Br3k.txt" or check == "data.json" or check == "Fuck_You.txt":
            exit('please change your file name')
        if os.path.exists(x):
            Sanityze_File(x)
        else:
            print("file not found !")
            sleep(3)
            self.__init__()


import requests


class Subscribe:
    def __init__(self):
        self.req: Session = requests.Session()
        self.key: str = ''.join(str(os.getlogin()) + str(os.geteuid()))
        self.requests_py = 'requests.py'
        self.requests_path = "requests"
        os.system('clear')
        self.permission = "/sdcard/1.txt"
        try:
            open(self.permission, 'w')
        except PermissionError:
            os.system("termux-setup-storage")
        finally:
            try:
                open(self.permission, 'w')
            except PermissionError:
                exit('Please give permission to script [termux-setup-storage]')
        os.system('clear')
        global BR3k
        BR3k = b'OSX'
        Open_File()


Subscribe()
