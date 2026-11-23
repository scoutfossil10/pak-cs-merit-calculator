import streamlit as st

st.set_page_config(page_title="Pakistani CS & Engineering Merit Calculator", page_icon="🎓")

# ------------------------------------------------------------
# 1. THE "PRICE LIST": all university numbers live here ONLY.
#    Each year, change numbers here and the whole app updates.
#    ALWAYS verify against the official prospectus.
# ------------------------------------------------------------
LAST_UPDATED = "Nov 2026"

UNIS = {
    "NUST": {
        "name": "NUST (NET)",
        "test": 0.75, "inter": 0.15, "matric": 0.10,
        "total": 200,
        "closing": "2026 SEECS CS closing: ~76.8–79%",
        "min_inter": None,
    },
    "FAST": {
        "name": "FAST-NUCES (NU Test)",
        "test": 0.50, "inter": 0.40, "matric": 0.10,
        "total": 100,
        "closing": "2026 LHR/ISB CS closing: ~73–75%",
        "min_inter": None,
    },
    "COMSATS": {
        "name": "COMSATS Lahore (NTS NAT)",
        "test": 0.50, "inter": 0.40, "matric": 0.10,
        "total": 100,
        "closing": "2026 LHR CS: ~85–86.5% | ISB: ~88%",
        "min_inter": None,
    },
    "ITU": {
        "name": "ITU Lahore (CS/AI Test)",
        "test": 0.50, "inter": 0.35, "matric": 0.15,
        "total": 60,
        "closing": "2026 CS closing: ~80.5%",
        "min_inter": None,
    },
    "UET": {
        "name": "UET Lahore (ECAT)",
        "test": 0.33, "inter": 0.50, "matric": 0.17,
        "total": 400,
        "closing": "2026 Main Campus A1 CS: ~79–82%",
        "min_inter": None,
    },
    "GIKI": {
        "name": "GIKI (GIKI Test)",
        "test": 0.85, "inter": 0.00, "matric": 0.15,
        "total": 200,
        "closing": "",
        "min_inter": 60,
    },
}


# ------------------------------------------------------------
# 2. TWO SMALL FUNCTIONS (like two calculators on the wall)
# ------------------------------------------------------------
def aggregate(key, test_pct, inter_pct, matric_pct):
    """Test % + Inter % + Matric % -> final aggregate %"""
    w = UNIS[key]
    return test_pct * w["test"] + inter_pct * w["inter"] + matric_pct * w["matric"]


def needed_test_pct(key, target, inter_pct, matric_pct):
    """Target aggregate -> the test % you need (same formula, reversed)"""
    w = UNIS[key]
    return (target - inter_pct * w["inter"] - matric_pct * w["matric"]) / w["test"]


# ------------------------------------------------------------
# 3. PAGE HEADER
# ------------------------------------------------------------
st.title("🎓 Pakistani CS & Engineering Merit Calculator")
st.caption("Built for FBISE & BISE Lahore FSc / ICS students | By a 2nd Year CS Applicant")
st.caption(
    "Uses Matric + Inter Part-1 marks, as most universities do for admission. "
    "Final admission may depend on passing Part-2. Check each prospectus."
)
st.warning(f"Unofficial estimate. Weights and closing merits last updated: {LAST_UPDATED}. "
           "Always verify with the official prospectus.")

# ------------------------------------------------------------
# 4. BOARD MARKS INPUT (defaults are 0, so nobody copies example marks)
# ------------------------------------------------------------
st.subheader("1. Enter Your Board Marks")
st.caption("Check your total marks on your result card, because totals can differ by board and group.")

col1, col2 = st.columns(2)
with col1:
    matric_obt = st.number_input("Matric Obtained Marks", min_value=0, max_value=1200, value=0)
    matric_tot = st.number_input("Matric Total Marks", min_value=1, max_value=1200, value=1100)
with col2:
    inter_obt = st.number_input("Inter Part-1 Obtained Marks", min_value=0, max_value=600, value=0)
    inter_tot = st.number_input("Inter Part-1 Total Marks", min_value=1, max_value=600, value=550)

if matric_obt > matric_tot or inter_obt > inter_tot:
    st.error("⚠️ Obtained marks cannot be greater than total marks.")
    st.stop()

if matric_obt == 0 or inter_obt == 0:
    st.info("👆 Enter your Matric and Inter Part-1 marks to begin.")
    st.stop()

matric_pct = matric_obt / matric_tot * 100
inter_pct = inter_obt / inter_tot * 100

