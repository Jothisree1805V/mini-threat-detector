import random
from datetime import datetime

THREATS = {
    "normal": "Normal traffic",
    "port_scan": "Port scanning detected",
    "brute_force": "Brute-force attack detected",
    "ddos": "Possible DDoS attack detected",
}

def get_risk_level(traffic):
    if traffic == "normal":
        return "LOW"
    elif traffic == "port_scan":
        return "MEDIUM"
    elif traffic in ["brute_force", "ddos"]:
        return "HIGH"
    else:
        return "UNKNOWN"


def analyze_traffic():
    """Simulate network traffic and detect suspicious behavior."""
    traffic_types = ["normal", "normal", "normal", "port_scan",
                     "brute_force", "ddos"]

    traffic = random.choice(traffic_types)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n" + "=" * 40)
    print("       NETWORK THREAT ANALYSIS")
    print("=" * 40)
    print(f"Timestamp: {timestamp}")
    
    print(f"Traffic Type : {traffic.upper()}")
    print(f"Status       : {THREATS[traffic]}")
    print(f"Risk Level   : {get_risk_level(traffic)}")
    print("=" * 40)


if __name__ == "__main__":
    print("🛡️ Mini Network Threat Detector")
    print("-" * 35)

    for _ in range(5):
        analyze_traffic()