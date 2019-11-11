**Course**: Data Science   <br/>
**Mod**: 1                    <br/>
**Topic**: Statistical Distributions                  <br/>
**Amount of time**: 1.5 hours <br/>
**Author**: Greg Damico


***

## Lesson Summary:

#### Topic:
Statistical Distributions

#### Learn.co material:
<https://learn.co/tracks/data-science-career-v1-1/section-01/section-09-statistical-distributions/introduction?>

#### Prerequisite knowledge/ Prework:
Student should have a basic understanding of statistical concepts.


#### Learning goals for this lesson:
SWBAT: <br/>
- Explain the difference between discrete and continuous distributions <br/>
- Explain the differences among probability mass functions, cumulative distribution functions, and probability density functions <br/>
- Explain the importance of the normal distribution <br/>
- Use z-scores to calculate probabilities


#### Misconceptions:
Knowing statistics isn't imnportant for the practicing data scientist. (Fact: Very much of data science is applied statistics!)

#### Materials:
weight-height.csv (from Kaggle) <br/>
Jupyter notebooks: 
\_statistical\_distributions and \_demonstration\_manipulation\_of\_height\_dataset.ipynb <br/>
z-table.com <br/>
blog post: <https://emredjan.github.io/blog/2017/07/19/plotting-distributions/>

***


## Lesson Outline:

**Step 1**: Problem <br/>
**Time**: 10 min

_Goal/Scenario:_<br/>
Leading question: If I measure some quantity, what is the probability that I get one value rather than another? Contrast different scenarios here. If I flip a fair coin, what is the probability that I get heads rather than tails? If I measure the height of someone randomly selected from the U.S. population, what is the probability that I get someone who's 5'9"? What is the probability that I get someone who's 7'9"?

Scenario: I want to calculate what the probability is that I select a person who's 6'6" or taller.

_Learning Goals in sequence:_<br/>
- Explain the difference between discrete and continuous distributions <br/>
- Explain the differences among probability mass functions, cumulative distribution functions, and probability density functions <br/>
- Explain the importance of the normal distribution <br/>
- Use z-scores to calculate probabilities

**Step 2**: Activation <br/>
**Time**: 5 min

Students all have the experience of tossing coins and rolling dice (where the distribution is uniform). Tell them that the idea is to generalize from this familiar sort of activity to be able to draw conclusions about statistical frequencies for other sorts of distributions.

**Step 3**: Learning Goal 1: Explain the difference between discrete and continuous distributions. <br/>
**Time**: 5 min

_Demonstrate_: <br/>
Illustrate the difference between discrete and continous sets / variables.

_Application_: <br/>
Question: "Discrete or continuous?": <br/>
- how much time between click-events <br/>
- how many people in attendance at a football game <br/>
- how tall a person is


_Informal assessment_: <br/>
Poll the class: Is the distinction clear?


**Step 4**: Learning Goal 2: Explain the differences among probability mass functions, cumulative distribution functions, and probability density functions. <br/>
**Time**: 10 min

_Demonstrate_: <br/>
Use the notebook and the blog post to illustrate different distributions. Show that discrete distributions have pmfs while continuous distributions have pdfs.

_Application_: <br/>
Question: When would I want to use the cdf rather than the pmf or pdf? Which do I want to use in our example of the varying heights?

_Informal assessment_: <br/>
Poll

**Step 5**: Learning Goal 3: Explain the importance of the normal distribution. <br/>
**Time**: 10 min

_Demonstrate_: <br/>
Use the notebook to demonstrate normal distributions.

_Application_: <br/>
Question: Does it make sense to use the normal distribution for our problem about heights?

_Informal assessment_: <br/>
What other variables might be normally distributed?

**Step 6**: Learning Goal 4: Use z-scores to calculate probabilities. <br/>
**Time**: 15 min

_Demonstrate_: <br/>
Give students the idea of _standardization_: replacing values of a variable with the ratio of the difference between that value and the mean to the standard deviation.

Show them <http://z-table.com>.

_Application_: <br/>
Ask them to use the table:
-What is the probability of selecting a value 2.48 standard deviations above the mean from a normally distributed variable? (Ans. 0.66%) <br/>

-How much smaller than the mean must a value be before the chance of selecting that small of a value drops below 1%? (Ans.: 2.33 standard deviations below the mean.)


_Informal assessment_: <br/>
Poll: Does everyone feel comfortable using the z-table?


**Step 7**: Integration:  <br/>
**Time**: 15 min

_Synthesis_: <br/>
Review: We now need to solve our problem. How do we go about answering our question about selecting someone taller than 6'6"? <br/>
(Ans.: We need to get the z-score for 78" = 6'6", which means we'll need to know the mean and the std for the 'Height' column in the dataset. Then we'll need to consult the z-table.)

_Application_: <br/>
Go through the steps in the notebook and/or ask the students to help. Point them (only at the end!) to sklearn.preprocessing.StandardScaler if they don't already know of it.

**Step 8**: Assessment:  <br/>
**Time**: 10 min

Think-pair-share: What were the crucial steps in solving a z-score problem?

**Step 9**: Reflection:  <br/>
**Time**: 5 min

How might the normal distribution apply to your future projects?

