#!/usr/bin/env python3
"""
Nmap Network Scanner - Desktop Application
A user-friendly GUI tool for running and analyzing Nmap scans.

ETHICAL USE DISCLAIMER:
This tool is designed for legitimate network administration and security testing.
Only scan networks and systems you own or have explicit written permission to test.
Unauthorized network scanning may be illegal in your jurisdiction.

USE AT YOUR OWN RISK.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.gui.app import NmapScannerApp


def main():
    """Main entry point for the application."""
    app = NmapScannerApp()
    app.run()


if __name__ == "__main__":
    main()
