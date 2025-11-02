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


