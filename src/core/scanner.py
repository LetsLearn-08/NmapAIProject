import nmap
import subprocess
import platform
from typing import Dict, Optional


class NmapScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()
        self.last_scan_results = None
        
    def check_nmap_installed(self) -> bool:
        """Check if Nmap is installed on the system."""
        try:
            if platform.system() == "Windows":
                result = subprocess.run(
                    ["nmap", "--version"],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
            else:
                result = subprocess.run(
                    ["which", "nmap"],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False
    
    def validate_target(self, target: str) -> bool:
        """Basic validation for target IP/domain."""
        if not target or target.strip() == "":
            return False
        return True
    
    def validate_ports(self, ports: str) -> bool:
        """Validate port range format and ensure proper ordering."""
        if not ports or ports.strip() == "":
            return True
        
        try:
            if '-' in ports:
                start, end = ports.split('-')
                start_port = int(start)
                end_port = int(end)
                return (1 <= start_port <= 65535 and 
                       1 <= end_port <= 65535 and 
                       start_port <= end_port)
            elif ',' in ports:
                port_list = [int(p.strip()) for p in ports.split(',')]
                return all(1 <= p <= 65535 for p in port_list)
            else:
                port = int(ports)
                return 1 <= port <= 65535
        except (ValueError, AttributeError):
            return False
    
    def perform_scan(
        self,
        target: str,
        scan_type: str = "Quick Scan",
        ports: Optional[str] = None
    ) -> Dict:
        """
        Perform Nmap scan with specified parameters.
        
        Args:
            target: IP address or domain name
            scan_type: Type of scan (Quick Scan, Full Scan, Custom Port Scan)
            ports: Port range for custom scans (e.g., "22-80" or "22,80,443")
        
        Returns:
            Dictionary containing scan results and metadata
        """
        if not self.validate_target(target):
            raise ValueError("Invalid target. Please provide a valid IP address or domain name.")
        
        if not self.check_nmap_installed():
            raise RuntimeError(
                "Nmap is not installed or not found in PATH.\n"
                "Please install Nmap from https://nmap.org/download.html"
            )
        
        arguments = ""
        port_range = ""
        
        if scan_type == "Quick Scan":
            arguments = "-T4 -F"
            port_range = "100 most common ports"
        elif scan_type == "Full Scan":
            arguments = "-T4 -p-"
            port_range = "all 65535 ports"
        elif scan_type == "Custom Port Scan":
            if not ports:
                raise ValueError("Port range required for Custom Port Scan")
            if not self.validate_ports(ports):
                raise ValueError("Invalid port format. Use formats like: 80, 22-80, or 22,80,443")
            arguments = f"-T4 -p {ports}"
            port_range = f"ports {ports}"
        else:
            arguments = "-T4 -F"
            port_range = "100 most common ports"
        
        try:
            self.nm.scan(target, arguments=arguments)
            self.last_scan_results = {
                'target': target,
                'scan_type': scan_type,
                'port_range': port_range,
                'arguments': arguments,
                'raw_data': self.nm,
                'hosts': self.nm.all_hosts()
            }
            
            return self.last_scan_results
            
        except nmap.PortScannerError as e:
            raise RuntimeError(f"Nmap scan failed: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error during scan: {str(e)}")
    
    def format_results(self, scan_data: Optional[Dict] = None) -> str:
        """
        Format scan results into human-readable text.
        
        Args:
            scan_data: Scan results dictionary (uses last scan if None)
        
        Returns:
            Formatted string with scan results
        """
        if scan_data is None:
            scan_data = self.last_scan_results
        
        if not scan_data:
            return "No scan results available."
        
        nm = scan_data['raw_data']
        target = scan_data['target']
        
        output = []
        output.append("=" * 70)
        output.append(f"NMAP SCAN RESULTS")
        output.append("=" * 70)
        output.append(f"Target: {target}")
        output.append(f"Scan Type: {scan_data['scan_type']}")
        output.append(f"Port Range: {scan_data['port_range']}")
        output.append(f"Scan Arguments: {scan_data['arguments']}")
        output.append("=" * 70)
        output.append("")
        
        if not scan_data['hosts']:
            output.append("No hosts found or host is down.")
            return "\n".join(output)
        
        for host in scan_data['hosts']:
            output.append(f"\n{'='*70}")
            output.append(f"Host: {host}")
            
            if 'hostnames' in nm[host]:
                hostnames = nm[host]['hostnames']
                if hostnames and hostnames[0]['name']:
                    output.append(f"Hostname: {hostnames[0]['name']}")
            
            state = nm[host].state()
            output.append(f"State: {state}")
            output.append(f"{'='*70}")
            
            protocols = nm[host].all_protocols()
            
            if not protocols:
                output.append("\nNo open ports found.")
                continue
            
            for proto in protocols:
                output.append(f"\nProtocol: {proto.upper()}")
                output.append("-" * 70)
                
                ports = nm[host][proto].keys()
                sorted_ports = sorted(ports)
                
                output.append(f"{'PORT':<10} {'STATE':<15} {'SERVICE':<20} {'VERSION'}")
                output.append("-" * 70)
                
                for port in sorted_ports:
                    port_info = nm[host][proto][port]
                    port_num = f"{port}/{proto}"
                    state = port_info['state']
                    service = port_info.get('name', 'unknown')
                    version = port_info.get('product', '')
                    
                    if port_info.get('version'):
                        version += f" {port_info['version']}"
                    
                    output.append(f"{port_num:<10} {state:<15} {service:<20} {version}")
                
                output.append("-" * 70)
                output.append(f"Total open ports: {len(sorted_ports)}")
        
        output.append("\n" + "=" * 70)
        output.append("SCAN COMPLETE")
        output.append("=" * 70)
        
        return "\n".join(output)
