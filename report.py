from fpdf import FPDF
from PIL import Image, ImageEnhance
import pandas as pd

# Create a sample DataFrame with patient data
data = {
    'Age': [30],
    'Gender': ['Male'],
    'Height (cm)': [175],
    'Weight (kg)': [70],
    'BMI': [22.9],
    'Physical Activity Level': ['Moderate'],
    'Dietary Habits': ['Balanced'],
    'Sleep Patterns': ['7 hours'],
    'Stress Level': ['Moderate'],
    'Past Surgeries': ['None'],
    'Chronic Conditions': ['None'],
    'Family History': ['Hypertension'],
    'Allergies': ['None'],
    'Medication Use': ['None'],
    'Alcohol Consumption': ['Occasionally'],
    'Tobacco Use': ['No'],
    'Blood Pressure (mmHg)': ['120/80'],
    'Glucose (mg/dL)': [90],
    'Heart Rate (bpm)': [72],
    'Temperature (°C)': [36.6],
    'Blood Test Parameters': ['CBC, BMP, Glucose'],
    'Blood Test Date': ['2024-09-15'],
    'Risk Score': [0]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Step 1: Create a PDF and add the watermark image at the top
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add the transparent logo as a watermark at the top
pdf.image('img.jpg', x=1, y=1, w=70, h=31)  # Adjust 'x', 'y', 'w', 'h' as needed

# Title of the PDF centered
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Patient Medical Report", ln=True, align='C')  # Width 0 ensures the cell takes the entire page width
pdf.ln(10)  # Line break

# Add the data to the PDF in a tabular format with left padding
pdf.set_font("Arial", size=12)
for col, value in df.iloc[0].items():
    pdf.set_x(15)  # Set left padding of 15px
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(80, 10, f"{col}:", border=1)
    pdf.set_font("Arial", size=12)
    pdf.cell(100, 10, f"{value}", border=1, ln=True)

# Save PDF
pdf_output = "medical_report_with_centered_title.pdf"
pdf.output(pdf_output)

print(f"PDF created: {pdf_output}")
