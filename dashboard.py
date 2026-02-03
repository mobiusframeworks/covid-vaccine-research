import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="COVID-19 Vaccine Research Dashboard",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize dark mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Theme colors with HIGH CONTRAST
if st.session_state.dark_mode:
    bg_color = "#0e1117"
    secondary_bg = "#262730"
    text_color = "#fafafa"
    header_color = "#ffffff"
    card_bg = "#262730"
    border_color = "#4a4a4a"
    plot_bg = "#262730"
    plot_paper = "#0e1117"
else:
    bg_color = "#ffffff"
    secondary_bg = "#f0f2f6"
    text_color = "#262730"
    header_color = "#0e1117"
    card_bg = "#ffffff"
    border_color = "#e0e0e0"
    plot_bg = "white"
    plot_paper = "white"

# Enhanced CSS with proper contrast
st.markdown(f"""
<style>
    /* Main app */
    .stApp {{
        background-color: {bg_color} !important;
    }}

    /* All text elements */
    .stApp, .stMarkdown, p, span, label, div, li {{
        color: {text_color} !important;
    }}

    /* Headers */
    h1, h2, h3, h4, h5, h6 {{
        color: {header_color} !important;
    }}

    /* Metrics */
    [data-testid="stMetricValue"] {{
        color: {header_color} !important;
        font-size: 32px !important;
        font-weight: bold !important;
    }}

    [data-testid="stMetricLabel"] {{
        color: {text_color} !important;
        font-size: 16px !important;
    }}

    [data-testid="stMetricDelta"] {{
        color: {text_color} !important;
    }}

    /* Citation boxes */
    .citation {{
        background-color: {card_bg};
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #3498db;
        margin: 10px 0;
        color: {text_color} !important;
    }}

    .citation a {{
        color: #3498db !important;
        text-decoration: none;
    }}

    .citation a:hover {{
        text-decoration: underline;
    }}

    /* Info boxes */
    .stAlert {{
        background-color: {card_bg} !important;
        color: {text_color} !important;
    }}

    /* Expander */
    .streamlit-expanderHeader {{
        background-color: {card_bg} !important;
        color: {text_color} !important;
    }}

    /* Dataframes */
    .dataframe {{
        color: {text_color} !important;
    }}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🔬 Research Navigation")

    # Dark mode toggle
    mode_label = "🌙 Light Mode" if st.session_state.dark_mode else "☀️ Dark Mode"
    if st.button(mode_label, use_container_width=True, type="primary"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

    st.markdown("---")

    page = st.radio(
        "Select View:",
        ["📊 Dashboard Overview",
         "📈 Statistical Analysis",
         "🫀 Cardiovascular Data",
         "🧬 Efficacy & Safety",
         "📚 Research Documents",
         "📖 Citations & Sources"]
    )

    st.markdown("---")
    st.metric("Total Sources", "76", delta="Peer-reviewed")
    st.metric("Largest Study", "46M", delta="participants")
    st.metric("Follow-up Period", "4 years")

# DASHBOARD OVERVIEW
if page == "📊 Dashboard Overview":
    st.title("COVID-19 mRNA Vaccine Research Dashboard")
    st.subheader("Comprehensive Evidence-Based Analysis")

    st.markdown(f"""
    <div class="citation">
    📚 <strong>Data Sources:</strong> This dashboard compiles data from 76 peer-reviewed sources from
    NEJM, JAMA, Nature, The Lancet, and CDC/FDA surveillance systems.
    </div>
    """, unsafe_allow_html=True)

    # Metrics
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Pfizer Efficacy", "95.0%", "90.3-97.6% CI")
        st.markdown('<div class="citation"><a href="https://www.nejm.org/doi/full/10.1056/NEJMoa2034577" target="_blank">Polack et al., NEJM 2020</a></div>', unsafe_allow_html=True)

    with col2:
        st.metric("Moderna Efficacy", "94.1%", "89.3-96.8% CI")
        st.markdown('<div class="citation"><a href="https://www.nejm.org/doi/full/10.1056/NEJMoa2035389" target="_blank">Baden et al., NEJM 2021</a></div>', unsafe_allow_html=True)

    with col3:
        st.metric("Myocarditis Risk", "1 in 32K", "5.6× lower vs infection")
        st.markdown('<div class="citation"><a href="https://www.cdc.gov/mmwr/volumes/71/wr/mm7114e1.htm" target="_blank">CDC MMWR 2022</a></div>', unsafe_allow_html=True)

    with col4:
        st.metric("4-Year Mortality", "No Excess", "28M participants")
        st.markdown('<div class="citation"><a href="https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2842305" target="_blank">JAMA 2025</a></div>', unsafe_allow_html=True)

    with col5:
        st.metric("CV Protection", "10% Lower", "Heart attacks/strokes")
        st.markdown('<div class="citation"><a href="https://www.nature.com/articles/s41467-024-49634-x" target="_blank">Nature 2024</a></div>', unsafe_allow_html=True)

    st.markdown("---")

    # Charts
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Vaccine Efficacy Comparison")
        efficacy_data = pd.DataFrame({
            'Vaccine': ['Pfizer', 'Moderna', 'Pfizer', 'Moderna'],
            'Outcome': ['Symptomatic', 'Symptomatic', 'Severe', 'Severe'],
            'Efficacy': [95.0, 94.1, 95.0, 100.0]
        })
        fig = px.bar(efficacy_data, x='Vaccine', y='Efficacy', color='Outcome', barmode='group')
        fig.update_layout(plot_bgcolor=plot_bg, paper_bgcolor=plot_paper, font=dict(color=text_color))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Myocarditis Risk by Age (Males)")
        myocarditis_data = pd.DataFrame({
            'Age': ['12-17', '18-29', '30-39', '40+'],
            'Per 100K': [35.9, 25.0, 12.0, 3.5]
        })
        fig = px.line(myocarditis_data, x='Age', y='Per 100K', markers=True)
        fig.update_traces(line_color='#e74c3c', line_width=3, marker_size=12)
        fig.update_layout(plot_bgcolor=plot_bg, paper_bgcolor=plot_paper, font=dict(color=text_color))
        st.plotly_chart(fig, use_container_width=True)

# STATISTICAL ANALYSIS
elif page == "📈 Statistical Analysis":
    st.title("Statistical Analysis & Data")

    st.markdown('<div class="citation">📊 All statistics from peer-reviewed publications and CDC/FDA surveillance.</div>', unsafe_allow_html=True)

    st.subheader("Vaccine Efficacy Statistics")
    efficacy_df = pd.DataFrame({
        'Vaccine': ['Pfizer-BioNTech', 'Moderna'],
        'Efficacy (%)': [95.0, 94.1],
        'CI Lower': [90.3, 89.3],
        'CI Upper': [97.6, 96.8],
        'Sample Size': [43548, 30420],
        'Vaccine Cases': [8, 11],
        'Placebo Cases': [162, 185]
    })
    st.dataframe(efficacy_df, use_container_width=True)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Myocarditis Incidence")
        myoc_df = pd.DataFrame({
            'Population': ['Overall Dose 1', 'Overall Dose 2', 'Males ≤30'],
            'Incidence': ['1 in 140,000', '1 in 32,000', '1 in 16,750'],
            'Per 100,000': [0.71, 3.13, 5.97]
        })
        st.dataframe(myoc_df, use_container_width=True)

        st.markdown('<div class="citation"><a href="https://www.cdc.gov/mmwr/volumes/71/wr/mm7114e1.htm" target="_blank">CDC MMWR 2022</a></div>', unsafe_allow_html=True)

    with col2:
        st.subheader("Vaccination vs Infection Risk")
        comp_df = pd.DataFrame({
            'Event': ['Myocarditis', 'Cardiac Events'],
            'Vaccination': ['3.24 per 100K', '0.5%'],
            'Infection': ['18.28 per 100K', '0.7%'],
            'Relative': ['5.6× higher', '1.4× higher']
        })
        st.dataframe(comp_df, use_container_width=True)

    st.markdown("---")
    st.subheader("VAERS Safety Surveillance Data")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Doses", "663.8M", "Dec 2020-Dec 2022")
    with col2:
        st.metric("Adverse Reports", "900,522", "0.136% rate")
    with col3:
        st.metric("Serious Events", "9.2%", "83,408 reports")

# CARDIOVASCULAR DATA
elif page == "🫀 Cardiovascular Data":
    st.title("Cardiovascular Effects Analysis")

    st.subheader("Major Population Studies")
    studies_df = pd.DataFrame({
        'Study': ['England', 'US PCORnet', 'UK Population', 'National Cohort'],
        'Sample Size': ['46 million', '15.2 million', 'Population', '1.9 million'],
        'Key Finding': [
            '10% reduction arterial thromboses',
            'Higher cardiac events with infection',
            '7× higher myocarditis with infection',
            '0.5% MACE (vaccinated) vs 0.7% (unvaccinated)'
        ]
    })
    st.dataframe(studies_df, use_container_width=True)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Myocarditis by Age & Sex")
        age_groups = ['12-17', '18-29', '30-39', '40+']
        males = [35.9, 25.0, 12.0, 3.0]
        females = [10.9, 5.0, 2.0, 0.5]

        fig = go.Figure(data=[
            go.Bar(name='Males', x=age_groups, y=males, marker_color='#3498db'),
            go.Bar(name='Females', x=age_groups, y=females, marker_color='#e74c3c')
        ])
        fig.update_layout(
            title='Cases per 100,000 by Age and Sex',
            barmode='group',
            plot_bgcolor=plot_bg,
            paper_bgcolor=plot_paper,
            font=dict(color=text_color)
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Recovery Outcomes")
        outcomes_df = pd.DataFrame({
            'Outcome': ['Hospital Stay', 'No Treatment', 'Deaths', 'Readmission', 'Full Recovery'],
            'Result': ['3 days median', '65%', '0 (of 357)', '2%', 'Most patients']
        })
        st.dataframe(outcomes_df, use_container_width=True)

        st.markdown('<div class="citation"><a href="https://www.nejm.org/doi/full/10.1056/NEJMoa2110737" target="_blank">Witberg et al., NEJM 2021</a></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Treatment Protocols")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Acute Phase:**")
        st.markdown("- Hospital admission\n- Cardiac monitoring\n- Serial troponins\n- ECG, echo, MRI")
    with col2:
        st.markdown("**Medications:**")
        st.markdown("- NSAIDs\n- Colchicine\n- Corticosteroids\n- ACE inhibitors\n- Beta-blockers")
    with col3:
        st.markdown("**Activity:**")
        st.markdown("- Avoid strenuous exercise\n- 3-6 months restriction\n- Gradual return\n- Based on recovery")

# EFFICACY & SAFETY
elif page == "🧬 Efficacy & Safety":
    st.title("Efficacy & Safety Analysis")

    st.subheader("Phase III Clinical Trial Results")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Pfizer-BioNTech (BNT162b2)")
        st.markdown("""
        **Efficacy:** 95.0% (95% CI: 90.3-97.6%)

        **Trial Details:**
        - Participants: 43,548
        - Design: Two 30 µg doses, 21 days apart
        - Cases (vaccine): 8 (0.04%)
        - Cases (placebo): 162 (0.75%)

        **Publication:** NEJM 2020
        """)
        st.metric("Number Needed to Vaccinate", "141", "to prevent 1 case")
        st.markdown('<div class="citation"><a href="https://www.nejm.org/doi/full/10.1056/NEJMoa2034577" target="_blank">Full Study</a></div>', unsafe_allow_html=True)

    with col2:
        st.markdown("### Moderna (mRNA-1273)")
        st.markdown("""
        **Efficacy:** 94.1% (95% CI: 89.3-96.8%)

        **Trial Details:**
        - Participants: 30,420
        - Design: Two 100 µg doses, 28 days apart
        - Cases (vaccine): 11 (0 severe)
        - Cases (placebo): 185 (30 severe)

        **Publication:** NEJM 2021
        """)
        st.metric("Number Needed to Vaccinate", "87", "to prevent 1 case")
        st.markdown('<div class="citation"><a href="https://www.nejm.org/doi/full/10.1056/NEJMoa2035389" target="_blank">Full Study</a></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Long-Term Safety: France Study (28M, 4 years)")

    st.markdown("""
    **Study Design:**
    - Population: 28+ million adults aged 18-59
    - Follow-up: 4 years (2021-2025)
    - Publication: JAMA Network Open, December 2025

    **Key Findings:**
    - Hazard Ratio for All-Cause Mortality: 0.98 (95% CI: 0.96-1.01)
    - No increased deaths from cancer, heart disease, accidents, or any other cause
    - Vaccinated had equal or LOWER mortality rates across all categories

    **Conclusion:** "Causal link between mRNA vaccination and excess long-term mortality appears highly unlikely"
    """)

    st.markdown('<div class="citation"><a href="https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2842305" target="_blank">Zureik et al., JAMA 2025</a></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Risk-Benefit Calculator")

    age = st.slider("Your Age", 12, 85, 30)
    sex = st.radio("Sex", ["Male", "Female"], horizontal=True)

    if sex == "Male":
        if age < 30:
            myoc_risk, benefit_ratio = "1 in 16,750", 250
        elif age < 40:
            myoc_risk, benefit_ratio = "1 in 80,000", 500
        else:
            myoc_risk, benefit_ratio = "1 in 200,000", 1000
    else:
        myoc_risk, benefit_ratio = "1 in 100,000", 500 if age < 30 else 1000

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Your Myocarditis Risk", myoc_risk)
    with col2:
        st.metric("Benefit-Risk Ratio", f"{benefit_ratio}:1")
    with col3:
        st.metric("COVID Risk", "5.6× Higher", "myocarditis from infection")

# RESEARCH DOCUMENTS
elif page == "📚 Research Documents":
    st.title("📚 Research Documents")
    st.subheader("Complete Research Database")

    documents = {
        "📖 README - Getting Started": "README.md",
        "🔬 Main Research Database (35,000+ words)": "COVID_Vaccine_Research_Database.md",
        "📊 Statistical Analysis Summary": "Statistical_Analysis_Summary.md",
        "🔍 Research Methodology Guide": "Research_Methodology_Guide.md",
        "📚 Annotated Bibliography (76 Sources)": "Annotated_Bibliography.md"
    }

    selected = st.selectbox("Select document:", list(documents.keys()))
    filename = documents[selected]

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        st.download_button(
            "📥 Download Document",
            content,
            file_name=filename,
            mime="text/markdown"
        )

        st.markdown("---")
        st.markdown(content)
    except:
        st.error(f"Document not found: {filename}")
        st.info("💡 All documents available at: https://github.com/mobiusframeworks/covid-vaccine-research")

# CITATIONS & SOURCES
elif page == "📖 Citations & Sources":
    st.title("📖 Citations & Sources")
    st.subheader("Complete Bibliography of 76 Peer-Reviewed Sources")

    with st.expander("🔬 Major Clinical Trials", expanded=True):
        st.markdown("""
        1. **Polack FP, et al.** Safety and Efficacy of the BNT162b2 mRNA Covid-19 Vaccine.
           *NEJM*. 2020;383(27):2603-2615.
           [Link](https://www.nejm.org/doi/full/10.1056/NEJMoa2034577)

        2. **Baden LR, et al.** Efficacy and Safety of the mRNA-1273 SARS-CoV-2 Vaccine.
           *NEJM*. 2021;384(5):403-416.
           [Link](https://www.nejm.org/doi/full/10.1056/NEJMoa2035389)
        """)

    with st.expander("📊 Large Population Studies", expanded=True):
        st.markdown("""
        3. **Zureik M, et al.** COVID-19 mRNA Vaccination and 4-Year All-Cause Mortality.
           *JAMA Network Open*. 2025;8(12):e2542305.
           [Link](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2842305)

        4. **Hippisley-Cox J, et al.** Cardiovascular safety (46M adults).
           *Nature Communications*. 2024;15:4963.
           [Link](https://www.nature.com/articles/s41467-024-49634-x)

        5. **Oster ME, et al.** Cardiac Complications (15M persons).
           *CDC MMWR*. 2022;71(14):477-482.
           [Link](https://www.cdc.gov/mmwr/volumes/71/wr/mm7114e1.htm)
        """)

    with st.expander("🫀 Myocarditis Studies"):
        st.markdown("""
        6. **Witberg G, et al.** Myocarditis after Covid-19 Vaccination.
           *NEJM*. 2021;385:2132-2139.
           [Link](https://www.nejm.org/doi/full/10.1056/NEJMoa2110737)

        7. **Patone M, et al.** Risks of myocarditis and cardiac arrhythmias.
           *Nature Medicine*. 2022;28:410–422.
           [Link](https://www.nature.com/articles/s41591-021-01630-0)
        """)

    st.markdown("---")

    try:
        with open("Annotated_Bibliography.md", 'r') as f:
            bib = f.read()
        st.download_button(
            "📥 Download Complete Bibliography (76 sources)",
            bib,
            "Complete_Bibliography.md",
            "text/markdown"
        )
    except:
        st.info("Full bibliography: https://github.com/mobiusframeworks/covid-vaccine-research")

# Footer
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; padding: 20px; background-color: {secondary_bg}; border-radius: 10px;'>
    <h3 style='color: {header_color};'>COVID-19 mRNA Vaccine Research Dashboard</h3>
    <p style='color: {text_color};'>
    76 peer-reviewed sources | Updated January 2026<br>
    100+ million participants | 4-year follow-up data
    </p>
    <p style='font-size: 12px; color: {text_color};'>
    <strong>Disclaimer:</strong> Educational purposes only. Not medical advice. Consult healthcare providers.
    </p>
</div>
""", unsafe_allow_html=True)
