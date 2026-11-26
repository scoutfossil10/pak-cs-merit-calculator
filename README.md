# 🎓 Pakistani CS & Engineering Merit Calculator

**Live App:** [pak-cs-merit.streamlit.app](https://pak-cs-merit.streamlit.app/)

An interactive merit aggregate and reverse target-score solver built for Pakistani FSc / ICS students applying to top undergraduate Computer Science and Engineering programs.

---

## 📌 Problem & Motivation
Every Pakistani university uses a different weightage formula across Matriculation, Inter Part-1 (HSSC-I), and entry exams—along with different test total marks (`60`, `100`, `200`, `400`, or `1600` for SAT). Built by a 2nd-year ICS student at **GCU Lahore**, this app eliminates manual spreadsheet guesswork, validates minimum eligibility rules, and benchmarks target scores against 2026 closing merits.

## ✨ Key Features
* **Smart Input Validation & Board Defaults:**  
  Pre-configured for modern Pakistani board totals (`1100,1200` Matric, `560` Inter Part-1) with automatic error guarding against invalid or zero entries.
* **Multi-University Aggregate Calculator (8 Tracks Across 7 Universities):**  
  Automatically adapts default test totals and weightage formulas when switching institutions:
  * **NUST (NET / SAT):** 75% Test + 15% Inter-1 + 10% Matric *(out of 200 or 1600)*
  * **FAST-NUCES (Computing / Business):** 50% NU Test + 40% Inter-1 + 10% Matric *(out of 100)*
  * **FAST-NUCES (Engineering):** 33% NU Test + 50% Inter-1 + 17% Matric *(out of 100)*
  * **COMSATS Lahore (NTS NAT / Special Test):** 50% Test + 40% Inter-1 + 10% Matric *(out of 100)*
  * **ITU Lahore (CS/AI, Engineering, NAT, ECAT, SAT):** 50% Test + 35% Inter-1 + 15% Matric *(supports 60, 100, 400, or 1600 totals)*
  * **UET Lahore (ECAT):** 33% Test + 50% Inter-1 + 17% Matric *(out of 400)*
  * **GIKI (Admission Test):** 85% Test + 15% Matric *(out of 200, with automated 60% Inter minimum eligibility check)*
  * **LUMS (SBASSE):** Holistic eligibility check (`75%+` in both Matric & Inter-1) with SAT/LCAT benchmark guidance
* **Reverse Target-Score Solver & 2026 Closing Merit Benchmarks:**  
  Given a student's board marks and a desired closing merit (`60%–95%`), calculates the exact raw score needed on every university's test—displayed alongside **2026 historical closing merit ranges** (e.g., NUST SEECS ~76.8–79%, FAST LHR/ISB CS ~73–75%, GIKI CS/AI ~75–80%) and reachability alerts.
* **Real-World Adoption:**  
  Used by **50+ unique student applicants** shortly after deployment.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Framework & Hosting:** Streamlit, Streamlit Community Cloud
* **IDE:** PyCharm

## 🚀 Run Locally
1. **Clone the repository:**
   ```bash
   git clone https://github.com/scoutfossil10/pak-cs-merit-calculator
   cd pak-cs-merit-calculator
   ```
2. **Install Streamlit:**
   ```bash
   pip install streamlit
   ```
3. **Launch the app:**
   ```bash
   streamlit run app.py
   ```
   *(Replace `app.py` with your main Python filename if named differently.)*

## ⚠️ Disclaimer
This is an independent, student-built estimation tool (weightages and closing merits updated November 2026). Final admission depends on official university policies and Inter Part-2 results—always verify with each university's official prospectus.

--
Built by **Muhammad Rehan Javed** | [GitHub](https://github.com/scoutfossil10) • [LinkedIn](https://www.linkedin.com/in/muhammad-rehan-javed-847701211/)