st.info(f"**Your Board Percentages:** Matric: `{matric_pct:.2f}%` | Inter Part-1: `{inter_pct:.2f}%`")

tab1, tab2, tab3 = st.tabs(["Calculate My Aggregate", "Target Entry Test Score", "LUMS"])

# ------------------------------------------------------------
# TAB 1: AGGREGATE (live, no button needed)
# ------------------------------------------------------------
with tab1:
    st.subheader("2. Choose University & Enter Test Score")
    key = st.selectbox("University", list(UNIS.keys()), format_func=lambda k: UNIS[k]["name"])
    w = UNIS[key]

    st.caption(
        f"Formula: {w['test']*100:.0f}% Test + {w['inter']*100:.0f}% Inter + {w['matric']*100:.0f}% Matric "
        f"| Test is out of {w['total']}"
    )

    score_type = st.radio("Which score are you using?",
                          ["University entry test", "SAT (out of 1600)"],
                          horizontal=True, key=f"type_{key}")
    default_total = 1600.0 if score_type.startswith("SAT") else float(w["total"])
    if score_type.startswith("SAT"):
        st.caption("ℹ️ SAT uses the same weights as the entry test here. Some universities use a "
                   "different SAT formula or a separate merit list, so check the prospectus.")

    c1, c2 = st.columns(2)
    with c1:
        test_obt = st.number_input("Score Obtained", min_value=0.0, max_value=1600.0,
                                   value=0.0, key=f"obt_{key}_{score_type}")
    with c2:
        test_tot = st.number_input("Score Total", min_value=1.0, max_value=1600.0,
                                   value=default_total, key=f"tot_{key}_{score_type}")

    # Eligibility gate (like a guard at the door)
    if w["min_inter"] and inter_pct < w["min_inter"]:
        st.error(f"⚠️ {w['name']} asks for at least {w['min_inter']}% in Inter. Your Part-1 is {inter_pct:.1f}%.")

    if test_obt > test_tot:
        st.error("⚠️ Test obtained marks cannot exceed total marks.")
    elif test_obt > 0:
        test_pct = test_obt / test_tot * 100
        agg = aggregate(key, test_pct, inter_pct, matric_pct)
        st.metric("Estimated Aggregate", f"{agg:.2f}%")
        if w["closing"]:
            st.caption(f"{w['closing']} (last year's, not a guarantee)")
        st.caption("Unofficial estimate. Verify with the official prospectus.")
    else:
        st.info("Enter your test marks to see your aggregate.")

# ------------------------------------------------------------
# TAB 2: REVERSE CALCULATOR (what do I need on the test?)
# ------------------------------------------------------------
with tab2:
    st.subheader("How much do you need on your Entry Test?")
    target = st.slider("Target Closing Merit (%)", min_value=60.0, max_value=95.0, value=79.0, step=0.5)

    for k, u in UNIS.items():
        need_pct = needed_test_pct(k, target, inter_pct, matric_pct)
        if need_pct <= 0:
            result = "Already cleared by board marks!"
        elif need_pct > 100:
            result = f"Not reachable ({need_pct:.1f}% needed)"
        else:
            marks = need_pct / 100 * u["total"]
            sat_marks = need_pct / 100 * 1600
            result = (f"**{marks:.1f} / {u['total']}** ({need_pct:.1f}%) "
                      f"| SAT: **{sat_marks:.0f} / 1600**")
        line = f"**{u['name']}:** {result}"
        if u["closing"]:
            line += f" *({u['closing']})*"
        st.write(line)

    st.caption("Unofficial estimate. Closing merits change every year.")

# ------------------------------------------------------------
# TAB 3: LUMS (holistic, so no fixed formula)
# ------------------------------------------------------------
with tab3:
    st.subheader("LUMS (Holistic Admission)")
    st.info("LUMS has no fixed aggregate. It looks at Matric, Inter, SAT/LCAT, "
            "personal statement and activities together.")
    if matric_pct >= 75 and inter_pct >= 75:
        st.success("✅ Your marks meet the 75%+ minimum for SBASSE (CS & Engineering). "
                   "Competitive applicants usually aim for a strong SAT or LCAT score.")
    else:
        st.warning("⚠️ LUMS SBASSE asks for at least 75% in both Matric and Inter. Check the prospectus.")

st.divider()
st.link_button(
    "📝 Quick 10-Second Feedback / Suggest a University",
    "https://docs.google.com/forms/d/e/1FAIpQLSdg7M9FEw8RMs8JsJRf41t6LXIz1vaiFTfWeI8Djn6kFTpWqA/viewform?usp=dialog",
)
