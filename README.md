# Capstone Project - Customer Persona Generator
- Author: Chi-Yuan (Tina) Peng
- Date: Dec. 2022

## Introduction
Hi, I am Chi-Yuan (Tina) Peng. And this is my capstone project. 🤗

In this capstone project, I want to design a persona generator that can automatically generate the persona and summary report of the customer segmentation. The persona generator can reduce the time and effort people need to spend on reading the customer segmentation report. Also, it allows the sales, marketing, and product design teams have a deeper understanding of who they are selling to and designing for,  why, and how their customers buy and use the products.

## Background
### What is customer segmentation ? 
According to [Garner](https://www.gartner.com/en/sales/glossary/customer-segmentation), **customer segmentation** is a process of analyzing customers' buying behavior and clustering customers into groups. It helps companies get more understanding of their customers of why and how they buy products. And the segment analysis can help and benefit the company by providing potential marketing and sales strategies for their customer groups.

### What is persona ?
"User personas are archetypical users whose goals and characteristics represent the needs of a larger group of users," according to [Adobe Xd](https://xd.adobe.com/ideas/process/user-research/putting-personas-to-work-in-ux-design/). **Persona** is usually a one to two pages profile to describe what kind of person your user or customer is. It usually includes a name, age, gender, habits, personality, product preference, and other background information. It helps product designers, sales, and marketing teams to have a deeper understanding of who they are designing for or selling to. With this better understanding of the target audiences or customers, it is more likely to create a product, provide the service, or make a successful marketing strategy that fulfills customer needs and improves sales.

## Objectives
![objectives](/pics/objectives.png "my objectives")

## Data
The dataset I used in this project is from [Kaggle customer segmentation clustering data](https://www.kaggle.com/code/karnikakapoor/customer-segmentation-clustering/data). It is a customer information dataset from a grocery store, including customers' age, marital status, number of they have, annual income, the amount they spent on different types of products, and so on. We can tell from the variables in the dataset that this grocery store has 7 types of products, including wine, fruits, meat, seafood, sweets, gold, and on-sale products. 

These are the variables that I will focus on in this project.
![variables](/pics/focus_variables.png "focus variables")

## Data Preprocessing
### Data cleaning
1. Missing values:
	There are totally 2,240 observations inside this dataset. And there are only 24 missing data of the `income` column, so I will remove those missing data.
2. Outliers:
	Removed 1 observation whose annual income is over 500,000.

### Create new columns
1. `edu_level` : 
	- This column is create from `Education` column, which stands for the education qualification of a customer, and includes 5 types of education qualification: Graduation, 2n Cycle, Basic, PhD, and Master. 
	- I will relabel these types into numbers from 1 to 3 to show the education levels:
		- 1:  2n Cycle, and Basic
		- 2: Graduation
		- 3: PhD, and Master
2. `not_live_alone` :
	- This column is create from `Marital_Status` column, which stands for marital status of a customer. 
	- I will relabel this column into 0 and 1 to show if this customer is living with any partner:
		- 0: All other status.
		- 1: Married, Together
3. `age` :
	- Create a new column by subtracting the  `Year_Birth`  from current year (2022). 
	- Removed 3 observations whose age are over 90.
4. `num_child` :
	-   Create a new column to add two columns `Kidhome` and `Teenhome` together to show the total number of children this customer has.
5. `has_child` :
	-   Create a new column to describe if this customer has any child. 0 stands for no child, and 1 stands for at least one child.
6. `num_family_member` :
	-   Create a new column to add  `not_live_alone`  and  `num_child` together to show the total number of family member this customer has.
7. `single_parent` :
	-   Create a new column to describe if this customer is single parenting (has at least one kid and is living without a partner).
8. `total_spent` :
	-   Create a new column to record the totall amount the customer spent in the store by adding all amount spending columns together, including `MntWines`, `MntFruits`, `MntMeatProducts`, `MntFishProducts`, `MntSweetProducts`, and `MntGoldProds`.
9. Percentage of the amount (`Pr_`) :
	- Create 6 new columns each calculating the percentage of the amount the customer spent on each type of products. 
```
File: 01_Data_Cleaning_and_EDA.ipynb
Input: customer_segmentation_rawdata.csv
Output: cleaned_data.csv
```
## Modeling
For customer segmentation, our goal is to cluster our customers into groups according to their feature behaviors. Therefore, I will use the unsupervised learning model - **KMeans** to make the clusters.
### Standard Scale
Before building the model, we need to use **Standard Scale** to remove the mean and scales of each variable to unit variance to make sure our variables are under the same scale.
### Choose the k (number of clusters)
Then, I used **inertia score** and **silhouette score** to tell which k (number of clusters) is optimal for this dataset. And I found that both of them didn't show the best number of k for me. Thus, I decided to add another step, **PCA**, before making the KMeans. PCA helps me to reduce the features and only focus on the main combining features I will need to use in the model.

And after the PCA process, the **inertia score** and **silhouette score** show that the optimal k is 4. Thus, I then used KMeans with **k = 4** to cluster the customers in this dataset into four groups. And I labeled them group A, B, C, and D.

```
File: 02_Feature_Engineering_and_Modeling.ipynb
Input: cleaned_data.csv
Output: labeled_result.csv
```
## Segment Analysis
After grouping customers into four groups, we can start to analyze what features each group has and generate some insights from it.

This is the analysis report from my customer segmentation:
![customer segment](/pics/customer_segment.png "customer segment")

However, this is a traditional way to do the segment report. In this project, I want to design a **persona generator** to automatically generate a summary report for my customer segmentation and also generate a persona for each group according to the features of the group they belong.

```
File: 03_Customer_Segment_Analysis.ipynb
Input: labeled_result.csv
Output: summary_result.csv
```
## Persona Generator
### Persona draft and introduction
This is my persona draft:
![persona draft](/pics/persona_draft.png "This is my persona draft")
- Name:
	- To randomly generate a name for a persona, I will need three name lists first, first names for males, first names for females, and last names.
	- Thus, I web-scraped two first name lists from [SSA - Top Names Over the Last 100 Years](https://www.ssa.gov/oact/babynames/decades/century.html) and last name list from [Name Census - What are the 5,000 Most Common Last Names in the U.S.?](https://namecensus.com/last-names/). And I saved them into a file called `name_list.csv`.
	- Finaly, in the persona generator, the program will randomly select a first name and last name from the file according to the gender provided.
- Gender: 
	- Gender is one of the most important features a persona should have since gender difference sometimes will make impact on what kinds of products we are going to sell to this group of customers. 
	- Also, usually, gender will be provided in a customer information database; however, in this dataset, it doesn't provide the gender of each customer. Thus, for this gender column, I will make the program randomly generate a gender for a persona.
- Age:
	- Persona's age will be randomly generated from the age range of the group. For example, if the age of group A is from 35 to 50, the program will randomly select a number between 35 to 50 and set it as the persona's age. *(range is from 25th percentile to 75th percentile)
- Group size:
	- This column shows the percentage of customers inside this group. For example, group A's size is 30% means that 30% of the customers in this whole dataset are grouped into group A.
	- With this column, we can tell the important difference between each persona. For example, if group A is 30% and group B is only 10%, then we can tell that group A might have a higher importance than group B since they are the majority and might generate more impacts on our sales, market, revenues, and so on.
- Photo:
	- An image is the soul of a persona since it does really help people to recognize and make the imagination of their target customers. Thus, I found a [python package: python-avatars](https://pypi.org/project/python-avatars/) which can help me create an avatar image for the persona. 
	- This package allows me to generate an avatar with different hair types, hair colors, clothing types, clothing colors, and so on. To make it simple, I selected 8 hair types for each gender and 5 clothing types. I also assigned 12 colors for clothing and 10 for hair. And the program will randomly generate an image from these selections based on the gender it gave.
- Profile:
	- Inside the profile column, there are some describtive information about this persona, for example, annual income, spending level, and family size. And these information are randomly generated from the given range of the group, same as the age column. *(range is from 25th percentile to 75th percentile)
	- Note that I make the spending amount into spending levels (High, Medium, and Low). A High spending level is the group with the highest spending range, and Low spending level is the lowest group. The purpose of doing this is to highlight the consuming ability of the highest and lowest group.
- Product preference:
	- This column allows us to notice the product preference of each group. For example, if it shows Friuts and Cookies in orange, this group of customers usually buy Friuts and Cookies from this store. 
	- I set the threshold to be the mean of the entire customers of the dataset. That is if the percentage of the amount the group A people spent on meat is over the threshold (the overall mean of the percentage of the amount spent on meat), group A people have a preference for meat products.

	\***Note**: The range of age, income, family size, and the number of kids are based on the 25th and 75th percentile of the group.

### Display the Persona via [Streamlit](https://streamlit.io/)
To fulfill this program and display the persona, I use wrote the whole python code in the `app.py` file and display it on Streamlit. 

Below is what the customer persona generator page looks like:
![persona display](/pics/persona_page.png "This is the display of customer persona")

```
File: app.py, web_scraping_name.ipynb
Input: summary_result.csv, name_list.csv
Output: customer persona generator streamlit page
```

## Citations
- [Kaggle customer segmentation clustering data](https://www.kaggle.com/code/karnikakapoor/customer-segmentation-clustering/data)
- [Python package: python-avatars](https://pypi.org/project/python-avatars/)
- [Streamlit](https://streamlit.io/)
- [SSA - Top Names Over the Last 100 Years](https://www.ssa.gov/oact/babynames/decades/century.html)
- [Name Census - What are the 5,000 Most Common Last Names in the U.S.?](https://namecensus.com/last-names/)
- [Garner - What Is Customer Segmentation](https://www.gartner.com/en/sales/glossary/customer-segmentation)
- [Adobe Xd - Putting Personas to Work in UX Design: What They Are and Why They’re Important](https://xd.adobe.com/ideas/process/user-research/putting-personas-to-work-in-ux-design/)
- [Excalidraw](https://excalidraw.com/)
- [Slidesgo - slides template](https://slidesgo.com/theme/flat-style-buyer-persona-infographics)

---
#### Hashtags
`#persona` `#customer_segmentation` `#persona_generator` 
`#machine_learning` `#unsupervise_learning` `#clustering` `#KMeans` `#PCA` `#standard_scaler` `#web_scraping` 
`#python` `#streamlit` `#html` `#avatar_generator` 



