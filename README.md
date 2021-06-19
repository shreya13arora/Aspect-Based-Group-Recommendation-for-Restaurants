# Group-Restaurant-Recommendation-System

## The Project

Most work on Recommender Systems to date focuses on recommending items to individual users. For instance, they may help select a book for a particular user to read, a movie to watch or songs to listen to based on either the users preferences in the past or the users similarity with a group of other users. A lot of progress has already been made on this which is experienced by all of us in our day to day life.
 
Our project aims at taking a step forward and focusing on those instances when it makes more sense to recommend to a group of users rather than to an individual. For instance, activities such as watching a movie in the theatres, visiting a restaurant with a group of friends or choosing a radio station for background music in a fitness centre to suit a group of people involved in it. Assuming that we know perfectly what is good for individual users, the issue arises on how to combine individual user models.

## Challenges 

While we started with the main focus on exploring different techniques to build a Group Recommendation System for Restaurants , we noticed a major drawback on using the number scale rating system to build a recommendation system. Although it is said to be a good tool to capture the behaviour of respondents in a quantitative manner, it faces with a challenge of response error ie. It is much more difficult for some people to justify choosing a category on the extreme ends than others. This in turn leads to respondents with the same opinion about the item to select different ratings, making it difficult to qualify what opinion the resulting data truly represents.
 
## Our Idea
 
Since the ratings given by the user was not reliable, we decided to use the additional, more subjective, information available with us about the user behaviour : The Reviews.
But How ?  Using NLP based techniques, we built an Aspect Based Summarization model which takes in all the reviews given by user for different restaurants , synthesizes the ratings for the major aspects : "food", "ambience", "price", "service" on a scale of 1-5  based on the sentiments of words used in the review. These ratings are then used to build user identity (based on how he weights different aspects) and restaurant identity (which reflects the public perception of different aspects of the restaurant). These ratings were then aggregated using the best technique to come up with a list of restaurants which would be preferred by the group.
