# ML-FlagOptNet
ML model that predicts the optimal set of compiler flags for a given C/C++ program, based on static code features such as loops, branching, and function complexity. 
The core idea is to build a pipeline that combines static analysis (via AST parsing) with dynamic benchmarking (via GCC compiler flags), which enables the automated optimization of C code by predicting how different optimization settings will affect performance.

By using machine learning (specifically XGBoost regressor), we can predict the runtime performance of C programs based on their structural features, and recommend the best set of compiler flags for optimization.

## 🏗️ Project Overview

### Objective
The goal is to build a system that:

- Extracts structural features from C source code files using Clang's AST parsing.
- Compiles and benchmarks the C code with various compiler optimization flags (e.g., `-O1`, `-O2`, `-O3`, `-Os`).
- Trains a machine learning model to predict runtime performance (in milliseconds) of a program based on its structural features.
- Predicts the runtime performance of a new C program and suggests the most optimal compiler flags.

### Components

- **Feature Extraction**: The program uses Clang's AST parsing to extract features like loop count, nesting depth, function calls, and more.
  
- **Benchmarking**: It runs the C program using GCC with various optimization flags and measures the runtime.
  
- **ML Training**: We train a machine learning model using the features and runtime data to predict runtime performance for unseen C programs.

- **Prediction**: Once the model is trained, it can predict the runtime for a new program and recommend flags.

### Use Cases
This pipeline can be used for:
- Optimizing performance of existing C code automatically.
- Research in compiler optimization and machine learning-powered auto-tuning systems.
- Educational purposes to demonstrate the impact of compiler flags on performance.

---

## 🚀 Code Performance Benchmarking & ML Prediction Pipeline

This project automates the **extraction of structural features from C programs**, benchmarks their execution under various **GCC compiler optimization flags**, and trains a machine learning model to **predict runtime performance** based on code structure.



## 📦 Project Structure
```
code-benchmark-ml/
├── c_sources/ # Input C programs
│ ├── sample.c # Example: Fibonacci
│ └── ... # Add more test cases
├── build/ # Compiled binaries
├── scripts/
│ ├── extract_features.py # AST-based code feature extraction (Clang)
│ ├── benchmark_runner.py # GCC compile and runtime benchmarking
│ ├── pipeline.py # End-to-end data collection pipeline
│ ├── train_model.py # ML training script (XGBoost regressor)
│ └── test_model.py # Predict runtime of new C files
├── dataset.csv # Generated dataset with features + runtime
├── requirements.txt # Python dependencies
└── README.md # You're here
```

---

## 🎯 Features Extracted (from AST)

| Feature         | Description                              |
|----------------|------------------------------------------|
| `num_loops`     | Count of `for`, `while`, `do-while`     |
| `max_nesting`   | Estimated nesting depth (indent-based)  |
| `num_branches`  | Count of `if`, `switch`                 |
| `num_calls`     | Total `CallExpr` (function calls)       |
| `num_funcs`     | Number of `FunctionDecl` (functions)    |
| `loc`           | Total lines of code                     |

---

## ✅ Setup

### 🛠 System Dependencies

Install required tools:

```bash
sudo apt update
sudo apt install gcc clang
```

## 📦 Python Environment
### Install dependencies:
```bash
git clone https://github.com/yourusername/code-benchmark-ml.git
cd code-benchmark-ml
pip install -r requirements.txt
```


## 🧪 Add C Files
Place your C programs in the `c_sources/` directory. These will be used for feature extraction and benchmarking.

For optimal benchmarking, make sure your C files contain some computational complexity. Here's an example of a C loop with a heavy workload:

```c
for (long long i = 0; i < 100000000; i++) {
    x += i % 3;
}
```
## 🚀 Running the Pipeline
The pipeline automates the following processes:

- **Extracts features** from C source files.
- **Compiles and benchmarks** the program with different compiler flags.
- **Builds the dataset** for machine learning (ML) training.

### Run the pipeline using:

```bash
python scripts/pipeline.py
```
## 🤖 Training the Model
Once you have the dataset, you can train the machine learning model. The model uses the structural features to predict runtime performance based on the data extracted from your C programs.

### To train the model, run:

```bash
python scripts/train_model.py
```
###Example Output:
```
✅ Model R² score: 0.846
```
## 🔮 Test on a New C File
Once the model is trained, you can use it to predict the runtime performance of a new C file.

### To predict the runtime performance of a new C file, run the following command:


```bash
python scripts/test_model.py c_sources/your_test_case.c
```

### The model will:
- Analyze the new C file.
- Extract its features (like loops, function calls, branches, etc.).
- Predict the runtime performance based on the trained model.

###Example Output:
```
[🚀] Testing: c_sources/test_case.c
🔮 Predicted runtime (ms): 12.38
```


## 📊 Example dataset.csv
After running the pipeline and collecting the benchmark data, a `dataset.csv` file will be generated. This file contains the extracted features and runtime measurements for each C program and compiler flag combination.

### Here’s an example of how the generated `dataset.csv` looks:

```
num_loops,max_nesting,num_branches,num_calls,num_funcs,loc,flags,runtime_ms,file
1,2,1,2,2,15,-O1,12.45,sample.c
1,2,1,2,2,15,-O2,8.32,sample.c
2,4,2,5,3,22,-O1,32.91,matrix.c
```

This dataset contains the following columns:
- Structural Features: Number of loops, nesting depth, branches, calls, functions, and lines of code.
- Flags: Compiler flags used for benchmarking (e.g., -O1, -O2).
- Runtime: Measured runtime in milliseconds.
- File: The corresponding C source file.

## 📜 License
```
MIT License — use this code freely, with attribution.
```


```
Would you like this turned into a `README.md` file and zipped into your project scaffold? Or want badges (`build passing`, `MIT license`, `Python 3.8+`, etc.) added to the top?
```
