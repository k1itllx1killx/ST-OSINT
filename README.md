# ST-OSINT

ST-OSINT

ST-OSINT is a professional OSINT tool designed to search for a username across 150+ popular social networks. It allows security researchers, penetration testers, and developers to quickly verify username availability and gather public presence data.

⸻

Features
	•	Search a username across 150+ social media platforms
	•	Real-time results with timestamped output
	•	Lightweight, fast, and easy to use
	•	Built-in update tool for automatic updates
	•	Designed for educational and security testing purposes

⸻

Requirements
	•	Python 3.x
	•	Requests library (pip install requests)
	•	Optional: Lolcat for colored terminal output

  # installation 

  # Clone the repository
git clone https://github.com/k1itllx1killx/ST-OSINT.git
cd ST-OSINT

# Run setup to install dependencies
python3 setup.py

The setup script will automatically install required Python libraries and optional tools.

# Usage

python3 st-osint.py

-------------------

1.	Select an option from the menu:
	•	1: OSINT Username Search
	•	2: Update Tool
	•	3: Exit
	2.	Enter the username to search.
	3.	View results in real-time, for example:

 [21:52:41] [INFO] https://www.facebook.com/exampleuser
[21:52:42] [INFO] https://www.twitter.com/exampleuser
[21:52:42] [INFO] USER NOT FOUND at https://www.instagram.com/exampleuser
-------------------

4.	Use the Update Tool to fetch the latest repository changes:

python3 ST-OSINT.py
# Then select option 2


Notes
	•	This tool does not access private information; it only checks if a username exists on public platforms.
	•	Use responsibly and legally.
	•	Output can be colorized with lolcat for better readability, but it is optional.

⸻

Advanced Use
	•	Combine with other OSINT or security tools for deeper analysis.
	•	Can be extended to support batch username searches.
	•	Optimized for fast internet connections to reduce query time.

⸻

Credits

Developed by .
Special thanks to contributors who tested and improved tool stability and performance.
