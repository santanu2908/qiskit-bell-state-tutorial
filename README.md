# 🔮 Quantum Hello World — Your First Quantum Program

A beginner-friendly, step-by-step guide to building your first quantum computing program using IBM's **Qiskit** Python package. Creating a **Bell State** — the quantum equivalent of "Hello, World!" — demonstrating **superposition** and **entanglement**.

> You don't need a physics degree. If you know basic Python, you're ready.

---

## 📋 Table of Contents

- [What Are We Building?](#what-are-we-building)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [The Full Program](#the-full-program)
- [Step-by-Step Breakdown](#step-by-step-breakdown)
  - [Step 1 — Create the Circuit](#step-1--create-the-circuit)
  - [Step 2 — Hadamard Gate (Superposition)](#step-2--hadamard-gate-superposition)
  - [Step 3 — CNOT Gate (Entanglement)](#step-3--cnot-gate-entanglement)
  - [Step 4 — Measure](#step-4--measure)
  - [Step 5 — Simulate & Run](#step-5--simulate--run)
- [Understanding the Math](#understanding-the-math)
  - [What Does |0⟩ Mean?](#what-does-0-mean)
  - [What Is Superposition?](#what-is-superposition)
  - [Why √2?](#why-2)
- [Expected Output](#expected-output)
- [Circuit Diagram](#circuit-diagram)
- [Quick Reference](#quick-reference)
- [What's Next?](#whats-next)
- [Resources](#resources)

---

## What Are We Building?

In classical computing, a bit is either `0` or `1`. In quantum computing, a **qubit** can be both at the same time — this is called **superposition**. When two qubits are linked so that measuring one instantly determines the other, that's called **entanglement**.

We're going to:

1. Create **2 qubits**
2. Put one into **superposition** (both 0 and 1 simultaneously)
3. **Entangle** them (link their fates)
4. **Measure** both
5. See that we only ever get `00` or `11` — never `01` or `10`

This is the **Bell State**, and Einstein famously called it _"spooky action at a distance."_

---

## Prerequisites

- Python 3.8 or higher
- Basic Python knowledge (variables, functions, imports)

---

## Installation

```bash
pip install qiskit
```

---

## The Full Program

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# Step 1: Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Step 2: Apply a Hadamard gate to qubit 0 (superposition)
qc.h(0)

# Step 3: Apply a CNOT gate (entangle qubit 0 and qubit 1)
qc.cx(0, 1)

# Step 4: Measure both qubits
qc.measure([0, 1], [0, 1])

# Step 5: Draw the circuit
print(qc.draw())

# Step 6: Simulate and get results
sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
result = job.result()
counts = result[0].data.meas.get_counts()

print(counts)
```

---

## Step-by-Step Breakdown

### Step 1 — Create the Circuit

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(2, 2)
```

| What                   | Why                                                                                                         |
| ---------------------- | ----------------------------------------------------------------------------------------------------------- |
| `QuantumCircuit`       | The blueprint where you design your quantum program — like a blank sheet of music.                          |
| `StatevectorSampler`   | A simulator that runs your quantum circuit on your laptop (no real quantum computer needed).                |
| `QuantumCircuit(2, 2)` | Creates a circuit with **2 qubits** (quantum bits) and **2 classical bits** (to store measurement results). |

> Both qubits start in state **|0⟩** — quantum notation for "definitely zero."

---

### Step 2 — Hadamard Gate (Superposition)

```python
qc.h(0)
```

The **Hadamard gate (H)** is applied to qubit 0. It transforms the qubit from a definite `|0⟩` into a **superposition** — equally likely to be measured as `0` or `1`.

**Analogy:** Imagine flipping a coin and freezing it mid-air. It's not heads, not tails — it's _both_ until you look.

**Mathematically:**

```
|0⟩  →  (|0⟩ + |1⟩) / √2
```

> Don't worry — we break this math down fully in the [Understanding the Math](#understanding-the-math) section below.

---

### Step 3 — CNOT Gate (Entanglement)

```python
qc.cx(0, 1)
```

The **CNOT (Controlled-NOT)** gate links two qubits:

- **Control qubit:** qubit 0
- **Target qubit:** qubit 1
- **Rule:** _"If qubit 0 is 1, flip qubit 1. Otherwise, do nothing."_

Since qubit 0 is in **superposition**, something remarkable happens — the two qubits become **entangled**:

- If you measure qubit 0 as `0` → qubit 1 is **always** `0`
- If you measure qubit 0 as `1` → qubit 1 is **always** `1`

Their fates are now permanently linked. This is the **Bell State**:

```
(|00⟩ + |11⟩) / √2
```

---

### Step 4 — Measure

```python
qc.measure([0, 1], [0, 1])
```

This **measures** both qubits and writes the results into the classical bits:

- Qubit 0's result → classical bit 0
- Qubit 1's result → classical bit 1

Measurement **collapses** the superposition. The coin finally lands.

---

### Step 5 — Simulate & Run

```python
sampler = StatevectorSampler()           # Create the simulator
job = sampler.run([qc], shots=1000)      # Run the circuit 1000 times
result = job.result()                    # Get results
counts = result[0].data.c.get_counts()  # Count outcomes
print(counts)
```

| Line                   | What It Does                                                    |
| ---------------------- | --------------------------------------------------------------- |
| `StatevectorSampler()` | Initializes a mathematical simulator of a quantum computer.     |
| `shots=1000`           | Runs the experiment 1000 times to build up statistics.          |
| `get_counts()`         | Counts how many times each outcome (`00`, `11`, etc.) appeared. |

---

## Understanding the Math

### What Does |0⟩ Mean?

The `| ⟩` symbols are **Dirac notation** (or "ket" notation) — just a naming convention for quantum states:

- `|0⟩` = the qubit is **definitely 0** (like a light switch that's OFF)
- `|1⟩` = the qubit is **definitely 1** (like a light switch that's ON)

Think of a box with a ball inside:

| State         | What's in the box        | When you open it                           |
| ------------- | ------------------------ | ------------------------------------------ |
| `\|0⟩`        | A red ball (definitely)  | Always red. 100% of the time.              |
| `\|1⟩`        | A blue ball (definitely) | Always blue. 100% of the time.             |
| Superposition | Both at once             | Could be either — you can't predict which. |

**Key idea:** `|0⟩` and `|1⟩` are _certain_ states. There's nothing weird about them. The weirdness only starts when a gate like Hadamard **mixes** them.

---

### What Is Superposition?

A qubit in superposition is written as:

```
α|0⟩ + β|1⟩
```

Where **α** and **β** are numbers (called amplitudes) that determine the probabilities:

```
Probability of measuring 0  =  α²
Probability of measuring 1  =  β²
```

And since probabilities must add to 100%:

```
α² + β² = 1    (always!)
```

**Examples:**
| State | α | β | P(\|0⟩) = α² | P(\|1⟩) = β² |
|-------|---|---|--------------|--------------|
| `\|0⟩` | 1 | 0 | 100% | 0% |
| `\|1⟩` | 0 | 1 | 0% | 100% |
| `(\|0⟩+\|1⟩)/√2` | 1/√2 | 1/√2 | 50% | 50% |
---

### Why √2?

After the Hadamard gate:

```
α = 1/√2,  β = 1/√2
```

We need α = β (equal chances) and α² + β² = 1:

```
α² + α² = 1
2α²      = 1
α²       = 1/2
α        = 1/√2  ≈ 0.7071
```

**√2 is the _only_ number that gives a perfect 50/50 split.** It's not arbitrary — it's mathematically necessary.

---

## Expected Output

### Circuit Diagram

```
     ┌───┐     ┌─┐
q_0: ┤ H ├──■──┤M├───
     └───┘┌─┴─┐└╥┘┌─┐
q_1: ─────┤ X ├─╫─┤M├
          └───┘ ║ └╥┘
c: 2/═══════════╩══╩═
                0  1
```

Read left to right: **H gate** on q_0 → **CNOT** connecting q_0 to q_1 → **Measurements**.

### Measurement Results

```
{'00': 512, '11': 488}
```

Out of 1000 runs:

- `00` appeared ~500 times
- `11` appeared ~500 times
- `01` and `10` **never appear** — because the qubits are entangled!

> Your exact numbers will vary slightly (it's random!), but the ~50/50 split between `00` and `11` is consistent.

---

## Quick Reference

| Concept | Symbol / Code | What It Does |
|---------------------|-------------------------------|--------------------------------------------------|
| Qubit in state zero | `\|0⟩` | Definitely 0 when measured |
| Qubit in state one | `\|1⟩` | Definitely 1 when measured |
| Superposition | `(\|0⟩ + \|1⟩) / √2` | 50% chance of 0 or 1 |
| Hadamard gate | `qc.h(0)` | Puts a qubit into superposition |
| CNOT gate | `qc.cx(0, 1)` | Entangles two qubits |
| Measurement | `qc.measure()` | Collapses superposition, gives a definite result |
| Bell State | `(\|00⟩ + \|11⟩) / √2` | Two entangled qubits — always measured the same |
---

## What's Next?

Now that you've mastered the Bell State, here are some paths to explore:

- **More gates** — Try the Pauli-X (`qc.x()`), Pauli-Z (`qc.z()`), and Phase gates
- **Quantum Teleportation** — Transfer a qubit's state using entanglement
- **Deutsch-Jozsa Algorithm** — Your first quantum algorithm that beats classical computers
- **Run on real hardware** — Use [IBM Quantum](https://quantum.ibm.com/) to run on actual quantum computers in the cloud

---

## Resources

- [Qiskit Documentation](https://docs.quantum.ibm.com/)
- [Qiskit Textbook](https://learning.quantum.ibm.com/)
- [IBM Quantum Platform](https://quantum.ibm.com/)

---

## License

MIT

---

_Built with ❤️ and quantum entanglement._
