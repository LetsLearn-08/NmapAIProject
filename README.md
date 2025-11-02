<<<<<<< HEAD
# 🛡️ Nmap Network Scanner

A modern, user-friendly desktop application for running and analyzing Nmap network scans with a graphical interface.

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

## ⚠️ Ethical Use Disclaimer

**IMPORTANT:** This tool is designed for legitimate network administration, security testing, and educational purposes only.

- ✅ **DO** use this tool on networks and systems you own
- ✅ **DO** obtain explicit written permission before scanning any network
- ❌ **DO NOT** scan networks or systems without authorization
- ❌ **DO NOT** use this tool for malicious purposes

**Unauthorized network scanning may be illegal in your jurisdiction. Use at your own risk.**

## 🤖 AI Usage Disclosure

This project was developed with assistance from AI tools. The code has been reviewed and tested, but users should verify functionality for their specific use cases.

## ✨ Features

- **Modern GUI** - Clean, dark-themed interface built with CustomTkinter
- **Multiple Scan Types**
  - Quick Scan (100 most common ports)
  - Full Scan (all 65535 ports)
  - Custom Port Scan (specify your own port ranges)
- **Real-time Results** - View formatted scan results as they complete
- **Export Functionality** - Save scan results to timestamped .txt files
- **Error Handling** - Comprehensive validation and error messages
- **Cross-Platform** - Works on Windows, Linux, and macOS

## 📋 Prerequisites

### System Requirements

- **Python 3.11 or higher**
- **Nmap** - Must be installed separately

### Installing Nmap

