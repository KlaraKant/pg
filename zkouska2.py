# Příklad 2: Práce s externími knihovnami a soubory
# Zadání:
# Napište funkci `fetch_and_save_data`, která:
# 1. Načte data z URL (https://jsonplaceholder.typicode.com/posts).
# 2. Do staženého json souboru přidá klíč `userName` s hodnotou jména uživatele podle klíče `userId` z URL (např. 1 -> "Leanne Graham").
# 3. Data uloží do souboru `data.json` ve formátu JSON.
# Použijte knihovny `requests` a `json`.

import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
user_names = {
    1: "Leanne Graham",
    2: "Ervin Howell",
    3: "Clementine Bauch",
    4: "Patricia Lebsack",
    5: "Chelsey Dietrich",
    6: "Mrs. Dennis Schulist",
    7: "Kurtis Weissnat",
    8: "Nicholas Runolfsdottir V",
    9: "Glenna Reichert",
    10: "Clementina DuBuque"
}

def fetch_and_save_data():
    response = requests.get(url) #načte data z URL, výsledek uložen do response 
    if not response.ok: #zkouška odpovědi
        return False #pokud je odpověď špatná, vrátí False
    
    data = response.json() #načte data ve formátu JSON
    
    for uživatel in data: #prochází všechna data, každý prvek seznamu je uložen do proměnné uživatel
        user_id = uživatel.get("userId") #získává hodnotu userID
        uživatel["userName"] = user_names.get(user_id)  #přidá klíč username ze seznamu
    
    with open("data.json", "w") as file:  #uloží data do souboru `data.json`
        file.write(json.dumps(data, indent=4))  #uložíme data do souboru ve formátu JSON
    
    return True  #úspěšné zpracování
  
# Pytest testy pro Příklad 2
from unittest.mock import patch, MagicMock, mock_open

def test_fetch_and_save_data():
    mock_data = [
        {"userId": 1, "id": 1, "title": "Test post", "body": "This is a test."}
    ]
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, json=MagicMock(return_value=mock_data), text=json.dumps(mock_data), content=json.dumps(mock_data))

        with patch("builtins.open", mock_open()) as mock_file:
            assert fetch_and_save_data() == True
            mock_file().write.call_args[0][0] == json.dumps([
                {
                    "userId": 1,
                    "id": 1,
                    "title": "Test post",
                    "body": "This is a test.",
                    "userName": "Leanne Graham"
                }
            ])