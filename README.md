# COVID-19 Dataset - Data Cleaning and Preprocessing

## Project Overview  
This project focuses on cleaning and preprocessing the **COVID-19** dataset provided by the **World Health Organization (WHO)**. The dataset includes global COVID-19 case and death reports by country. The primary goal of this project is to clean the data by addressing missing values, duplicates, and inconsistencies, preparing it for further analysis or predictive modeling. This preprocessing ensures that the data is accurate, consistent, and ready for use in deeper analyses, such as trend analysis or forecasting.

The project was built to understand and address the challenges of working with real-world data and showcase how data cleaning can provide more reliable insights.

---

## Key Features  

- **Data Inspection**: Carefully inspect the dataset to understand its structure, check for missing values, and confirm column types.
- **Missing Value Handling**: Identify and handle missing values using different techniques such as imputation or removal, depending on the nature of the data.
- **Duplicate Handling**: Detect and eliminate duplicate entries that could skew the analysis.
- **Data Consistency Checks**: Ensure the dataset contains no inconsistencies like invalid date formats, negative values, or unexpected null values.
- **Trend Visualizations**: Visualize trends such as the number of new cases, cumulative cases, new deaths, and cumulative deaths over time using line and bar plots.
- **Statistical Insights**: Analyze key statistical trends, regional differences, and the overall pandemic situation globally and locally.

---

## Dataset Information  

- **Source**: The dataset is sourced from the [WHO COVID-19 Dashboard](https://data.who.int/dashboards/covid19/cases?n=c).
- **Columns**:
  - `Date_reported`: The date when the data was reported.
  - `Country_code`: A code representing the country.
  - `Country`: The name of the country reporting the data.
  - `WHO_region`: The region where the country is located (e.g., Europe, Africa).
  - `New_cases`: The number of new COVID-19 cases reported on the specific day.
  - `Cumulative_cases`: The total number of reported COVID-19 cases up to the reported day.
  - `New_deaths`: The number of new deaths reported due to COVID-19 on the specific day.
  - `Cumulative_deaths`: The total number of deaths reported due to COVID-19 up to the reported day.

---

## Data Cleaning and Preprocessing Steps  

1. **Loading the Dataset**: The data is loaded using **pandas**, which provides powerful data manipulation capabilities.
2. **Inspecting the Data**:  
   - I printed the first and last five rows to ensure the data is loaded correctly.
   - Used `df.info()` to check data types and identify any missing or null values.
   - Checked for the distribution of numerical features using `df.describe()`.
3. **Handling Missing Values**:  
   - Identified columns with missing values using `df.isnull().sum()` and handled them by either removing rows with missing values or applying imputation.
4. **Removing Duplicates**:  
   - Checked the dataset for duplicate rows and used `df.drop_duplicates()` to remove them.
5. **Ensuring Data Consistency**:  
   - Ensured the date column (`Date_reported`) followed a standard format and no invalid values existed.
6. **Data Transformation and Normalization**:  
   - Transformed certain columns (like `Date_reported`) into the correct formats.
7. **Data Visualizations**:  
   - Created visualizations to explore trends in new cases and deaths over time.
   - Used **matplotlib** and **seaborn** for visualizing the distribution of cases and deaths, and to track global pandemic trends.
   - Examined trends for each **WHO region** to observe the differences in the pandemic's evolution globally.

---

## Report  
For a more detailed analysis of the dataset and the steps taken during data cleaning and preprocessing, please refer to  
👉 **[COVID19_Cleaning_Report.md](COVID19_Cleaning_Report.md)**.
