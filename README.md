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
