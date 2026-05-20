# Egyptian Used Car Market Analysis (August 2025)

## 📌 Project Overview
An end-to-end data analysis project focusing on the Egyptian used car market. The project aims to provide data-driven insights into car pricing, mileage impact, and brand popularity, helping buyers and sellers make informed decisions.

---

## 🛠️ Project Structure
The repository is organized cleanly and professionally into the following directories:
* **`data/`**: Contains the raw scraped dataset (`hatla2ee_cars_august_2025.csv`) and the fully cleaned dataset (`cleaned_data.xlsx`).
* **`jupyter_notebooks/`**: Detailed Python scripts covering Exploratory Data Analysis (EDA) and data visualization using Pandas, Seaborn, and Matplotlib.
* **`dashboard/`**: The interactive Power BI Dashboard file (`Dashboard.pbix`) containing the data model and visual reports.
* **`presentation/`**: Final project presentation slides (`PDF/PPTX`) and key visualization exports (`PNG`).

---

## 🧹 Data Cleaning & Preprocessing (Power Query)
Key data preprocessing and transformation steps were handled entirely within **Power Query** before visualization:
* Handled missing values and removed duplicates to ensure data integrity.
* Standardized and cleaned text columns (Brands, Models, Cities).
* Processed and extracted numerical features (e.g., transforming and separating exact price and mileage values).
* Filtered and managed statistical anomalies to ensure accurate reporting.

---

## 📊 Exploratory Data Analysis - EDA (Python)
Advanced data exploration was performed via **Python scripts (Visual Studio Code)** to uncover market behaviors:
* **Brand Dominance:** Analysis of the Top 15 most frequent car brands in the Egyptian market, highlighting consumer preference.
* **Price vs. Year:** Visualizing how vehicle manufacturing year heavily dictates the baseline price retention.
* **Price vs. Mileage:** Statistical correlation showing the exact degradation of car value relative to kilometers driven.

---

## 🖥️ Power BI Dashboard
The interactive dashboard includes:
* Overview KPI cards (Average Price, Total Cars Listed, Average Mileage).
* Dynamic filters by **Brand**, **City**, and **Year**.
* Advanced charts showcasing average pricing trends across the most popular models.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
