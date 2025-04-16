# 🧠 Cranium League Backend

A Python-based backend engine for **Cranium League** — a private IPL fantasy betting game. This system automates score calculation, balance tracking, and Excel data management using bet data copied directly from WhatsApp Web.

---

## 📁 Directory Structure

| File                  | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `rawtext.txt`         | 🔹 **Input file** — Paste raw WhatsApp Web bet data here before processing. |
| `edit-text.py`        | Cleans raw data by removing names and isolating bet amounts + team names.   |
| `CL_data_mod.py`      | Parses bets, assigns scores based on the winning team, and generates output.|
| `3_Import_To_Excel.py`| Maps scores to match-specific cells in `CL_S1.xlsx`.                        |
| `4_excel_datacross.py`| Shifts previous balances and resets interim data after each match.          |
| `5_excel-backup.py`   | Creates timestamped backups of the Excel file in `/backup/`.                |

---

> ⚠️ **IMPORTANT NOTE**  
> 🔒 **Do NOT keep `CL_S1.xlsx` open while running any of the scripts.**  
> Closing the Excel file is mandatory to prevent write errors and ensure data integrity. Always run scripts with Excel CLOSED.

---

## ✅ Usage Workflow (Admin Routine)

1. **Paste bets** from WhatsApp Web into `rawtext.txt`.
2. Run `edit-text.py`  
   → Cleans bet lines, removes names.
3. Run `CL_data_mod.py`  
   → Terminal asks: `Which team won today?` → Admin inputs winning team.  
   → Scores are generated.
4. Run `3_Import_To_Excel.py`  
   → Terminal asks: `Enter the Match Number (prefix 'M')`  
   → Terminal again asks: `Which team won today?` (repeat input)
   → Scores are written to the Excel sheet.

5. Now, **open `CL_S1.xlsx`** and follow these steps manually:
   - **Sort the `Name` column A→Z**
     > In the *Sort Warning* dialog: ✅ Select **"Expand the selection"**
   - Copy the bet data from the **match table** (based on match number)
     → Paste into the **"Bets" section** of the main leaderboard table.
   - **Sort the `Current Bal` column A→Z**
     > In the *Sort Warning* dialog: ✅ Select **"Expand the selection"**
   - **Sort the `Rank` column 1→9**
     > In the *Sort Warning* dialog: ✅ Select **"Continue with current selection"**
   - Take a **screenshot** of the updated table.
   - **Send** the screenshot to the **Main Group**.
   - **Close the Excel sheet** completely.

6. Run `4_excel_datacross.py`  
   → Resets interim values, updates rolling balances.
7. Run `5_excel-backup.py`  
   → Creates a timestamped backup in the `/backup` folder.

---

## ⚙️ Key Features

- 🧾 WhatsApp Web-compatible input handling  
- 📊 Excel integration for leaderboard and balance tracking  
- ♻️ Automated data resets and rollovers  
- 💾 Safe backup system with timestamped versioning  
- 🔧 Modular and extendable for new rule logic

---

## 📌 Notes

- Ensure `CL_S1.xlsx` and `/backup/` folder exist.
- Match number input format must follow `"M##"` (e.g., `M23`).
- `CL_data_mod.py` and `3_Import_To_Excel.py` both ask for the **winning team** — input accurately.

---

## 🔒 Private Use Only

This backend is designed for **internal use** within Cranium League and not intended for public deployment without customization.

