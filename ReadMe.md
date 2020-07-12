# Predicting Life Expectancy in the US
## *Using gender, state, and personal income quartile to predict longevity*

---

### Tools and tech used in this project:

- SAS to clean the data
- Python (sklearn, joblib) to generate the model
- Python (flask) to host the webpage
- Tableau to create the visualizations
- HTML/JavaScript/CSS to structure/enhance the webpage

![SAS](images/sas.png) ![Python](images/python.png) ![Tableau](images/tableau.png) ![HTML, CSS, JS](images/html_css_js.png)

---

### Data Sources:

- Data obtained from *[The Health Inequality Project]*(https://healthinequality.org/data/)
	> The Health Inequality Project uses big data to measure differences in life expectancy by income across areas and identify strategies to improve health outcomes for low-income Americans. **[The Association Between Income and Life Expectancy in the United States, 2001-2014]**(https://jamanetwork.com/journals/jama/fullarticle/2513561?guestAccessKey=4023ce75-d0fb-44de-bb6c-8a10a30a6173)
- Income quartiles for 2015 were obtained from *[Don't Quit Your Day Job]*(https://dqydj.com/average-income-by-state-median-percentiles/). Income quartiles for 2019 can be referenced [here](https://dqydj.com/income-percentile-by-state-calculator/). Data provided by IPUMS-CPS, University of Minnesota, [www.ipums.org](www.ipums.org).
	> DQYDJ has provided original finance and investment research and tools since 2009. With hundreds of interactive tools, thousands of articles, tens of thousands of subscribers, and millions of page views, DQYDJ is a trusted source for statistics, economics, and financial strategies.

---

### Notes:

- Model was trained on data obtained for the years 2001 to 2014. 
- Individual income quartiles provided on webpage reflect 2015 - be sure to use [this link](https://dqydj.com/income-percentile-by-state-calculator/), provided above and on the webpage, to use the most recent income quartile calculations (2019). 
- This project was originally created in October 2019, as a part of a data analytics and visualizations bootcamp. It was last updated in July 2020.
- Please note that this is a personal project that is not peer-reviewed and should not be used to make any claims. 