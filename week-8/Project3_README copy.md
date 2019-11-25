
# Module 4 Final Project - Multiple Regression with Regularization


## Introduction

In this lesson, we'll review all of the guidelines and specifications for the final project for Module 4.

## Objectives
You will be able to:
* Describe all required aspects of the final project for Module 4
* Describe all required deliverables
* Describe what constitutes a successful project
* Describe what the experience of the project review should be like

## Final Project Summary

You've made it all the way through the first module of this course - take a minute to celebrate your awesomeness!

![awesome](https://raw.githubusercontent.com/learn-co-curriculum/dsc-v2-mod1-final-project/master/awesome.gif)

All that remains in Module 4 is to put our newfound regression skills to use with a final project! You should expect this project to take between 20 and 25 hours of solid, focused effort. If you're done way quicker, go back and dig in deeper or try some of the optional "level up" suggestions. If you're worried that you're going to get to 30 hrs and still not even have the data imported, reach out to an instructor in Slack ASAP to get some help!

## The Dataset

For this project, you'll have the option to work on your own dataset, as long as it is a regression problem. We have also provided a few available default datasets for you to use in case you can't collect your data in time. One of the options is the King's county dataset, which we've modified to make it a bit more fun and challenging.  The dataset can be found in the file `"kc_house_data.csv"`, in this repo.

#### Kc House data
The description of the column names can be found in the column_names.md file in this repository. As with most real world data sets, the column names are not perfectly described, so you'll have to do some research or use your best judgment if you have questions relating to what the data means.

You'll clean, explore, and model this dataset with a multivariate linear regression to predict the sale price of houses as accurately as possible.

## The Deliverables

1. A well documented **Jupyter Notebook** containing any code you've written for this project and comments explaining it. This work will need to be pushed to your GitHub repository in order to submit your project.  
2. An organized **README.md** file in the GitHub repository that describes the contents of the repository. This file should be the source of information for navigating through the repository.
3. A short **Keynote/PowerPoint/Google Slides presentation** (delivered as a PDF export) giving a high-level overview of your methodology and recommendations for non-technical stakeholders. Make sure to also add and commit this pdf of your non-technical presentation to your repository with a file name of presentation.pdf.
4. **LEVEL UP** Optional blog post detailing the process and findings of your project.

Note: On-campus students may have different requirements, please speak with your instructor.

### Jupyter Notebook Must-Haves

For this project, your Jupyter Notebook should meet the following specifications:

#### Organization/Code Cleanliness

* The notebook should be well organized, easy to follow,  and code should be commented where appropriate.  
    * Level Up: The notebook contains well-formatted, professional looking markdown cells explaining any substantial code.  All functions have docstrings that act as professional-quality documentation
* The notebook is written for technical audiences with a way to both understand your approach and reproduce your results. The target audience for this deliverable is other data scientists looking to validate your findings.

#### Visualizations & EDA

* Your project contains at least 4 meaningful data visualizations with corresponding interpretations. All visualizations are well labeled with axes labels, a title, and a legend (when appropriate)  
* You pose at least 3 meaningful questions and answer them through EDA.  These questions should be well labeled and easy to identify inside the notebook.
    * **Level Up**: Each question is clearly answered with a visualization that makes the answer easy to understand.   
* Your notebook should contain 1 - 2 paragraphs briefly explaining your approach to this project.

#### Model Quality/Approach

* Your model should not include any predictors with p-values greater than .05.  
* Your notebook shows an iterative approach to modeling, and details the parameters and results of the model at each iteration.  
    * **Level Up**: Whenever necessary, you briefly explain the changes made from one iteration to the next, and why you made these choices.  
* You spend at least 1 slide explaining your final model.
* You pick at least 3 coefficients from your final model and explain their impact on the outcome and interpret how these variables affect the outcome.
* You use regularization or another variable selection approach such as the F test to explain why you have selected the predictors you have selected. 
* You validate the performance of your model from the aspect of cost function and parsimony - how good is your model at predicting the outcome you want to predict? 


### Non-Technical Presentation Must-Haves

Another deliverable should be a Keynote, PowerPoint or Google Slides presentation delivered as a pdf file in your repository with the file name of `presentation.pdf` detailing the results of your project.  Your target audience is non-technical people interested in using your findings to solve the problem in the project's domain e.g maximize their profit when selling a home.

Your presentation should:

* Contain between 5 - 10 professional-quality slides.  
    * **Level Up**: The slides should use visualizations whenever possible, and avoid walls of text.
* Take no more than 5 minutes to present.   
* Avoid technical jargon and explain the results in a clear, actionable way for non-technical audiences.   

**_Based on the results of your models, your presentation should discuss at least two concrete features that highly influence the target variable e.g housing prices._**


## Summary

The end of module projects are a critical part of the program. They give you a chance to both bring together all the skills you've learned into realistic projects and to practice key "business judgement" and communication skills that you otherwise might not get as much practice with.

The projects are serious and important. They are not graded, but they can be passed and they can be failed. Take the project seriously, put the time in, ask for help from your peers or instructors early and often if you need it, and you'll do great. We'll also provide open and honest feedback so you can improve as quickly and efficiently as possible.

Finally, this is your first model. We don't expect you to remember all of the terms or to get all of the answers right. If in doubt, be honest. If you don't know something, say so. If you can't remember it, just say so. It's very unusual for someone to complete a project without being asked a question they're unsure of, we know you might be nervous which may affect your performance. Just be as honest, precise and focused as you can be, and you'll do great!