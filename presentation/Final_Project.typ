#import "@preview/polylux:0.3.1": *
#import themes.university: *

#show: university-theme.with(
  color-a: rgb("#1A3C6E"),
  color-b: rgb("#1A3C6E"),
  
  short-author: "Luka D, Nikoloz K, Ivane U",
  short-title: "Final Project",
  short-date: "Fall Term 2024",
)

#title-slide(
  authors: ("Luka Dumbadze, Nikoloz Kvinikadze, Ivane Urjumelashvili"),
  title: "Final Project",
  subtitle: "Intorduction to Data Science with Python",
  date: "January 22, 2025",
  institution-name: "Kutaisi International University",
  logo: align(center,image("thumbnail_KIU2_1.png", width: 40%)) 
)

#slide(outline())

#slide(title: [Project Goals])[
  - *Objective:*

    - Understand the factors influencing depression among students.
    - Analyze relationships between lifestyle, academic performance, and mental health.

  - *Key Deliverables:*

    - Clean and preprocess the dataset.
    - Conduct exploratory data analysis (EDA) with visualizations and statistical insights.
]

#slide(title: [Dataset Overview])[
  - *Dataset Description:*
    - Source: Provided dataset on student depression.
    - Rows: Number of students.
    - Columns: Features such as age, gender, CGPA, depression status, academic pressure, etc.

  - *Target Variable:* Depression_Status (Binary: Yes/No)
  - *Challenges:*
    - Missing values in some columns.
    - Presence of outliers in numerical data.
]

#slide(title: [Data Preprocessings])[

  - *Steps Taken:*

    - Handled missing values using median/mode imputation.

    - Identified and addressed outliers using the IQR method.
    - Encoded categorical variables (e.g., _Sleep Duration_ mapped to numeric values).

  - *Visuals:*
    - *before-and-after box plot* to show outlier handling.
]
#slide(title: [Data Preprocessings], new-section: [*before box plot*])[

  === 
  #align(center, image("../outputs/before.png"))]

#slide(title: [Data Preprocessings], new-section: [*after box plot*])[
  === before box plot
  #align(center, image("../outputs/after.png"))
]

#slide(title: [Exploratory Data Analysis (EDA)], new-section: [*Overview*])[

  - *Purpose:*

    - Discover patterns and trends in the data.

    - Visualize relationships between key features and depression status.

  - *Tools Used:*

    Pandas, Seaborn, Matplotlib, and Scipy for statistical tests.
]

#slide(title: [Key Findings from EDA], new-section: [*CGPA vs. Depression Status*])[
  Students with lower CGPA tend to have higher depression rates.

  #align(center, image("../outputs/cgpa_vs_depression.png", width: 73.5%))
]

#slide(title: [Key Findings from EDA], new-section: [*Academic Pressure Distribution*])[
  Students experiencing higher academic pressure are more likely to report depression.

  #align(center, image("../outputs/Academic_Pressure_Distribution.png", width: 66%))
]

#slide(title: [Key Findings from EDA (continued)], new-section: [*Correlation Heatmap*])[
  Strong correlations observed between depression and factors like academic pressure, work pressure, and financial stress.

  #align(center, image("../outputs/correlation.png", width: 44%))

]

#slide(title: [Key Findings from EDA (continued)], new-section: [*Family History of Mental Illness*])[
  Students with a family history of mental illness have a higher likelihood of depression.
  #align(center, image("../outputs/family_history_of_mental_illness.png", width: 66%))

]

#slide(title: [Statistical Insights])[
  - *Risk Factors:*
    - *Mann-Whitney U Test:* Significant differences in academic pressure and CGPA between students with and without depression (p < 0.05).
    - *Chi-Square Test:* Significant association between depression and family history of mental illness.
  - *Effect Sizes:*
    - Academic pressure shows a medium effect size, indicating a notable impact.
]

#slide(title: [Conclusion])[
  - *Summary of Findings:*
    - Academic and work pressure, along with financial stress, are key contributors to depression.
    - Family history of mental illness is a significant categorical factor.
  - *Effect Sizes:*
    - Academic pressure shows a medium effect size, indicating a notable impact.
]

#slide(title: [Questions and Answers], new-section: [*Q&A*])[
  = Encourage the audience to ask questions about the EDA process or findings. 
] 