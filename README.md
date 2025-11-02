# 🛡️ SCANIQ: Nmap Network Scanner GUI

**"RECON WITH REASON"**  
A modern, beginner-friendly desktop app for running and analyzing Nmap scans with a graphical interface. Built with Python and CustomTkinter, SCANIQ wraps powerful recon tools in a clean GUI to make ethical scanning accessible to all.

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)
![License](https://img.shields.io/badge/license-CC%20BY--NC--ND%204.0-red.svg)

---

## 🎯 Purpose

SCANIQ was created to:
- Help beginners understand network scanning
- Make Nmap easier to run and interpret
- Promote ethical cybersecurity practices
- Showcase the evolution from CLI to GUI

---

## ⚠️ Ethical Use Disclaimer

**IMPORTANT:** This tool is for legitimate network administration, security testing, and education only.

- ✅ Use only on systems you own or have permission to scan  
- ❌ Never use for unauthorized or malicious purposes

Unauthorized scanning may be illegal. Use responsibly.

---

## 🖥️ Download

You can now run SCANIQ without installing Python!

👉 [Download SCANIQ for Windows (.exe)](https://github.com/LetsLearn-08/NmapAIProject/releases)

Includes:
- Splash screen and logo
- GUI input for target, scan type, and ports
- Real-time output in a scrollable textbox
- Beginner-friendly setup — just download and run

---

## 📸 Preview

Screenshots coming soon:
- Splash screen with logo  
- GUI input fields  
- Real-time scan output

---

## 🔄 CLI to GUI Evolution

| Feature | CLI Version | SCANIQ GUI |
|--------|-------------|------------|
| Interface | Terminal | Graphical |
| Input | Manual typing | GUI fields |
| Output | Raw text | Formatted textbox |
| Branding | None | Logo + slogan |
| Accessibility | Low | High |
| Code Structure | Single script | Modular folders |
| Educational Value | Basic scripting | Guided interaction |

🔗 [View original CLI project](https://github.com/LetsLearn-08/Roadmap---Penetration-Testing/blob/main/nmap-scans/README.md)

---

## 📁 Project Structure

```
nmap-scanner-app/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── .gitignore             # Git ignore rules
├── src/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── scanner.py     # Nmap scanning logic
│   └── gui/
│       ├── __init__.py
│       └── app.py         # GUI implementation
└── exports/               # Saved scan results 
```


## 📁 Folder Structure


| Path | Purpose |
|------|---------|
| [`scanner_app.py`](scanner_app.py) | Main launcher for the GUI. Handles splash screen, input fields, and scan output. |
| [`core/scanner.py`](core/scanner.py) | Contains the scan logic using `python-nmap`. Modular and easy to extend. |
| [`assets/scaniq_logo.png`](assets/scaniq_logo.png) | Logo used in splash screen and GUI. Adds professional branding. |
| [`requirements.txt`](requirements.txt) | List of Python packages required to run the app. |
| [`LICENSE`](LICENSE) | MIT license for open-source sharing. |
| [`.gitignore`](.gitignore) | Keeps the repo clean by ignoring temporary files. |


---

## 🧠 How It Works

- **Splash Screen:** Shows logo and slogan  
- **GUI Input:** Target, scan type, ports  
- **Scan Execution:** Runs Nmap with selected options  
- **Output Box:** Displays formatted results in real time

---

## 📦 Requirements

Listed in `requirements.txt`:

| Package | Purpose |
|----------|----------|
| **customtkinter** | GUI framework with modern styling and HDPI support |
| **pillow** | Image handling for logos and splash screens |
| **python-nmap** | Python wrapper for Nmap, used to run and parse scans |

---


## 🛠️ Setup Instructions

> 💡 **Tip for Beginners:**  
> Make sure Python is installed on your system.  
> You can download it from [python.org](https://www.python.org/downloads/).  
> Run commands in a terminal or command prompt inside the project folder.


### 1. Clone the repo
```bash
git clone https://github.com/LetsLearn-08/NmapAIProject.git
cd WmapAIProject
```
## ⚙️ Installation Steps

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the App
```
python scanner_app.py
```

---


## 📦 Build Standalone Executable 

- To create a .exe:
```
pip install pyinstaller
pyinstaller --onefile --windowed --name "SCANIQ" scanner_app.py
Output will be in the dist/ folder.
```

## 🐛 Troubleshooting

- Nmap not found: Add it to system PATH
- App won’t start: Check Python version and dependencies
- Scan fails: Verify target and network permissions
- GUI missing: Ensure display environment is available


## 🤝 Contributing

Pull requests are welcome!  
If you’d like to suggest features, improve documentation, or help with packaging, please **open an issue** first to discuss your ideas.

- 📬 [View CONTRIBUTING.md](CONTRIBUTING.md)

📄 License

Licensed under  [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) license.

Use for ethical and educational purposes only. Reposting, redistribution, or modification is not allowed.

🙌 Acknowledgments

- **Nmap** — the engine behind the scans  
- **CustomTkinter** — for the beautiful GUI  
- **Everyone learning cybersecurity** — this tool is for you ❤️  


## 📣 About Me

I’m passionate about **ethical hacking**, **automation**, and **making cybersecurity tools beginner-friendly**.  
**SCANIQ** is part of my journey to build tools that are useful, transparent, and easy to share.

Follow my progress and connect on **[LinkedIn](https://www.linkedin.com/in/tanuja-reddy-03aa7b38a)**
)**.


