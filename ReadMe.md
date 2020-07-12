# Predicting Life Expectancy in the US
## *Using gender, state, and personal income quartile to predict longevity*

---

### Tools and tech used in this project:

- SAS to clean the data
- Python (sklearn, joblib) to generate the model
- Python (flask) to host the webpage
- Tableau to create the visualizations
- HTML/CSS/JavaScript to structure and enhance the webpage

![SAS](/Images/sas.png)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Python](/Images/python.png)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Tableau](/Images/tableau.png)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![HTML, CSS, JS](/Images/html_css_js.png)

---

### Data Sources:

- Data obtained from *[The Health Inequality Project](https://healthinequality.org/data/)*
	> The Health Inequality Project uses big data to measure differences in life expectancy by income across areas and identify strategies to improve health outcomes for low-income Americans. **[The Association Between Income and Life Expectancy in the United States, 2001-2014](https://jamanetwork.com/journals/jama/fullarticle/2513561?guestAccessKey=4023ce75-d0fb-44de-bb6c-8a10a30a6173)**

- Income quartiles for 2018 were obtained from *[Don't Quit Your Day Job](https://dqydj.com/2018-income-percentile-by-state-calculator/)*. Data provided by IPUMS-CPS, University of Minnesota, [www.ipums.org](www.ipums.org).
	> DQYDJ has provided original finance and investment research and tools since 2009. With hundreds of interactive tools, thousands of articles, tens of thousands of subscribers, and millions of page views, DQYDJ is a trusted source for statistics, economics, and financial strategies.

	> IPUMS CPS is an integrated set of data from the Current Population Survey (CPS) from 1962 forward. IPUMS CPS is microdata- it provides information about individual persons and households. The IPUMS CPS project was carried out by the Minnesota Population Center in collaboration with Unicon Research Corporation.

---

### Notes:

- Model was trained on data obtained for the years 2001 to 2014.
- life expectancy prediction is based on individuals at age 40, and is not adjusted by race.
- Individual income quartiles provided on webpage reflect 2018 - for the most recent income quartile calculations (2019), be sure to use [this link](https://dqydj.com/income-percentile-by-state-calculator/), also provided on the webpage.
- This project was originally created in October 2019, as a part of a data analytics and visualizations bootcamp. It was last updated in July 2020.
- Please note that this is a personal project that is not peer-reviewed and should not be used to make any assumptions or claims.