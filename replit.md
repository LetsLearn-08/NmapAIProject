# Nmap Network Scanner - Project Documentation

## Overview
A Python desktop application that provides a graphical interface for running and analyzing Nmap network scans. Built with CustomTkinter for a modern UI and python-nmap for reliable scanning capabilities.

**Status**: Production Ready  
**Last Updated**: October 31, 2025

## Purpose
- Enable users to perform network scans through an intuitive GUI
- Provide formatted, readable scan results
- Support multiple scan types (Quick, Full, Custom Port)
- Export scan results for documentation and analysis

## Recent Changes

### October 31, 2025 - Initial Development & Thread Safety Fixes
- Created complete project structure with clean separation of concerns
- Implemented core scanning logic in `src/core/scanner.py`
- Built GUI application with CustomTkinter in `src/gui/app.py`
- Added export functionality for saving scan results
- Created comprehensive README with ethical use disclaimers
- Set up VNC workflow for desktop application display
- **Thread Safety Fix**: Implemented queue-based communication between scan thread and main UI thread
- Enhanced port validation to ensure proper range ordering (start <= end)

## Project Architecture

### Directory Structure
```
├── main.py                 # Entry point
├── src/
│   ├── core/
│   │   └── scanner.py     # Nmap scanning logic
│   └── gui/
│       └── app.py         # GUI implementation
└── exports/               # Saved scan results
```

### Key Components

1. **Scanner Module** (`src/core/scanner.py`)
   - `NmapScanner` class for all scanning operations
   - Input validation for targets and ports
   - Error handling for missing Nmap installation
   - Result formatting and parsing

2. **GUI Module** (`src/gui/app.py`)
   - `NmapScannerApp` class for UI management
   - CustomTkinter for modern, dark-themed interface
   - Threading for non-blocking scans
   - Export functionality with file dialogs

3. **Main Entry Point** (`main.py`)
   - Application launcher with ethical use disclaimer
   - Path setup for module imports

## Dependencies

### Python Packages
- `customtkinter` - Modern GUI framework
- `python-nmap` - Nmap wrapper for Python
- `tkinter` - Built-in for file dialogs

### External Requirements
- Nmap (must be installed on system)

## User Preferences
None specified yet - project just created

## Technical Decisions

### Why CustomTkinter?
- Modern, professional appearance
- Dark mode support out of the box
- Better widget styling than standard Tkinter
- Cross-platform compatibility

### Why VNC Output Type?
- Desktop GUI application requires graphical display
- VNC provides virtual desktop environment in Replit
- Allows users to interact with the application

### Threading for Scans
- Nmap scans can take significant time
- Threading prevents UI freezing
- Progress bar and status updates provide feedback

## Ethical Considerations

This project includes multiple layers of ethical use warnings:
1. Disclaimer in main.py docstring
2. Warning label in the GUI
3. Comprehensive ethical use section in README
4. AI usage disclosure for transparency

## Future Enhancements (Potential)
- Scan history and previous results viewer
- Save/load scan profiles
- Visual network topology maps
- PyInstaller packaging for Windows .exe
- Port service vulnerability highlighting
- Scan scheduling
- Multi-target scanning
