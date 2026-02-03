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

# Initialize session state for dark mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Theme colors
if st.session_state.dark_mode:
    bg_color = "#1e1e1e"
    secondary_bg = "#2d2d2d"
    text_color = "#e0e0e0"
    header_color = "#ffffff"
    card_bg = "#2d2d2d"
    plot_bg = "#2d2d2d"
else:
    bg_color = "#ffffff"
    secondary_bg = "#f8f9fa"
    text_color = "#2c3e50"
    header_color = "#1a1a1a"
    card_bg = "#ffffff"
    plot_bg = "white"

# Apply theme
st.markdown(f"""
<style>
    .stApp {{ background-color: {bg_color}; color: {text_color}; }}
    .stMarkdown, p, span, label {{ color: {text_color} !important; }}
    h1, h2, h3 {{ color: {header_color} !important; }}
    .citation {{
        background: {secondary_bg};
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #3498db;
        margin: 10px 0;
    }}
    .citation a {{ color: #3498db !important; }}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🔬 Research Navigation")
    
    # DARK MODE TOGGLE - Make it prominent
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("### Theme")
    with col2:
        mode_emoji = "🌙" if st.session_state.dark_mode else "☀️"
        
    if st.button(f"{mode_emoji} {'Dark' if not st.session_state.dark_mode else 'Light'} Mode", 
                 use_container_width=True, 
                 type="primary"):
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
    st.markdown("### Quick Stats")
    st.metric("Total Sources", "76", delta="Peer-reviewed")
    st.metric("Largest Study", "46M", delta="participants")
    st.metric("Follow-up Period", "4 years", delta="France study")

# Main content
if page == "📊 Dashboard Overview":
    st.title("COVID-19 mRNA Vaccine Research Dashboard")
    st.markdown("### Comprehensive Evidence-Based Analysis")
    
    st.markdown(f"""
    <div class="citation">
    📚 <strong>Data Sources:</strong> This dashboard compiles data from 76 peer-reviewed sources including
    studies from NEJM, JAMA, Nature, The Lancet, and CDC/FDA surveillance systems.
    </div>
    """, unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Pfizer Efficacy", "95.0%", delta="90.3-97.6% CI")
        st.markdown('<div class="citation">Source: <a href="https://www.nejm.org/doi/full/10.1056/NEJMoa2034577" target="_blank">Polack et al., NEJM 2020</a></div>', unsafe_allow_html=True)
    
    with col2:
        st.metric("Moderna Efficacy", "94.1%", delta="89.3-96.8% CI")
        st.markdown('<div class="citation">Source: <a href="https://www.nejm.org/doi/full/10.1056/NEJMoa2035389" target="_blank">Baden et al., NEJM 2021</a></div>', unsafe_allow_html=True)
    
    with col3:
        st.metric("Myocarditis Risk", "1 in 32K", delta="5.6× lower vs infection")
        st.markdown('<div class="citation">Source: <a href="https://www.cdc.gov/mmwr/volumes/71/wr/mm7114e1.htm" target="_blank">CDC MMWR 2022</a></div>', unsafe_allow_html=True)
    
    with col4:
        st.metric("4-Year Mortality", "No Excess", delta="28M participants")
        st.markdown('<div class="citation">Source: <a href="https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2842305" target="_blank">JAMA 2025</a></div>', unsafe_allow_html=True)
    
    with col5:
        st.metric("CV Protection", "10% Lower", delta="Heart attacks/strokes")
        st.markdown('<div class="citation">Source: <a href="https://www.nature.com/articles/s41467-024-49634-x" target="_blank">Nature Comm 2024</a></div>', unsafe_allow_html=True)
    
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
        
        fig = px.bar(efficacy_data, x='Vaccine', y='Efficacy', color='Outcome',
                    barmode='group', title="Efficacy Against COVID-19")
        fig.update_layout(plot_bgcolor=plot_bg, paper_bgcolor=plot_bg,
                         font=dict(color=text_color))
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Myocarditis Risk by Age (Males)")
        myocarditis_data = pd.DataFrame({
            'Age': ['12-17', '18-29', '30-39', '40+'],
            'Cases per 100K': [35.9, 25.0, 12.0, 3.5]
        })
        
        fig = px.line(myocarditis_data, x='Age', y='Cases per 100K',
                     markers=True, title="Age-Stratified Risk")
        fig.update_traces(line_color='#e74c3c', line_width=3, marker_size=12)
        fig.update_layout(plot_bgcolor=plot_bg, paper_bgcolor=plot_bg,
                         font=dict(color=text_color))
        st.plotly_chart(fig, use_container_width=True)

elif page == "📚 Research Documents":
    st.title("📚 Research Documents")
    st.markdown("### Complete Research Database")
    
    st.info("Click on any document below to view the full content")
    
    documents = {
        "📖 README - Getting Started": "README.md",
        "🔬 Main Research Database (35,000+ words)": "COVID_Vaccine_Research_Database.md",
        "📊 Statistical Analysis Summary": "Statistical_Analysis_Summary.md",
        "🔍 Research Methodology Guide": "Research_Methodology_Guide.md",
        "📚 Annotated Bibliography (76 Sources)": "Annotated_Bibliography.md"
    }
    
    selected_doc = st.selectbox("Select a document to view:", list(documents.keys()))
    
    st.markdown("---")
    
    filename = documents[selected_doc]
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Download button
        st.download_button(
            label="📥 Download this document",
            data=content,
            file_name=filename,
            mime="text/markdown"
        )
        
        st.markdown("---")
        
        # Display content
        st.markdown(content)
        
    except FileNotFoundError:
        st.error(f"❌ Document '{filename}' not found. This may be a deployment issue.")
        st.info("💡 The documents are available in the GitHub repository: https://github.com/mobiusframeworks/covid-vaccine-research")
    except Exception as e:
        st.error(f"Error loading document: {str(e)}")

elif page == "📖 Citations & Sources":
    st.title("📖 Citations & Sources")
    st.markdown("### Complete Bibliography of 76 Peer-Reviewed Sources")
    
    st.markdown("""
    All data presented in this dashboard is sourced from peer-reviewed scientific literature,
    government regulatory agencies (FDA, CDC, EMA), and official public health databases.
    """)
    
    st.markdown("---")
    
    with st.expander("🔬 **Major Clinical Trials (Phase III)**", expanded=True):
        st.markdown("""
        1. **Polack FP, Thomas SJ, Kitchin N, et al.** Safety and Efficacy of the BNT162b2 mRNA Covid-19 Vaccine.
           *New England Journal of Medicine*. 2020;383(27):2603-2615.
           [https://www.nejm.org/doi/full/10.1056/NEJMoa2034577](https://www.nejm.org/doi/full/10.1056/NEJMoa2034577)

        2. **Baden LR, El Sahly HM, Essink B, et al.** Efficacy and Safety of the mRNA-1273 SARS-CoV-2 Vaccine.
           *New England Journal of Medicine*. 2021;384(5):403-416.
           [https://www.nejm.org/doi/full/10.1056/NEJMoa2035389](https://www.nejm.org/doi/full/10.1056/NEJMoa2035389)
        """)
    
    with st.expander("📊 **Large Population Studies**", expanded=True):
        st.markdown("""
        3. **Zureik M, et al.** COVID-19 mRNA Vaccination and 4-Year All-Cause Mortality (28M participants).
           *JAMA Network Open*. 2025;8(12):e2542305.
           [https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2842305](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2842305)

        4. **Hippisley-Cox J, et al.** Cardiovascular safety study (46M adults in England).
           *Nature Communications*. 2024;15:4963.
           [https://www.nature.com/articles/s41467-024-49634-x](https://www.nature.com/articles/s41467-024-49634-x)

        5. **Oster ME, et al.** Cardiac Complications After SARS-CoV-2 Infection and mRNA Vaccination (15M persons).
           *CDC MMWR*. 2022;71(14):477-482.
           [https://www.cdc.gov/mmwr/volumes/71/wr/mm7114e1.htm](https://www.cdc.gov/mmwr/volumes/71/wr/mm7114e1.htm)
        """)
    
    with st.expander("🫀 **Myocarditis & Cardiovascular Effects**", expanded=True):
        st.markdown("""
        6. **Witberg G, et al.** Myocarditis after Covid-19 Vaccination in a Large Health Care Organization.
           *NEJM*. 2021;385:2132-2139.
           [https://www.nejm.org/doi/full/10.1056/NEJMoa2110737](https://www.nejm.org/doi/full/10.1056/NEJMoa2110737)

        7. **Patone M, et al.** Risks of myocarditis, pericarditis, and cardiac arrhythmias.
           *Nature Medicine*. 2022;28:410–422.
           [https://www.nature.com/articles/s41591-021-01630-0](https://www.nature.com/articles/s41591-021-01630-0)

        8. **Stanford Medicine.** Why mRNA vaccine can cause myocarditis (mechanism identified).
           *Science Translational Medicine*. December 2025.
           [https://med.stanford.edu/news/all-news/2025/12/myocarditis-vaccine-covid.html](https://med.stanford.edu/news/all-news/2025/12/myocarditis-vaccine-covid.html)
        """)
    
    with st.expander("📈 **Safety Surveillance & VAERS**"):
        st.markdown("""
        9. **CDC/FDA.** Vaccine Adverse Event Reporting System (VAERS).
           [https://vaers.hhs.gov/](https://vaers.hhs.gov/)

        10. **Shimabukuro TT, et al.** Safety of mRNA vaccines (first 6 months, 298M doses).
            *Lancet Infectious Diseases*. 2022;22(6):802-812.
        """)
    
    st.markdown("---")
    st.markdown("### 📥 Download Complete Bibliography")
    
    try:
        with open("Annotated_Bibliography.md", 'r') as f:
            bib_content = f.read()
        st.download_button(
            label="📥 Download Full Bibliography (76 sources)",
            data=bib_content,
            file_name="Complete_Bibliography.md",
            mime="text/markdown"
        )
    except:
        st.info("💡 Full bibliography available at: https://github.com/mobiusframeworks/covid-vaccine-research")

else:
    st.title(f"{page}")
    st.info("This page is under construction. Please check back soon!")

# Footer
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; padding: 20px; background-color: {secondary_bg}; border-radius: 10px;'>
    <p style='font-size: 18px; font-weight: bold; color: {header_color};'>
    COVID-19 mRNA Vaccine Research Dashboard
    </p>
    <p style='color: {text_color};'>
    Compiled from 76 peer-reviewed sources | Updated: January 30, 2026<br>
    Data from over 100 million participants across multiple countries
    </p>
    <p style='font-size: 12px; color: {text_color}; margin-top: 10px;'>
    <strong>Disclaimer:</strong> For educational purposes. Not medical advice. Consult healthcare providers.
    </p>
</div>
""", unsafe_allow_html=True)
