# Gradient Calculation Project

This project demonstrates **numerical gradient calculation** for a simple **linear regression cost function**, comparing it with the **analytical gradient** solution.

---

## 🚀 Features

* Numerical gradient calculation using **finite differences**
* Analytical gradient calculation for **Mean Squared Error (MSE)** cost function
* Side-by-side comparison of numerical and analytical results
* Clean, modular, and well-documented code

---

## 📦 Installation

1. **Clone this repository**:

   ```bash
   git clone <your-repo-url>
   cd gradient-calculation-project
   ```

2. **Create and activate a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🧠 Usage

Run the main script:

```bash
python gradient.py
```

This will:

* Calculate the cost function at several test points
* Compute both numerical and analytical gradients
* Print a comparison table showing the differences

---

## 🖥️ Example Output

```
=== Gradient Calculation Demo ===

At w = 0:
Cost: 18.6667
Numerical gradient: -9.3333
Analytical gradient: -9.3333

At w = 1:
Cost: 0.0000
Numerical gradient: 0.0000
Analytical gradient: 0.0000

Gradient Comparison:
w       Numerical       Analytical      Difference
----------------------------------------------
-1.0    -18.666667      -18.666667      0.000000
0.0     -9.333333       -9.333333       0.000000
1.0     0.000000        0.000000        0.000000
2.0     9.333333        9.333333        0.000000
3.0     18.666667       18.666667       0.000000
```

---

## ✏️ Customization

You can modify the following in `gradient.py`:

* The input arrays `x` and `y` in the cost function
* The step size `h` for numerical differentiation
* The test values of `w` used for evaluating gradients

---

## 📁 Folder Structure

```
gradient-calculation-project/
├── gradient.py            # Main script with gradient logic
├── requirements.txt       # List of required packages
├── README.md              # Project documentation
├── .gitignore             # Files/folders to ignore
```

---

## 🔧 .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class

# IDEs
.idea/
.vscode/

# Virtual Environments
venv/
env/

# System files
.DS_Store
```

---

## 🧾 Dependencies

* Python 3.7+
* NumPy

Listed in `requirements.txt`:

```
numpy
```

---

## 📌 How to Use This Project

1. Set up the directory and add the following files:

   * `gradient.py`
   * `requirements.txt`
   * `README.md`
   * `.gitignore`

2. Set up the virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the main script:

   ```bash
   python gradient.py
   ```

The script will:

* Calculate the cost function and gradients at several test points
* Compare the numerical and analytical methods
* Print a detailed comparison table

You can easily modify the input data or cost function to experiment with different scenarios. This project is a great starting point for understanding gradient computation in **machine learning**.

---

## 📝 License

This project is open source and available under the **MIT License**.

---

Built for learning and experimentation. Happy coding! 🧠📈
