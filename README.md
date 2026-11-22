# 🛡️ Mini Network Threat Detector

A beginner-friendly Python cybersecurity project that simulates network traffic and identifies potential security threats using basic risk-level classification.

## 🚀 Features

- Normal traffic detection
- Port scan detection
- Brute-force attack detection
- Possible DDoS attack detection
- Automatic risk-level classification (LOW, MEDIUM, HIGH)
- Automated unit testing

## 🛠️ Technologies Used

- Python
- Random module
- Unittest framework

## 📁 Project Structure

```text
mini-threat-detector/
│
├── threat_detector.py
├── test_threat_detector.py
├── tests/
│   └── test_threat_detector.py
├── README.md
└── .gitignore
```

## ▶️ How to Run

1. Clone this repository:

```bash
git clone https://github.com/Jothisree1805V/mini-threat-detector.git
```

2. Open the project folder:

```bash
cd mini-threat-detector
```

3. Run the program:

```bash
python threat_detector.py
```

## 🧪 Run Automated Tests

```bash
python -m unittest discover -s tests -v
```

## 📊 Risk Classification

| Traffic Type | Risk Level |
|---|---|
| Normal | LOW |
| Port Scan | MEDIUM |
| Brute Force | HIGH |
| DDoS | HIGH |
| Unknown | UNKNOWN |

## 🎯 Project Objective

To understand basic cybersecurity concepts, network threat identification, Python programming, and automated software testing through a simple simulation.

## 👩‍💻 Author

Created as a beginner cybersecurity learning project.