#### Windows
1. Download the installer from [nmap.org/download.html](https://nmap.org/download.html)
2. Run the installer and follow the prompts
3. Ensure Nmap is added to your system PATH

#### Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install nmap
```

#### Linux (Fedora/RHEL)
```bash
sudo dnf install nmap
```

#### macOS
```bash
brew install nmap
```

## 🚀 Installation

### Option 1: Clone from GitHub

```bash
# Clone the repository
git clone https://github.com/yourusername/nmap-scanner-app.git
cd nmap-scanner-app

# Install Python dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Option 2: Using uv (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/nmap-scanner-app.git
cd nmap-scanner-app

# Install dependencies with uv
uv pip install -r requirements.txt

# Run the application
python main.py
```

## 📖 Usage Guide

### Basic Workflow

1. **Launch the Application**
   ```bash
   python main.py
   ```

2. **Enter Target**
   - Input an IP address (e.g., `192.168.1.1`)
   - Or a domain name (e.g., `example.com`)

3. **Select Scan Type**
   - **Quick Scan**: Fast scan of 100 most common ports
   - **Full Scan**: Comprehensive scan of all 65,535 ports (slower)
   - **Custom Port Scan**: Specify your own port range

4. **Configure Ports** (Custom Scan Only)
   - Single port: `80`
   - Port range: `22-80`
   - Multiple ports: `22,80,443,8080`

5. **Start Scan**
   - Click "🔍 Start Scan"
   - Wait for the scan to complete
   - Results will appear in the text box

6. **Export Results**
   - Click "💾 Export Results"
   - Choose a location to save the .txt file
   - Results are saved with a timestamp

### Example Scans

#### Quick Scan
```
Target: 192.168.1.1
Scan Type: Quick Scan
Port Range: (default)
```

#### Custom Port Scan
```
Target: example.com
Scan Type: Custom Port Scan
Port Range: 22,80,443,8080
```

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
└── exports/               # Saved scan results (created automatically)
```

## 🔧 Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/nmap-scanner-app.git
cd nmap-scanner-app

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Code Structure

- **`src/core/scanner.py`** - Core scanning logic using python-nmap
  - `NmapScanner` class handles all Nmap operations
  - Input validation and error handling
  - Result parsing and formatting

- **`src/gui/app.py`** - GUI implementation using CustomTkinter
  - `NmapScannerApp` class manages the UI
  - Threading for non-blocking scans
  - File export functionality

## 📦 Building Standalone Executable (Optional)

To create a standalone `.exe` file for Windows:

```bash
# Install PyInstaller
pip install pyinstaller

# Build the executable
pyinstaller --onefile --windowed --name "NmapScanner" main.py

# The .exe will be in the dist/ folder
```

**Note:** You'll need to distribute Nmap separately or include it in your installation package.

## 🐛 Troubleshooting

### "Nmap is not installed" Error
- Ensure Nmap is installed and available in your system PATH
- Try running `nmap --version` in your terminal
- On Windows, you may need to restart your terminal after installation

### Application Won't Start
- Verify Python 3.11+ is installed: `python --version`
- Install dependencies: `pip install -r requirements.txt`
- Check for error messages in the terminal

### Scans Fail or Time Out
- Ensure you have permission to scan the target
- Check your network connection
- Try a Quick Scan first before attempting a Full Scan
- Firewall or antivirus may be blocking Nmap

### GUI Doesn't Appear
- Make sure you have a display environment (not running headless)
- On Linux, ensure you have required GUI libraries
- Try running with `python main.py` directly

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Acknowledgments

- [Nmap](https://nmap.org/) - The Network Mapper
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Modern UI library
- [python-nmap](https://pypi.org/project/python-nmap/) - Python wrapper for Nmap

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Search existing [Issues](https://github.com/yourusername/nmap-scanner-app/issues)
3. Open a new issue with detailed information

## 🔒 Security Note

This application runs Nmap commands on your system. Always review the code before running, especially if downloading from untrusted sources. Never scan systems without proper authorization.

---

**Remember: With great power comes great responsibility. Use this tool ethically and legally!** 🛡️
=======
## NmapAIProject
A GUI-based Nmap scanner with splash screen, real-time output, and clean UX — built for ethical recon.

# SCANIQ: Nmap Network Scanner GUI

**"RECON WITH REASON"**

Welcome to SCANIQ — a beginner-friendly desktop app that makes network scanning simple, visual, and accessible. Built with Python and CustomTkinter, SCANIQ wraps powerful Nmap functionality in a clean GUI so anyone can explore ethical reconnaissance with confidence.

---

## 🎯 Purpose

This project was created to:
- Help beginners understand how network scanning works
- Make Nmap scans easier to run and interpret
- Promote ethical cybersecurity practices
- Share my personal journey from CLI tools to GUI-based automation

Whether you're a student, hobbyist, or aspiring ethical hacker — SCANIQ is designed to guide you step-by-step.

---


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
## 📸 Preview

Screenshots coming soon!  
This section will include:
- Splash screen with SCANIQ logo
- GUI interface with input fields and scan output
- Example scan results from a test target

Once added, they’ll help beginners visualize how the app works before running it.

![Splash Screen](screenshots/splash_screen.png)
![GUI Input](screenshots/gui_input.png)
![Scan Output](screenshots/scan_output.png)


---

## 🔄 Evolution from CLI to GUI

Before SCANIQ, I built a command-line based Nmap analyzer as my first hands-on cybersecurity project. It helped me understand:

- How Nmap works under the hood
- How to parse and format scan results
- How to modularize Python scripts for reuse.

That CLI tool was functional but not beginner-friendly — it required terminal commands, manual input, and had no visual interface.

 | Feature / Aspect         | Previous Project: Nmap Analyzer (CLI) | Current Project: SCANIQ (GUI) |
|--------------------------|----------------------------------------|-------------------------------|
| **Interface**            | Command-line only                      | Graphical user interface (GUI) with input fields and buttons |
| **User Experience**      | Manual typing, no visual feedback      | Beginner-friendly, interactive, and visual |
| **Scan Input**           | Hardcoded or typed manually            | Entered via GUI fields (target, scan type, ports) |
| **Output Format**        | Raw terminal output                    | Formatted, scrollable textbox with clean layout |
| **Branding**             | None                                   | Splash screen, logo, and slogan: “RECON WITH REASON” |
| **Error Handling**       | Minimal                                | GUI alerts and safe image loading |
| **Code Structure**       | Single script                          | Modular: `scanner_app.py`, `core/scanner.py`, `assets/` |
| **Beginner Accessibility** | Low — required terminal knowledge     | High — no coding or CLI experience needed |
| **Educational Value**    | Focused on Nmap basics                 | Teaches scanning concepts through guided interaction |
| **Purpose**              | Learn Nmap scripting and parsing       | Make ethical scanning accessible and visual for everyone |


**SCANIQ is the next step.** It transforms that raw functionality into a polished desktop app with:

- A splash screen and logo for professional branding
- GUI inputs for target, scan type, and ports
- Real-time output in a scrollable textbox
- Error handling and modular design for future upgrades

By keeping both projects public, I want to show how cybersecurity tools can evolve — and how anyone can start simple and build something powerful.

🔗 [View my original Nmap Analyzer project](https://github.com/LetsLearn-08/Roadmap---Penetration-Testing/blob/main/nmap-scans/README.md)


## 🛠️ Setup Instructions

> 💡 **Tip for Beginners:**  
> Make sure Python is installed on your system.  
> You can download it from [python.org](https://www.python.org/downloads/).  
> Run commands in a terminal or command prompt inside the project folder.


### 1. Clone the repo
```bash
git clone https://github.com/yourusername/WmapAIProject.git
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

## 📦 Requirements

Listed in `requirements.txt`:

| Package | Purpose |
|----------|----------|
| **customtkinter** | GUI framework with modern styling and HDPI support |
| **pillow** | Image handling for logos and splash screens |
| **python-nmap** | Python wrapper for Nmap, used to run and parse scans |

---

## 🖥️ Download

👉 [Download SCANIQ for Windows (.exe)](https://github.com/LetsLearn-08/NmapAIProject/releases)


## 🧠 How It Works

- **Splash Screen:** Displays logo and slogan for 2 seconds  
- **GUI Interface:** Lets you enter:  
  - Target IP or Host  
  - Scan Type (e.g., *Quick Scan*)  
  - Ports (e.g., *80,443*)  
- **Run Scan:** Executes Nmap with selected options  
- **Output Box:** Shows formatted results in real time  

---

## 🧑‍💻 For Beginners

If you're new to cybersecurity:

- **Nmap** is a tool used to discover devices and services on a network  
- **Scan Types** like “Quick Scan” or “Aggressive Scan” control how deep the scan goes  
- **Ports** are gateways into a system — scanning them reveals what services are running  

**SCANIQ** helps you learn these concepts interactively, without needing to memorize terminal commands.

## 📄 License

This project is licensed under the [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) license.

You may use this project for educational and ethical purposes only.  
Reposting, redistribution, or modification is **not allowed**.

---

## 🤝 Contributing

Pull requests are welcome!  
If you’d like to suggest features, improve documentation, or help with packaging, please **open an issue** first to discuss your ideas.

- 📬 [View CONTRIBUTING.md](CONTRIBUTING.md)



You’ve built something powerful — now you’re documenting it like a pro.

---

## 🙌 Acknowledgments

- **Nmap** — the engine behind the scans  
- **CustomTkinter** — for the beautiful GUI  
- **Everyone learning cybersecurity** — this tool is for you ❤️  

---

## 📣 About Me

I’m passionate about **ethical hacking**, **automation**, and **making cybersecurity tools beginner-friendly**.  
**SCANIQ** is part of my journey to build tools that are useful, transparent, and easy to share.

Follow my progress and connect on **[LinkedIn](linkedin.com/in/tanuja-reddy-03aa7b38a)**.


>>>>>>> d7a065adbdb12e0330a6a409a9027da0add94bc2
