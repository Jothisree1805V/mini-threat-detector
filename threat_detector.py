import random

THREATS = {
    "normal": "Normal traffic",
    "port_scan": "Port scanning detected",
    "brute_force": "Brute-force attack detected",
    "ddos": "Possible DDoS attack detected",
}

def analyze_traffic():
    """Simulate network traffic and detect suspicious behavior."""
    traffic_types = ["normal", "normal", "normal", "port_scan",
                     "brute_force", "ddos"]

    traffic = random.choice(traffic_types)

    print(f"\nTraffic analysis result:")
    print(f"Status: {THREATS[traffic]}")

    if traffic == "normal":
        print("Risk Level: LOW")
    elif traffic == "port_scan":
        print("Risk Level: MEDIUM")
    else:
        print("Risk Level: HIGH")


if __name__ == "__main__":
    print("🛡️ Mini Network Threat Detector")
    print("-" * 35)

    for _ in range(5):
        analyze_traffic()