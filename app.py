import streamlit as st

st.set_page_config(page_title="Pakistani CS Merit Calculator", page_icon="🎓")
st.title("🎓 Pakistani CS Merit & Target Score Calculator")
st.caption("Built for FBISE & BISE Lahore FSc / ICS Students | By a 2nd Year CS Applicant")

# Step 1: Board Marks Input
st.subheader("1. Enter Your Board Marks")
col1, col2 = st.columns(2)
with col1:
    matric_obt = st.number_input("Matric Obtained Marks", min_value=0, max_value=1200, value=1034)
    matric_tot = st.number_input("Matric Total Marks", min_value=1, max_value=1200, value=1100)
with col2:
    inter_obt = st.number_input("Inter Part-1 Obtained Marks", min_value=0, max_value=600, value=519)
    inter_tot = st.number_input("Inter Part-1 Total Marks", min_value=1, max_value=600, value=560)

if matric_obt > matric_tot or inter_obt > inter_tot:
    st.error("⚠️ Obtained marks cannot be greater than total marks.")
    st.stop()

matric_pct = (matric_obt / matric_tot) * 100
inter_pct = (inter_obt / inter_tot) * 100

st.info(f"**Your Board Percentages:** Matric: `{matric_pct:.2f}%` | Inter Part-1: `{inter_pct:.2f}%`")

tab1, tab2 = st.tabs(["Calculate My Aggregate", "Target Entry Test Score"])

# TAB 1: CALCULATE AGGREGATE
with tab1:
    st.subheader("2. Select University & Entry Test Score")
    uni = st.selectbox("Select University & Formula", [
        "LUMS (Holistic — Matric, Inter-1 & SAT/LCAT)",
        "NUST (NET — 75% Test, 15% Inter, 10% Matric)",
        "FAST-NUCES (NU Test — 50% Test, 40% Inter, 10% Matric)",
        "COMSATS Lahore (NTS NAT — 50% Test, 40% Inter, 10% Matric)",
        "ITU Lahore (ITU CS Test — 50% Test, 35% Inter, 15% Matric)",
        "UET Lahore (ECAT — 33% Test, 50% Inter, 17% Matric)",
        "GIKI (GIKI Test — 85% Test, 15% Matric; 60% Inter min)"
    ])

    if "NUST" in uni:
        st.caption("ℹ️ NUST NET is out of **200** marks (or enter **1600** total if applying on separate SAT basis).")
    elif "FAST" in uni:
        st.caption("ℹ️ FAST NU Test is out of **100** marks (SAT & NTS NAT have separate, higher-merit lists).")
    elif "COMSATS" in uni:
        st.caption("ℹ️ COMSATS accepts **NTS NAT** or **COMSATS Special Test** (both out of **100** marks).")
    elif "ITU" in uni:
        st.caption("ℹ️ ITU CS/AI Test is out of **60** MCQs (or enter **100** for Engineering/NAT, **400** for ECAT, **1600** for SAT).")
    elif "UET" in uni:
        st.caption("ℹ️ UET ECAT is out of **400** marks (Hafiz-e-Quran candidates get +20 marks in FSc).")
    elif "GIKI" in uni:
        st.caption("ℹ️ GIKI Admission Test is out of **200** marks (requires min 60% in Inter overall, Math & Physics).")

    if "LUMS" not in uni:
        if "NUST" in uni:
            def_obt, def_tot = 150.0, 200.0
        elif "ITU" in uni:
            def_obt, def_tot = 45.0, 60.0
        elif "UET" in uni:
            def_obt, def_tot = 260.0, 400.0
        elif "GIKI" in uni:
            def_obt, def_tot = 140.0, 200.0
        else:  # FAST, COMSATS
            def_obt, def_tot = 75.0, 100.0

        c1, c2 = st.columns(2)
        with c1:
            test_obt = st.number_input("Entry Test / SAT Obtained Marks", min_value=0.0, max_value=1600.0, value=def_obt, key=f"obt_{uni}")
        with c2:
            test_tot = st.number_input("Entry Test / SAT Total Marks", min_value=1.0, max_value=1600.0, value=def_tot, key=f"tot_{uni}")

    if st.button("Check Eligibility / Calculate Aggregate", type="primary"):
        if "LUMS" in uni:
            st.info("**LUMS uses a holistic admission model** (no fixed aggregate percentage), evaluating Matric, Inter-1, SAT/LCAT, personal statement, and extracurriculars together.")
            if matric_pct >= 75 and inter_pct >= 75:
                st.success(f"✅ Your board marks (Matric: {matric_pct:.1f}%, Inter-1: {inter_pct:.1f}%) meet LUMS SBASSE minimum eligibility (75%+ in both)! Competitive CS applicants typically aim for **1350–1450+ on the SAT** (or a strong LCAT).")
            else:
                st.warning("⚠️ LUMS SBASSE (Computer Science) strictly requires at least **75% in Matric and 75% in Intermediate** (FSc/ICS).")
        else:
            if test_obt > test_tot:
                st.error("⚠️ Entry test obtained marks cannot exceed total marks.")
            else:
                test_pct = (test_obt / test_tot) * 100

                if "NUST" in uni:
                    agg = (test_pct * 0.75) + (inter_pct * 0.15) + (matric_pct * 0.10)
                elif "FAST" in uni or "COMSATS" in uni:
                    agg = (test_pct * 0.50) + (inter_pct * 0.40) + (matric_pct * 0.10)
                elif "ITU" in uni:
                    agg = (test_pct * 0.50) + (inter_pct * 0.35) + (matric_pct * 0.15)
                elif "UET" in uni:
                    agg = (test_pct * 0.33) + (inter_pct * 0.50) + (matric_pct * 0.17)
                else:  # GIKI
                    agg = (test_pct * 0.85) + (matric_pct * 0.15)

                st.success(f"**Your Estimated Aggregate:** `{agg:.2f}%`")
                st.caption("Note: Weightage formulas follow standard university policies; always verify with the latest prospectus.")

