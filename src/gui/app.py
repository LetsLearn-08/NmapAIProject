import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading
from datetime import datetime
import os
from typing import Optional
import queue
from src.core.scanner import NmapScanner


class NmapScannerApp:
    def __init__(self):
        self.scanner = NmapScanner()
        self.current_results = ""
        self.is_scanning = False
        self.result_queue = queue.Queue()
        
        self.window = ctk.CTk()
        self.window.title("Nmap Scanner - Network Analysis Tool")
        self.window.geometry("900x700")
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.setup_ui()
        self.check_queue()
        
    def setup_ui(self):
        """Setup the user interface."""
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        title_label = ctk.CTkLabel(
            main_frame,
            text="🛡️ Nmap Network Scanner",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=(0, 20))
        
        disclaimer_label = ctk.CTkLabel(
            main_frame,
            text="⚠️ Only scan networks you own or have explicit permission to scan",
            font=ctk.CTkFont(size=12),
            text_color="orange"
        )
        disclaimer_label.pack(pady=(0, 10))
        
        input_frame = ctk.CTkFrame(main_frame)
        input_frame.pack(fill="x", pady=(0, 20))
        
        ctk.CTkLabel(
            input_frame,
            text="Target IP/Domain:",
            font=ctk.CTkFont(size=14, weight="bold")
        ).grid(row=0, column=0, sticky="w", padx=10, pady=10)
        
        self.target_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="e.g., 192.168.1.1 or example.com",
            width=300
        )
        self.target_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        ctk.CTkLabel(
            input_frame,
            text="Scan Type:",
            font=ctk.CTkFont(size=14, weight="bold")
        ).grid(row=1, column=0, sticky="w", padx=10, pady=10)
        
        self.scan_type_var = ctk.StringVar(value="Quick Scan")
        scan_type_menu = ctk.CTkOptionMenu(
            input_frame,
            variable=self.scan_type_var,
            values=["Quick Scan", "Full Scan", "Custom Port Scan"],
            command=self.on_scan_type_change,
            width=300
        )
        scan_type_menu.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        
        ctk.CTkLabel(
            input_frame,
            text="Port Range:",
            font=ctk.CTkFont(size=14, weight="bold")
        ).grid(row=2, column=0, sticky="w", padx=10, pady=10)
        
        self.port_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="e.g., 22-80 or 22,80,443",
            width=300,
            state="disabled"
        )
        self.port_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        
        input_frame.columnconfigure(1, weight=1)
        
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.pack(fill="x", pady=(0, 20))
        
        self.scan_button = ctk.CTkButton(
            button_frame,
            text="🔍 Start Scan",
            command=self.start_scan,
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40,
            fg_color="green",
            hover_color="dark green"
        )
        self.scan_button.pack(side="left", padx=10, expand=True, fill="x")
        
        self.export_button = ctk.CTkButton(
            button_frame,
            text="💾 Export Results",
            command=self.export_results,
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40,
            state="disabled"
        )
        self.export_button.pack(side="left", padx=10, expand=True, fill="x")
        
        self.clear_button = ctk.CTkButton(
            button_frame,
            text="🗑️ Clear",
            command=self.clear_results,
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40,
            fg_color="gray",
            hover_color="dark gray"
        )
        self.clear_button.pack(side="left", padx=10, expand=True, fill="x")
        
        results_label = ctk.CTkLabel(
            main_frame,
            text="Scan Results:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        results_label.pack(anchor="w", pady=(0, 5))
        
        self.results_text = ctk.CTkTextbox(
            main_frame,
            font=ctk.CTkFont(family="Courier", size=11),
            wrap="none"
        )
        self.results_text.pack(fill="both", expand=True)
        
        status_frame = ctk.CTkFrame(main_frame)
        status_frame.pack(fill="x", pady=(10, 0))
        
        self.status_label = ctk.CTkLabel(
            status_frame,
            text="Ready to scan",
            font=ctk.CTkFont(size=12)
        )
        self.status_label.pack(side="left", padx=10)
        
        self.progress_bar = ctk.CTkProgressBar(status_frame)
        self.progress_bar.pack(side="right", padx=10, fill="x", expand=True)
        self.progress_bar.set(0)
    
    def on_scan_type_change(self, choice):
        """Enable/disable port entry based on scan type."""
        if choice == "Custom Port Scan":
            self.port_entry.configure(state="normal")
        else:
            self.port_entry.configure(state="disabled")
    
    def update_status(self, message: str, progress: float = 0):
        """Update status label and progress bar."""
        self.status_label.configure(text=message)
        self.progress_bar.set(progress)
    
    def start_scan(self):
        """Start the Nmap scan in a separate thread."""
        if self.is_scanning:
            messagebox.showwarning("Scan in Progress", "A scan is already running. Please wait.")
            return
        
        target = self.target_entry.get().strip()
        if not target:
            messagebox.showerror("Invalid Input", "Please enter a target IP address or domain.")
            return
        
        scan_type = self.scan_type_var.get()
        ports = None
        
        if scan_type == "Custom Port Scan":
            ports = self.port_entry.get().strip()
            if not ports:
                messagebox.showerror("Invalid Input", "Please enter a port range for Custom Port Scan.")
                return
        
        self.is_scanning = True
        self.scan_button.configure(state="disabled", text="⏳ Scanning...")
        self.export_button.configure(state="disabled")
        self.update_status("Starting scan...", 0.2)
        
        scan_thread = threading.Thread(
            target=self.perform_scan,
            args=(target, scan_type, ports),
            daemon=True
        )
        scan_thread.start()
    
    def check_queue(self):
        """Check the queue for updates from the scan thread (runs in main thread)."""
        try:
            while True:
                message = self.result_queue.get_nowait()
                
                if message['type'] == 'status':
                    self.update_status(message['text'], message['progress'])
                    
                elif message['type'] == 'results':
                    self.current_results = message['data']
                    self.results_text.delete("1.0", "end")
                    self.results_text.insert("1.0", message['data'])
                    self.export_button.configure(state="normal")
                    
                elif message['type'] == 'error':
                    messagebox.showerror(message['title'], message['text'])
                    
                elif message['type'] == 'complete':
                    self.is_scanning = False
                    self.scan_button.configure(state="normal", text="🔍 Start Scan")
                    
        except queue.Empty:
            pass
        
        self.window.after(100, self.check_queue)
    
    def perform_scan(self, target: str, scan_type: str, ports: Optional[str] = None):
        """Perform the actual scan (runs in separate thread)."""
        try:
            self.result_queue.put({'type': 'status', 'text': 'Scanning in progress...', 'progress': 0.5})
            
            scan_results = self.scanner.perform_scan(target, scan_type, ports)
            
            self.result_queue.put({'type': 'status', 'text': 'Formatting results...', 'progress': 0.8})
            
            formatted_results = self.scanner.format_results(scan_results)
            
            self.result_queue.put({'type': 'results', 'data': formatted_results})
            self.result_queue.put({'type': 'status', 'text': 'Scan completed successfully', 'progress': 1.0})
            
        except ValueError as e:
            self.result_queue.put({'type': 'error', 'title': 'Validation Error', 'text': str(e)})
            self.result_queue.put({'type': 'status', 'text': 'Scan failed - validation error', 'progress': 0})
        except RuntimeError as e:
            self.result_queue.put({'type': 'error', 'title': 'Scan Error', 'text': str(e)})
            self.result_queue.put({'type': 'status', 'text': 'Scan failed - runtime error', 'progress': 0})
        except Exception as e:
            self.result_queue.put({'type': 'error', 'title': 'Unexpected Error', 'text': f"An unexpected error occurred:\n{str(e)}"})
            self.result_queue.put({'type': 'status', 'text': 'Scan failed - unexpected error', 'progress': 0})
        finally:
            self.result_queue.put({'type': 'complete'})
    
    def export_results(self):
        """Export scan results to a text file."""
        if not self.current_results:
            messagebox.showwarning("No Results", "No scan results to export.")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        default_filename = f"nmap_scan_{timestamp}.txt"
        
        os.makedirs("exports", exist_ok=True)
        
        filepath = filedialog.asksaveasfilename(
            initialdir="exports",
            initialfile=default_filename,
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        
        if filepath:
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(self.current_results)
                    f.write(f"\n\nExported on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                
                messagebox.showinfo("Export Successful", f"Results saved to:\n{filepath}")
                self.update_status(f"Results exported to {os.path.basename(filepath)}", 1.0)
            except Exception as e:
                messagebox.showerror("Export Failed", f"Failed to save file:\n{str(e)}")
    
    def clear_results(self):
        """Clear the results text box."""
        self.results_text.delete("1.0", "end")
        self.current_results = ""
        self.export_button.configure(state="disabled")
        self.update_status("Ready to scan", 0)
    
    def run(self):
        """Start the application main loop."""
        nmap_installed = self.scanner.check_nmap_installed()
        if not nmap_installed:
            messagebox.showwarning(
                "Nmap Not Found",
                "Nmap is not installed or not found in PATH.\n\n"
                "Please install Nmap from https://nmap.org/download.html\n\n"
                "The application will start but scans will fail until Nmap is installed."
            )
        
        self.window.mainloop()
