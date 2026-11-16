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
    inter_obt = st.number_input("Inter Part-1 Obtained Marks", min_value=0, max_value=600, value=510)
    inter_tot = st.number_input("Inter Part-1 Total Marks", min_value=1, max_value=600, value=550)

matric_pct = (matric_obt / matric_tot) * 100
inter_pct = (inter_obt / inter_tot) * 100

st.info(f"**Your Board Percentages:** Matric: `{matric_pct:.2f}%` | Inter Part-1: `{inter_pct:.2f}%`")

tab1, tab2 = st.tabs(["Calculate My Aggregate", "Target Entry Test Score"])

# TAB 1: CALCULATE AGGREGATE
with tab1:
    st.subheader("2. Enter Your Entry Test Score")
    uni = st.selectbox("Select University & Formula", [
        "NUST (NET — 75% Test, 15% Inter, 10% Matric)",
        "FAST-NUCES (NU Test — 50% Test, 40% Inter, 10% Matric)",
        "COMSATS Lahore (NTS NAT — 50% Test, 40% Inter, 10% Matric)",
        "ITU Lahore (ITU Test / NAT — 50% Test, 35% Inter, 15% Matric)",
        "UET Lahore (ECAT — 33% Test, 50% Inter, 17% Matric)",
        "GIKI (GIKI Test — 85% Test, 15% Inter)"
    ])

    c1, c2 = st.columns(2)
    with c1:
        test_obt = st.number_input("Entry Test Obtained Marks", min_value=0.0, max_value=400.0, value=145.0)
    with c2:
        test_tot = st.number_input("Entry Test Total Marks", min_value=1.0, max_value=400.0, value=200.0)

    if st.button("Calculate Aggregate", type="primary"):
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
            agg = (test_pct * 0.85) + (inter_pct * 0.15)

        st.success(f"**Your Estimated Aggregate:** `{agg:.2f}%`")
        st.caption("Note: Weightage formulas follow standard university policies; always verify with the latest prospectus.")

# TAB 2: REVERSE TARGET SCORE CALCULATOR
with tab2:
    st.subheader("How much do you need on your Entry Test?")
    target_agg = st.slider("Select Target Closing Merit (%)", min_value=60.0, max_value=92.0, value=79.0, step=0.5)

    # Calculate required test percentages
    req_nust = (target_agg - (inter_pct * 0.15) - (matric_pct * 0.10)) / 0.75
    req_fast = (target_agg - (inter_pct * 0.40) - (matric_pct * 0.10)) / 0.50
    req_itu = (target_agg - (inter_pct * 0.35) - (matric_pct * 0.15)) / 0.50
    req_uet = (target_agg - (inter_pct * 0.50) - (matric_pct * 0.17)) / 0.33
    req_giki = (target_agg - (inter_pct * 0.15)) / 0.85

    def format_req(req_pct, max_marks):
        if req_pct <= 0:
            return "Already cleared by board marks!"
        elif req_pct > 100:
            return f"Not reachable ({req_pct:.1f}% needed)"
        else:
            marks = (req_pct / 100) * max_marks
            return f"**{marks:.1f} / {max_marks}** ({req_pct:.1f}%)"

    st.write(f"🏛️ **NUST NET (out of 200):** {format_req(req_nust, 200)}")
    st.write(f"💻 **FAST NU Test (out of 100):** {format_req(req_fast, 100)}")
    st.write(f"📘 **COMSATS NTS NAT (out of 100):** {format_req(req_fast, 100)}")
    st.write(f"🔬 **ITU Lahore Test (out of 100):** {format_req(req_itu, 100)}")
    st.write(f"⚙️ **UET ECAT (out of 400):** {format_req(req_uet, 400)}")
    st.write(f"🏔️ **GIKI Test (out of 200):** {format_req(req_giki, 200)}")

st.divider()
st.caption("Have feedback or want to suggest a university formula? Email **khoonlahore.support@gmail.com**")