# TAB 2: REVERSE TARGET SCORE CALCULATOR
with tab2:
    st.subheader("How much do you need on your Entry Test?")
    target_agg = st.slider("Select Target Closing Merit (%)", min_value=60.0, max_value=95.0, value=79.0, step=0.5)

    req_nust = (target_agg - (inter_pct * 0.15) - (matric_pct * 0.10)) / 0.75
    req_fast = (target_agg - (inter_pct * 0.40) - (matric_pct * 0.10)) / 0.50
    req_itu = (target_agg - (inter_pct * 0.35) - (matric_pct * 0.15)) / 0.50
    req_uet = (target_agg - (inter_pct * 0.50) - (matric_pct * 0.17)) / 0.33
    req_giki = (target_agg - (matric_pct * 0.15)) / 0.85

    def format_req(req_pct, max_marks):
        if req_pct <= 0:
            return "Already cleared by board marks!"
        elif req_pct > 100:
            return f"Not reachable ({req_pct:.1f}% needed)"
        else:
            marks = (req_pct / 100) * max_marks
            return f"**{marks:.1f} / {max_marks}** ({req_pct:.1f}%)"

    st.write(f"🏛️ **NUST NET (out of 200):** {format_req(req_nust, 200)} *(2026 SEECS CS closing: ~76.8–79%)*")
    st.write(f"💻 **FAST NU Test (out of 100):** {format_req(req_fast, 100)} *(2026 LHR/ISB CS closing: ~73–75%)*")
    st.write(f"📘 **COMSATS NTS NAT (out of 100):** {format_req(req_fast, 100)} *(2026 LHR CS: ~85–86.5% | ISB: ~88%)*")
    st.write(f"🔬 **ITU Lahore CS Test (out of 60 MCQs):** {format_req(req_itu, 60)} *(2026 CS closing: ~80.5%)*")
    st.write(f"⚙️ **UET ECAT (out of 400):** {format_req(req_uet, 400)} *(2026 Main Campus A1 CS: ~79–82%)*")
    st.write(f"🏔️ **GIKI Test (out of 200):** {format_req(req_giki, 200)}")
    st.caption("Note: LUMS evaluates applicants holistically (Matric, Inter-1, SAT/LCAT & essays) rather than a fixed aggregate cutoff.")

st.divider()
st.link_button("📝 Quick 10-Second Feedback / Suggest a University", "https://docs.google.com/forms/d/e/1FAIpQLSdg7M9FEw8RMs8JsJRf41t6LXIz1vaiFTfWeI8Djn6kFTpWqA/viewform?usp=dialog")
