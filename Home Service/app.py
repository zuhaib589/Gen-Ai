import streamlit as st
from urllib.parse import quote

# --- Streamlit Config ---
st.set_page_config(page_title="Pakistan Home Services", layout="wide")

# --- Custom Sidebar CSS ---
st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        background-color: #b30000;
        color: white;
    }
    .stSelectbox > div:hover {
        background-color: #ff6666 !important;
    }
    .css-1cpxqw2, .css-q8sbsg {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Language Selection ---
lang = st.sidebar.radio("Choose Language / زبان منتخب کریں", ["English", "اردو"])

# --- Category Selection ---
if lang == "اردو":
    st.sidebar.title("🔧 سروس منتخب کریں")
    category = st.sidebar.selectbox("آپ کو کس کی ضرورت ہے؟", [
        "پلمبر", "الیکٹریشن", "مالی", "پینٹر", "اے سی ٹیکنیشن", "کارپینٹر", "ڈرائیور", "کلینر", "دیگر"
    ])
else:
    st.sidebar.title("🛠️ Choose Worker Type")
    category = st.sidebar.selectbox("Select a category", [
        "Plumber", "Electrician", "Gardener", "Painter", "AC Technician", "Carpenter", "Driver", "Cleaner", "Other"
    ])

# --- Dummy Worker Database ---
workers_data = [
    {"name": "Ali Khan", "category": "Plumber", "city": "Lahore", "area": "Model Town", "phone": "03001234567", "rating": 4.5},
    {"name": "Ahmed Raza", "category": "Electrician", "city": "Lahore", "area": "DHA", "phone": "03009876543", "rating": 4.2},
    {"name": "Sanaullah", "category": "Gardener", "city": "Karachi", "area": "Gulshan-e-Iqbal", "phone": "03111234567", "rating": 4.8},
    {"name": "Babar Hussain", "category": "Driver", "city": "Islamabad", "area": "F-10", "phone": "03211234567", "rating": 4.3},
    {"name": "Farhan Mehmood", "category": "Cleaner", "city": "Faisalabad", "area": "D-Ground", "phone": "03027654321", "rating": 4.1},
    {"name": "Zahid Iqbal", "category": "Painter", "city": "Rawalpindi", "area": "Saddar", "phone": "03114567890", "rating": 4.6},
    {"name": "Imran Haider", "category": "Carpenter", "city": "Multan", "area": "Cantt", "phone": "03018906743", "rating": 4.0},
    {"name": "Javed Anwar", "category": "Electrician", "city": "Peshawar", "area": "Hayatabad", "phone": "03339876542", "rating": 4.3},
    {"name": "Bilal Ashraf", "category": "AC Technician", "city": "Quetta", "area": "Satellite Town", "phone": "03455678912", "rating": 4.7},
    {"name": "Shahid Nazir", "category": "Plumber", "city": "Lahore", "area": "Johar Town", "phone": "03011239876", "rating": 4.4},
    {"name": "Rizwan Latif", "category": "Gardener", "city": "Islamabad", "area": "G-11", "phone": "03123450987", "rating": 4.6},
    {"name": "Naeem Ahmed", "category": "Cleaner", "city": "Karachi", "area": "Nazimabad", "phone": "03033455678", "rating": 4.0},
    {"name": "Usman Tariq", "category": "Painter", "city": "Lahore", "area": "Iqbal Town", "phone": "03457890234", "rating": 4.9},
    {"name": "Wasim Bhatti", "category": "Carpenter", "city": "Rawalpindi", "area": "Peshawar Road", "phone": "03332345678", "rating": 4.2},
    {"name": "Kashif Jameel", "category": "Driver", "city": "Faisalabad", "area": "Jinnah Colony", "phone": "03114543210", "rating": 4.1},
    {"name": "Adnan Saeed", "category": "AC Technician", "city": "Multan", "area": "Shah Rukn-e-Alam", "phone": "03215439876", "rating": 4.5},
    {"name": "Yasir Nawaz", "category": "Electrician", "city": "Peshawar", "area": "University Road", "phone": "03099887766", "rating": 4.4},
    {"name": "Tariq Bashir", "category": "Plumber", "city": "Quetta", "area": "Jinnah Town", "phone": "03110987654", "rating": 4.3},
    {"name": "Mubashir Ali", "category": "Driver", "city": "Lahore", "area": "Gulberg", "phone": "03217894567", "rating": 4.6},
    {"name": "Noman Qureshi", "category": "Cleaner", "city": "Islamabad", "area": "G-6", "phone": "03076543218", "rating": 4.2},
]


# --- UI Title ---
if lang == "اردو":
    st.title("🏠 پاکستان ہوم سروسز")
    st.write("قابل اعتماد مقامی کاریگر تلاش کریں")
else:
    st.title("🏠 Pakistan Home Services")
    st.write("Find trusted local home workers across Pakistan")

# --- City & Area Input ---
cities = ["Lahore", "Karachi", "Islamabad", "Rawalpindi", "Faisalabad", "Multan", "Peshawar", "Quetta"]

if lang == "اردو":
    city = st.selectbox("شہر منتخب کریں", cities)
    area = st.text_input("علاقہ یا سب ایریا لکھیں")
else:
    city = st.selectbox("Select your city", cities)
    area = st.text_input("Enter your area or sub-address")

# --- Filter & Search ---
if st.button("🔍 Search Worker" if lang == "English" else "🔍 کاریگر تلاش کریں"):
    if city and area:
        # Filter matched workers
        matched = [
            worker for worker in workers_data
            if worker["category"].lower() == category.lower()
            and worker["city"] == city
            and area.lower() in worker["area"].lower()
        ]

        if matched:
            if lang == "اردو":
                st.success(f"{len(matched)} کاریگر {area}، {city} میں دستیاب ہیں:")
            else:
                st.success(f"Found {len(matched)} {category.lower()}(s) in {area}, {city}:")

            for worker in matched:
                st.markdown(f"### 👷 {worker['name']}")
                st.markdown(f"📍 **Area**: {worker['area']}")
                st.markdown(f"⭐ **Rating**: {worker['rating']}/5.0")

                # WhatsApp Contact
                msg = quote(f"Hello {worker['name']}, I need a {worker['category']} in {worker['area']}, {worker['city']}.")
                whatsapp_url = f"https://wa.me/92{worker['phone'][1:]}?text={msg}"
                st.markdown(f"[📞 Contact on WhatsApp]({whatsapp_url})")
                st.markdown("---")
        else:
            st.warning("No workers found. Try a nearby area or different category." if lang == "English" else "کوئی کاریگر نہیں ملا، قریبی علاقہ آزمائیں۔")
    else:
        st.warning("Please enter both city and area." if lang == "English" else "براہ کرم شہر اور علاقہ درج کریں۔")
