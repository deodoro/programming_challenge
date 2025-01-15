**Advanced Data Analysis and Visualization Challenge**

Welcome to the **NSDP Delay Analysis Challenge**. This exercise is designed to test your data analysis, Python programming, and Power BI visualization skills. You will work with an existing dataset that contains fictional information about delays in National Summary Data Page (NSDP) dissemination across various countries.

---

### **Objective**  
Your task is to process the dataset using Python, extract insights, and create an interactive Power BI report to visualize your findings.

---

### **Instructions**

#### **1. Dataset Description**  
You are provided with a single spreadsheet (`NSDP_Delays.xlsx`) that contains the following columns:
- `Country`: The ISO-3 code of the country.
- `Year`: The reporting year.
- `Type`: Either `Periodicity` or `Timeliness`.
- `Delay (days)`: The number of days by which the country delayed NSDP dissemination.
- `Last Update`: The timestamp of the last update to the record.

#### **2. Data Analysis Requirements**  
You are required to perform the following analyses using Python:

1. **Filter the Data**  
   - Only include rows where `Type` is **Timeliness**.
   - Exclude any records where `Delay (days)` is negative or missing.
   
2. **Compute Aggregates**  
   - Calculate the **average delay** per year for each country.
   - Identify the **top 5 countries** with the highest average delay across all years.

3. **Regional Insights**  
   - Compute the average delay by **region** for each year.
   - Identify which region has shown the most improvement in timeliness over the years.

4. **Outlier Detection**  
   - Identify any countries with delays that are statistical outliers (using a method of your choice, such as z-score or interquartile range).
   
5. **Export Results**  
   - Export the following outputs to CSV:
     - `Average_Delay_By_Country.csv`: Average delay per year for each country.
     - `Regional_Averages.csv`: Average delay by region and year.
     - `Outliers.csv`: List of identified outlier countries and their corresponding delay values.

#### **3. Power BI Visualization Requirements**  
Once the data is processed, create an interactive report using Power BI to present your findings. Your report should include:

1. **Yearly Delay Trends**  
   - A line chart showing the average delay per year for each country.
   
2. **Regional Performance Comparison**  
   - A clustered bar chart comparing average delays by region for a selected year.

3. **Top 5 Countries with Highest Delays**  
   - A table or bar chart listing the top 5 countries with the highest average delays.

4. **Outlier Analysis**  
   - A visual (e.g., scatter plot or highlighted table) indicating countries with outlier delays.

5. **Filters and Slicers**  
   - Include slicers for `Region`, `Year`, and `Country` to allow users to explore the data interactively.

Please note that the sample spreadsheet contains only ISO country codes. Reports are expected to display the full country and region names properly. You may use external resources to map the ISO codes to country and region names, such as *https://restcountries.com/v3.1/alpha/{ISO3_CODE}* or *https://api.worldbank.org/v2/country/{ISO3_CODE}?format=json*, or any other method you prefer.

#### **4. Submission Steps**

1. **Python Script**
   - Write a well-documented Python script that performs the required data analysis. Use comments to explain your logic.
   
2. **Power BI Report**  
   - Save your Power BI report as a `.pbix` file.

3. **Repository Update**  
   - Place your Python script, the processed CSV files, and the Power BI report in a folder named `NSDP_Challenge` and push it to your GitHub repository.

4. **Write a README**  
   - Include a README file in your repository that explains:
     - The objective of the challenge.
     - Steps to run your Python script.
     - Instructions on how to open and explore your Power BI report.
     - Any assumptions or decisions made during the analysis.

5. **Pull Request**  
   - Create a pull request to the main branch of the repository.

6. **Notify Us**  
   - Once your pull request is created, send an email to notify us that your work is ready for review.

---

### **Evaluation Criteria**

Your submission will be evaluated on the following criteria:

1. **Correctness**:  
   - Does the Python script produce the required outputs correctly?  
   - Are the CSV files structured as expected?

2. **Code Quality**:  
   - Is the Python code well-documented, clean, and following best practices?

3. **Visualization**:  
   - Are the Power BI visuals clear, informative, and interactive?  
   - Do they provide meaningful insights into the data?

4. **Documentation**:  
   - Is the README file clear and complete?

---

For more information about Data Standards and NSDP, please visit the [Data Dissemination Bulletin Board](https://dsbb.imf.org/).

Good luck, and we look forward to your submission!
