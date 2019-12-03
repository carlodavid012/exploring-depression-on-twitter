# Exploring Depression on Twitter

### Overview

Depression is the leading cause of disability worldwide. Almost 75% of people with mental disorders remain untreated in developing countries with almost 1 million people taking their lives each year. In addition, according to the World Health Organization (WHO), 1 in 13 globally suffers from anxiety. 

Around 3 million Filipinos live with depression. Arguing that social media is an alternative platform documenting daily life and thought patterns, In this project, we will explore tweets of depressed users to identify changes in social media language and behavior that might signal the onset of a depressive episode. The purpose of is to create a machine learning model for early intervention for depression that is contextualized in the Philippines.


### Dataset

We scraped data from Twitter using the [Twint](https://github.com/twintproject/twint) library. We scraped tweets from users near Manila, Philippines and only include English tweets. The dataset contains about 114,728 tweets  which roughly 100 self-identify as having been diagnosed with depression (users who publicly tweeted “I was diagnosed with depression” or similar), with manual validation of tweets to check sarcasm/jokes and to remove automated tweets. 

