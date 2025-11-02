import customtkinter as ctk
from customtkinter import CTkImage
from core.scanner import NmapScanner
from PIL import Image, UnidentifiedImageError
import time
import os

# 🔹 Splash screen function
def show_splash():
    splash = ctk.CTk()
    splash.title("SCANIQ")
    splash.geometry("400x300")
    splash.resizable(False, False)

    logo_path = os.path.join(os.path.dirname(__file__), "assets", "scaniq_logo.png")
    print("Splash logo path:", logo_path)

    try:
        logo_image = Image.open(logo_path)
        logo_photo = CTkImage(light_image=logo_image, dark_image=logo_image, size=(200, 200))
    except (FileNotFoundError, UnidentifiedImageError) as e:
        splash.destroy()
        raise RuntimeError(f"❌ Splash image error: {e}")

    logo_label = ctk.CTkLabel(splash, image=logo_photo, text="")
    logo_label.image = logo_photo
    logo_label.pack(pady=10)

    slogan_label = ctk.CTkLabel(splash, text='"RECON WITH REASON"', font=("Arial", 14))
    slogan_label.pack(pady=5)

    splash.update()
    time.sleep(2)
    splash.destroy()

# 🔹 Main App Class
class NmapScannerApp:
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()
        self.app.title("Nmap Network Scanner")
        self.app.geometry("600x500")

        self.build_ui()

    def build_ui(self):
        logo_path = os.path.join(os.path.dirname(__file__), "assets", "scaniq_logo.png")
        print("Main GUI logo path:", logo_path)

        try:
            logo_image = Image.open(logo_path)
            logo_photo = CTkImage(light_image=logo_image, dark_image=logo_image, size=(200, 200))
        except (FileNotFoundError, UnidentifiedImageError) as e:
            self.app.destroy()
            raise RuntimeError(f"❌ GUI image error: {e}")

        logo_label = ctk.CTkLabel(self.app, image=logo_photo, text="")
        logo_label.image = logo_photo
        logo_label.pack(pady=10)

        slogan_label = ctk.CTkLabel(self.app, text='"RECON WITH REASON"', font=("Arial", 14))
        slogan_label.pack(pady=5)

        self.target_entry = ctk.CTkEntry(self.app, placeholder_text="Target IP or Host")
        self.target_entry.pack(pady=10)

        self.scan_type_entry = ctk.CTkEntry(self.app, placeholder_text="Scan Type (e.g. Quick Scan)")
        self.scan_type_entry.pack(pady=10)

        self.port_entry = ctk.CTkEntry(self.app, placeholder_text="Ports (e.g. 80,443)")
        self.port_entry.pack(pady=10)

        self.scan_button = ctk.CTkButton(self.app, text="Run Scan", command=self.run_scan)
        self.scan_button.pack(pady=10)

        self.output_box = ctk.CTkTextbox(self.app, width=550, height=300)
        self.output_box.pack(pady=10)

    def run_scan(self):
        target = self.target_entry.get()
        scan_type = self.scan_type_entry.get()
        ports = self.port_entry.get()

        scanner = NmapScanner()

        try:
            scan_data = scanner.perform_scan(target, scan_type, ports)
            output = scanner.format_results(scan_data)
        except Exception as e:
            output = f"❌ Error: {str(e)}"

        self.output_box.delete("1.0", "end")
        self.output_box.insert("end", output)

    def run(self):
        self.app.mainloop()

# 🔹 Launch sequence
if __name__ == "__main__":
    try:
        print("Launching splash screen...")
        show_splash()
        print("Launching main app...")
        app = NmapScannerApp()
        app.run()
    except Exception as e:
        print(f"❌ App failed to launch: {e}")
