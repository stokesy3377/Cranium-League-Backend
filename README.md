🧠 Cranium League Backend
A Python-based backend system for Cranium League, a private fantasy betting game played among friends using IPL match data.

📄 Files Overview
rawtext.txt
Daily input file. Bets must be copied directly from WhatsApp Web and pasted here before processing.

edit-text.py
Cleans rawtext.txt by stripping participant prefixes and isolating bet data.

CL_data_mod.py
Parses cleaned data, assigns scores based on the winning team, and generates a score list for each player.

3_Import_To_Excel.py
Maps scores to the appropriate match number cell in CL_S1.xlsx.

4_excel_datacross.py
Maintains rolling balances by shifting and resetting Excel columns using evaluated values.

5_excel-backup.py
Creates date-stamped backups of CL_S1.xlsx in the /backup directory for data integrity.
