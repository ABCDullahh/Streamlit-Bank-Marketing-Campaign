import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import plotly.graph_objects as go
import time
from datetime import datetime

st.set_page_config(
    page_title="Bank Marketing Campaign Prediction",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS ya ges yak
st.markdown("""
    <style>
    /* Main Styles */
    .main {
        background-color: #f5f7f9;
    }
    
    /* Custom Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
    
    /* Header Styles */
    .big-font {
        font-family: 'Poppins', sans-serif;
        font-size: 40px !important;
        font-weight: 700;
        background: linear-gradient(45deg, #1E88E5, #1565C0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 20px 0;
        margin-bottom: 0;
    }
    
    .subtitle {
        font-family: 'Poppins', sans-serif;
        font-size: 20px !important;
        color: #424242;
        text-align: center;
        margin-bottom: 2rem;
        opacity: 0.8;
    }
    
    /* Section Headers */
    .section-header {
        font-family: 'Poppins', sans-serif;
        font-size: 26px !important;
        font-weight: 600;
        color: #1565C0;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding: 10px;
        border-left: 5px solid #1E88E5;
        background: linear-gradient(90deg, rgba(30,136,229,0.1) 0%, rgba(255,255,255,0) 100%);
    }
    
    /* Cards */
    .stat-card {
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
        background: white;
        transition: transform 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #1E88E5, #1565C0);
        color: white;
        width: 100%;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(30,136,229,0.3);
    }
    
    /* Prediction Results */
    .prediction-box {
        padding: 25px;
        border-radius: 15px;
        margin: 15px 0;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .prediction-box:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    
    .success {
        background: linear-gradient(45deg, #66BB6A, #43A047);
        color: white;
    }
    
    .failure {
        background: linear-gradient(45deg, #EF5350, #D32F2F);
        color: white;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div {
        background-color: #1E88E5;
    }
    
    /* Metrics */
    .metric-card {
        background: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Sliders */
    .stSlider {
        padding-top: 10px;
        padding-bottom: 10px;
    }
    
    /* Selectbox */
    .stSelectbox {
        padding-top: 10px;
        padding-bottom: 10px;
    }
    
    /* Footer */
    .footer {
        background: white;
        padding: 20px;
        text-align: center;
        border-radius: 10px;
        margin-top: 30px;
        box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Loading Animation */
    .loading {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid rgba(255,255,255,.3);
        border-radius: 50%;
        border-top-color: #fff;
        animation: spin 1s ease-in-out infinite;
    }
    
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    
    /* Custom Input Styling */
    .stTextInput>div>div>input {
        border-radius: 8px;
        padding: 10px;
        border: 2px solid #e0e0e0;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #1E88E5;
        box-shadow: 0 0 0 2px rgba(30,136,229,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 📊 Dashboard Info")
    st.info("This dashboard predicts the likelihood of a customer subscribing to a term deposit based on various features.")
    
    st.markdown("### 🎯 Model Performance")
    st.success("F2 Score on Test Data: 0.5651")
    
    st.markdown("### ⚙️ Last Updated")
    st.write(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    st.write("Model Version: 1.0.0")
    
    st.markdown("### 📚 Resources")
    st.markdown("""
        <style>
        .resource-links {
            display: flex;
            align-items: center;
            margin-bottom: 8px;
        }
        .resource-links img {
            margin-right: 8px;
            width: 18px;
        }
        </style>
        <div class="resource-links">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub">
            <a href="https://github.com/ABCDullahh/Purwadhika-Final-Project-Bank-Marketing-Campaign" target="_blank">Documentation</a>
        </div>
        <div class="resource-links">
            <img src="https://cdn4.iconfinder.com/data/icons/social-media-logos-6/512/112-gmail_email_mail-512.png" alt="Email">
            <a href="mailto:faizal2jz@gmail.com">Report Bug</a>
        </div>
    """, unsafe_allow_html=True)


st.markdown('<p class="big-font">🏦 Bank Marketing Campaign Prediction</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Advanced Analytics for Customer Subscription Prediction</p>', unsafe_allow_html=True)

@st.cache_resource
def load_model():
    with open("Bank Marketing Campaign Deposit Prediction - LGBM Classifier.pkl", "rb") as file:
        return pickle.load(file)

with st.spinner('Loading model...'):
    model = load_model()
    time.sleep(1)
st.success('Model loaded successfully!')

job_category_map = {
    'admin.': 'white_collar', 
    'management': 'white_collar', 
    'entrepreneur': 'white_collar',
    'blue-collar': 'blue_collar', 
    'technician': 'blue_collar',
    'services': 'service', 
    'housemaid': 'service',
    'self-employed': 'self_employed',
    'retired': 'inactive', 
    'student': 'inactive', 
    'unemployed': 'inactive',
    'unknown': 'unknown'
}

tab1, tab2, tab3 = st.tabs(["🎯 Single Prediction", "📊 Bulk Prediction", "🔍 Feature Importance"])

with tab1:
    st.markdown('<p class="section-header">📊 Customer Information</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 👤 Personal Details")
        with st.container():
            age = st.slider("Age", min_value=17, max_value=98, value=40)
            education = st.selectbox("Education", ["university.degree", "professional.course", "basic.6y", "unknown", 
                                                 "basic.9y", "basic.4y", "high.school", "illiterate"])
            job = st.selectbox("Job", list(job_category_map.keys()))
            marital = st.selectbox("Marital Status", ["single", "married", "divorced", "unknown"])

    with col2:
        st.markdown("### 💰 Financial Profile")
        with st.container():
            default = st.selectbox("Has Credit in Default?", ["no", "yes", "unknown"])
            housing = st.selectbox("Has Housing Loan?", ["no", "yes", "unknown"])
            loan = st.selectbox("Has Personal Loan?", ["no", "yes", "unknown"])
            cons_price_idx = st.slider("Consumer Price Index", min_value=92.201, max_value=94.767, value=93.576, 
                                     format="%.3f")
            cons_conf_idx = st.slider("Consumer Confidence Index", min_value=-50.8, max_value=-26.9, value=-40.507, 
                                    format="%.3f")

    with col3:
        st.markdown("### 📞 Campaign Details")
        with st.container():
            campaign = st.slider("Campaign Contacts", min_value=1, max_value=56, value=2)
            previous = st.slider("Previous Contacts", min_value=0, max_value=7, value=1)
            pdays = st.slider("Days Since Last Contact", min_value=0, max_value=999, value=999)
            contact = st.selectbox("Contact Method", ["cellular", "telephone"])
            month = st.selectbox("Month", ["mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])
            day_of_week = st.selectbox("Day of Week", ["mon", "tue", "wed", "thu", "fri"])
            poutcome = st.selectbox("Previous Outcome", ["nonexistent", "failure", "success"])

    st.markdown('<p class="section-header">📈 Economic Indicators</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        euribor3m = st.slider("Euribor 3 Month Rate", min_value=0.634, max_value=5.045, value=3.604, format="%.3f")
        
        fig_euribor = go.Figure()
        fig_euribor.add_trace(go.Indicator(
            mode="gauge+number",
            value=euribor3m,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Euribor 3M Rate"},
            gauge={'axis': {'range': [0, 5.045]},
                   'bar': {'color': "#1E88E5"},
                   'steps': [
                       {'range': [0, 2], 'color': "#C8E6C9"},
                       {'range': [2, 4], 'color': "#FFECB3"},
                       {'range': [4, 5.045], 'color': "#FFCDD2"}
                   ]}))
        st.plotly_chart(fig_euribor, use_container_width=True)
        
    with col2:
        emp_var_rate = st.slider("Employment Variation Rate", min_value=-3.4, max_value=1.4, value=0.07, format="%.2f")
        
        # Visualisasi Employment Rate trend
        fig_emp = go.Figure()
        fig_emp.add_trace(go.Indicator(
            mode="gauge+number",
            value=emp_var_rate,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Employment Variation Rate"},
            gauge={'axis': {'range': [-3.4, 1.4]},
                   'bar': {'color': "#1E88E5"},
                   'steps': [
                       {'range': [-3.4, -1.5], 'color': "#FFCDD2"},
                       {'range': [-1.5, 0], 'color': "#FFECB3"},
                       {'range': [0, 1.4], 'color': "#C8E6C9"}
                   ]}))
        st.plotly_chart(fig_emp, use_container_width=True)

    nremployed = st.slider("Number of Employees (thousands)", min_value=4500.0, max_value=5200.0, value=5099.1, 
                          format="%.1f")

    contact_ratio = previous / (campaign + previous) if (campaign + previous) != 0 else 0
    
    fig_ratio = go.Figure()
    fig_ratio.add_trace(go.Indicator(
        mode="gauge+number+delta",
        value=contact_ratio * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Contact Ratio", 'font': {'size': 24}},
        delta={'reference': 50},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#1E88E5"},
            'steps': [
                {'range': [0, 30], 'color': "#FFCDD2"},
                {'range': [30, 70], 'color': "#FFECB3"},
                {'range': [70, 100], 'color': "#C8E6C9"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 80
            }
        }
    ))
    st.plotly_chart(fig_ratio, use_container_width=True)

# Create input dataframe
    input_data = {
        'age': [age],
        'campaign': [campaign],
        'previous': [previous],
        'pdays': [pdays],
        'contact_ratio': [contact_ratio],
        'cons.price.idx': [cons_price_idx],
        'cons.conf.idx': [cons_conf_idx],
        'euribor3m': [euribor3m],
        'nr.employed': [nremployed],
        'emp.var.rate': [emp_var_rate],
        'education': [education],
        'month': [month],
        'marital': [marital],
        'default': [default],
        'housing': [housing],
        'loan': [loan],
        'contact': [contact],
        'day_of_week': [day_of_week],
        'poutcome': [poutcome],
        'job_category': [job_category_map.get(job, "unknown")]
    }

    input_df = pd.DataFrame(input_data)

    # Prediction button with animation
    if st.button("🔮 Generate Prediction", key="single_predict"):
        with st.spinner('Analyzing customer data...'):
            time.sleep(1)
            
# Make prediction
            prediction = model.predict(input_df)
            prediction_proba = model.predict_proba(input_df)[0][1]
            
            fig_prob = go.Figure()
            fig_prob.add_trace(go.Indicator(
                mode="gauge+number+delta",
                value=prediction_proba * 100,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Subscription Probability", 'font': {'size': 24}},
                delta={'reference': 50},
                gauge={
                    'axis': {'range': [0, 100], 'ticksuffix': "%"},
                    'bar': {'color': "#1E88E5" if prediction_proba >= 0.5 else "#EF5350"},
                    'steps': [
                        {'range': [0, 30], 'color': "#FFCDD2"},
                        {'range': [30, 70], 'color': "#FFECB3"},
                        {'range': [70, 100], 'color': "#C8E6C9"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 50
                    }
                }
            ))
            
# Display prediction results
            result_class = "success" if prediction[0] == 1 else "failure"
            result_text = "LIKELY TO SUBSCRIBE" if prediction[0] == 1 else "UNLIKELY TO SUBSCRIBE"
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.plotly_chart(fig_prob, use_container_width=True)
            
            with col2:
                st.markdown(f"""
                    <div class='prediction-box {result_class}'>
                        <h2>Prediction Result</h2>
                        <h1>{result_text}</h1>
                        <p style='font-size: 1.2em;'>Confidence: {prediction_proba:.2%}</p>
                        <p>Based on the provided customer information</p>
                    </div>
                """, unsafe_allow_html=True)


with tab2:
    st.markdown('<p class="section-header">📁 Bulk Prediction Analysis</p>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        try:
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i in range(100):
                progress_bar.progress(i + 1)
                status_text.text(f"Processing file... {i+1}%")
                time.sleep(0.01)
            
# Read file
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file, delimiter=';')
            else:
                df = pd.read_excel(uploaded_file)
            
            status_text.text("File processed successfully!")
            
            st.markdown("### 📊 Dataset Overview")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.markdown("""
                    <div class="stat-card">
                        <h3>Total Records</h3>
                        <p style="font-size: 24px; color: #1E88E5;">{:,}</p>
                    </div>
                """.format(len(df)), unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                    <div class="stat-card">
                        <h3>Features</h3>
                        <p style="font-size: 24px; color: #1E88E5;">{:,}</p>
                    </div>
                """.format(len(df.columns)), unsafe_allow_html=True)
            
            with col3:
                st.markdown("""
                    <div class="stat-card">
                        <h3>Missing Values</h3>
                        <p style="font-size: 24px; color: #EF5350;">{:,}</p>
                    </div>
                """.format(df.isnull().sum().sum()), unsafe_allow_html=True)
            
            with col4:
                st.markdown("""
                    <div class="stat-card">
                        <h3>Duplicate Rows</h3>
                        <p style="font-size: 24px; color: #66BB6A;">{:,}</p>
                    </div>
                """.format(df.duplicated().sum()), unsafe_allow_html=True)
            
            tab_preview, tab_stats = st.tabs(["Data Preview", "Statistics"])
            
            with tab_preview:
                st.dataframe(df.head(), use_container_width=True)
            
            with tab_stats:
                st.write(df.describe())
            
            if st.button("🚀 Run Bulk Prediction", key="bulk_predict"):
                with st.spinner('Processing predictions...'):
                    df['contact_ratio'] = df.apply(
                        lambda row: row['previous'] / (row['campaign'] + row['previous'])
                        if (row['campaign'] + row['previous']) != 0 else 0,
                        axis=1
                    )
                    
# Map job categories
                    df['job_category'] = df['job'].map(job_category_map).fillna('unknown')
                    
                    predictions = model.predict(df)
                    prediction_proba = model.predict_proba(df)[:, 1]
                    
                    df['Prediction'] = predictions
                    df['Subscription_Probability'] = prediction_proba
                    
                    
                    st.markdown("### 📈 Prediction Results")
# Summary metrics
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.markdown("""
                            <div class="metric-card">
                                <h4>Predicted Subscribers</h4>
                                <p style="font-size: 24px; color: #1E88E5;">{:,}</p>
                            </div>
                        """.format(sum(predictions)), unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown("""
                            <div class="metric-card">
                                <h4>Conversion Rate</h4>
                                <p style="font-size: 24px; color: #1E88E5;">{:.2%}</p>
                            </div>
                        """.format(sum(predictions)/len(predictions)), unsafe_allow_html=True)
                    
                    with col3:
                        st.markdown("""
                            <div class="metric-card">
                                <h4>Average Probability</h4>
                                <p style="font-size: 24px; color: #1E88E5;">{:.2%}</p>
                            </div>
                        """.format(prediction_proba.mean()), unsafe_allow_html=True)
                    
# Probability distribution plot
                    fig_dist = px.histogram(
                        df,
                        x='Subscription_Probability',
                        nbins=50,
                        title='Distribution of Subscription Probabilities',
                        labels={'Subscription_Probability': 'Probability'},
                        color_discrete_sequence=['#1E88E5']
                    )
                    fig_dist.update_layout(showlegend=False)
                    st.plotly_chart(fig_dist, use_container_width=True)
                    
# Results table
                    st.markdown("### 📋 Detailed Results")
                    st.dataframe(
                        df.sort_values('Subscription_Probability', ascending=False),
                        use_container_width=True
                    )
                    
# Download results
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Results",
                        data=csv,
                        file_name="prediction_results.csv",
                        mime="text/csv"
                    )
                    
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")





with tab3:
    st.markdown('<p class="section-header">🔍 Feature Importance Analysis</p>', unsafe_allow_html=True)
    feature_data = pd.DataFrame({
        'Feature': [
            'num__euribor3m', 'num__age', 'num__campaign', 'ord__education',
            'num__cons.price.idx', 'num__contact_ratio', 'num__cons.conf.idx',
            'onehot_cat__contact_telephone', 'onehot_cat__day_of_week_mon',
            'onehot_cat__marital_single', 'num__pdays', 'ord__month',
            'onehot_binary__job_category_1', 'onehot_cat__day_of_week_wed',
            'onehot_cat__default_unknown', 'onehot_cat__poutcome_success',
            'onehot_binary__job_category_2', 'onehot_binary__job_category_0',
            'onehot_cat__day_of_week_tue'
        ],
        'Importance': [
            2515, 2302, 1294, 1112, 822, 617, 462, 331, 236, 219, 
            198, 190, 190, 145, 139, 113, 97, 78, 40
        ]
    })




# Sort by importance
    feature_data = feature_data.sort_values('Importance', ascending=True)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=feature_data['Importance'],
        y=feature_data['Feature'],
        orientation='h',
        marker=dict(
            color=feature_data['Importance'],
            colorscale='Blues',
            line=dict(color='rgba(30,136,229,1.0)', width=2)
        ),
        text=feature_data['Importance'].round(0),
        textposition='auto',
    ))
    
    fig.update_layout(
        xaxis_title="Importance Score",
        yaxis_title="Feature",
        height=800,
        template="plotly_white",
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family="Poppins")
    )
    
    st.plotly_chart(fig, use_container_width=True)
    





    st.markdown("### **Rekomendasi Bisnis Berdasarkan Feature Importance**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### Strategi Targeting
        - Fokus pada nasabah usia matang
        - Segmentasi berdasarkan pendidikan
        - Personalisasi berdasarkan profil
        """)
    
    with col2:
        st.markdown("""
        #### Optimasi Kampanye
        - Timing berdasarkan indikator ekonomi
        - Frekuensi kontak yang optimal
        - Pemilihan channel komunikasi
        """)
    
    with col3:
        st.markdown("""
        #### Pengembangan Produk
        - Penyesuaian dengan kondisi pasar
        - Fitur berdasarkan segmen
        - Penawaran khusus berdasarkan profil
        """)




# Footer
st.markdown("""
    <div class="footer">
        <p>Made by</p>
        <p>Faizal Lutfi Yoga Triadi</p>
        <p>Taufiqurrahman</p>
    </div>
""", unsafe_allow_html=True)