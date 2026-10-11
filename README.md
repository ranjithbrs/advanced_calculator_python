# 🧮 Advanced Scientific Calculator (Python CLI)

[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Interface: CLI](https://img.shields.io/badge/Interface-Interactive%20CLI-blue?style=for-the-badge&logo=gnubash&logoColor=white)](sci_calc.py)
[![GUI Sibling: AdvSciCalcGUI](https://img.shields.io/badge/GUI%20Version-AdvSciCalcGUI-orange?style=for-the-badge)](https://github.com/ranjithbrs/AdvSciCalcGUI)
[![Unit Tests: 100% Passing](https://img.shields.io/badge/Unit%20Tests-100%25%20Passing-success?style=for-the-badge&logo=checkmarx&logoColor=white)](test_sci_calc.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

> 🌟 **A fast, menu-driven scientific calculator that runs right inside your terminal without any extra software!**

---

## 💡 What is this Project in 30 Seconds? (In Plain English)

Have you ever needed to do quick scientific math while working in a terminal or on a server, without opening a web browser or searching for a physical calculator?

This project is a **smart, menu-driven calculator in Python**:
- 🔢 **Simple Numbered Menu:** Just pick an operation by number (e.g., `1` for Addition, `5` for Powers, `7` for Square Root, `11` for Trigonometry).
- ⚡ **Instant & Accurate:** Type your numbers and get exact results with up to 6 decimal precision in milliseconds.
- 🛡️ **Zero Crashes:** Built-in safeguards protect against division by zero, invalid roots, or complex numbers so the program never crashes.

---

## 📸 Example Usage

![Calculator Interface Screenshot](Screenshot_of_example.png)

---

## 📑 Table of Contents
- [What is this Project?](#-what-is-this-project-in-30-seconds-in-plain-english)
- [Architecture & Execution Workflow](#-architecture--execution-workflow)
- [Key Features](#-key-features)
- [Operation Menu & Supported Functions](#-operation-menu--supported-functions)
- [Local Setup & Usage](#-local-setup--usage)
- [Automated Unit Testing](#-automated-unit-testing)
- [Desktop GUI Version](#-desktop-gui-version)
- [Author & Connect](#-author)
- [License](#-license)

---

## 📐 Architecture & Execution Workflow

```mermaid
flowchart TD
    subgraph CLI["🖥️ Interactive Command-Line Interface"]
        A[User Launches CLI: python sci_calc.py] --> B[Display Operations Menu]
        B --> C[User Selects Operation Code or 'exit']
    end

    subgraph Controller["⚙️ Input Validation & Parsing"]
        C -->|Valid Code| D{Determine Operands Count}
        C -->|'exit'| E[Gracefully Terminate Session]
        D -->|Binary Op: +, -, *, /, **, //, %| F[Acquire Operand A & Operand B]
        D -->|Unary Op: sqrt, sin, cos, !, ln| G[Acquire Single Operand]
        D -->|Logarithm| H[Acquire Value & Base default 10]
    end

    subgraph Engine["📐 Core Math Engine (sci_calc.py)"]
        F --> I{Execute Mathematical Logic}
        G --> I
        H --> I
        I -->|Zero Division / Negative Root| J[Return Guarded Error String]
        I -->|Valid Computation| K[Format Result to 6 Decimals]
    end

    subgraph Presentation["📊 Output Terminal Display"]
        J --> L[Print Error Diagnostic Banner]
        K --> M[Print Formatted Calculation Result]
        L --> B
        M --> B
    end
```

---

## ✨ Key Features

- **Basic & Advanced Arithmetic**: Addition, subtraction, multiplication, floating-point division, integer floor division (`//`), modulus (`%`), and arbitrary exponentiation (`**`).
- **Comprehensive Trigonometry**: Direct evaluation of sine (`sin`), cosine (`cos`), and tangent (`tan`) in degrees, alongside reciprocal secant (`sec`), cosecant (`cosec`), and cotangent (`cot`).
- **Inverse Trigonometric Functions**: Arcsine (`asin`), arccosine (`acos`), and arctangent (`atan`) with domain validation.
- **Logarithmic & Exponential Suite**: Arbitrary-base logarithms (`log`), natural logarithms (`ln`), and Euler's exponential powers (`exp`).
- **Combinatorics**: Integer factorials (`!`) with input validation preventing fractional or negative evaluations.
- **Defensive Error Handling**: Traps division by zero, invalid logarithm bases ($b \le 0, b = 1$), imaginary square roots, and type mismatches without crashing the session loop.

---

## 📋 Operation Menu & Supported Functions

| Option Code | Operation | Mathematical Formula | Example Input $\rightarrow$ Output |
| :--- | :--- | :--- | :--- |
| `+` | Addition | $a + b$ | `5` and `6` $\rightarrow$ `11.0` |
| `-` | Subtraction | $a - b$ | `10` and `4` $\rightarrow$ `6.0` |
| `*` | Multiplication | $a \times b$ | `3` and `7` $\rightarrow$ `21.0` |
| `/` | Division | $a / b$ | `20` and `5` $\rightarrow$ `4.0` |
| `**` | Exponentiation | $a^b$ | `2` and `3` $\rightarrow$ `8.0` |
| `sqrt` | Square Root | $\sqrt{a}$ | `16` $\rightarrow$ `4.0` |
| `%` | Modulo | $a \pmod b$ | `10` and `3` $\rightarrow$ `1.0` |
| `log` | Logarithm | $\log_b(a)$ | `8`, Base `2` $\rightarrow$ `3.0` |
| `ln` | Natural Log | $\ln(a)$ | `2.718282` $\rightarrow$ `1.0` |
| `!` | Factorial | $n!$ | `5` $\rightarrow$ `120` |
| `//` | Floor Division | $\lfloor a / b \rfloor$ | `10` and `3` $\rightarrow$ `3.0` |
| `sin` | Sine (Degrees) | $\sin(\theta)$ | `90` $\rightarrow$ `1.0` |
| `cos` | Cosine (Degrees) | $\cos(\theta)$ | `0` $\rightarrow$ `1.0` |
| `tan` | Tangent (Degrees) | $\tan(\theta)$ | `45` $\rightarrow$ `1.0` |
| `exp` | Exponential | $e^x$ | `1` $\rightarrow$ `2.718282` |
| `sec` | Secant | $\sec(\theta)$ | `0` $\rightarrow$ `1.0` |
| `cosec` | Cosecant | $\csc(\theta)$ | `90` $\rightarrow$ `1.0` |
| `cot` | Cotangent | $\cot(\theta)$ | `45` $\rightarrow$ `1.0` |
| `asin` | Arcsine | $\arcsin(x)$ | `1` $\rightarrow$ `90.0` |
| `acos` | Arccosine | $\arccos(x)$ | `1` $\rightarrow$ `0.0` |
| `atan` | Arctangent | $\arctan(x)$ | `1` $\rightarrow$ `45.0` |
| `exit` | Terminate Session | — | Exits interactive loop cleanly |

---

## 🚀 Local Setup & Usage

### Prerequisites
- Python 3.8 or higher installed on your system.

### 1. Clone the Repository
```bash
git clone https://github.com/ranjithbrs/advanced_calculator_python.git
cd advanced_calculator_python
```

### 2. Run the Interactive CLI
```bash
python sci_calc.py
```

### 3. Use as a Python Module
`sci_calc.py` can be directly imported into any Python project:
```python
import sci_calc

print(sci_calc.addition(15, 25))        # 40.0
print(sci_calc.sine(90, mode="deg"))     # 1.0
print(sci_calc.factorial(6))             # 720
```

---

## 🧪 Automated Unit Testing

The repository features an automated test suite verifying all mathematical routines, boundary conditions, and exception handlers:

```bash
python -m unittest test_sci_calc.py -v
```

Output:
```text
Ran 8 tests in 0.001s

OK
```

---

## 🖥️ Desktop GUI Version

Looking for a desktop application with an LCD display, mouse keypad, calculation history, and standalone `.exe` packaging? Check out the sister repository:  
👉 **[AdvSciCalcGUI](https://github.com/ranjithbrs/AdvSciCalcGUI)**

---

## 👨‍💻 Author

**Ranjith B**  
🎓 *B.Tech Computer Science & Business Systems (CSBS)*  
🏛️ *Nehru Institute of Engineering and Technology, Coimbatore*  

- 💼 **LinkedIn**: [linkedin.com/in/ranjith-b-csbs](https://linkedin.com/in/ranjith-b-csbs)  
- 🐙 **GitHub**: [github.com/ranjithbrs](https://github.com/ranjithbrs)  
- 🌐 **Portfolio**: [ranjithbrs.github.io/portfolio](https://ranjithbrs.github.io/portfolio/)  
- 📧 **Email**: ranjithb2k06@gmail.com  

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
