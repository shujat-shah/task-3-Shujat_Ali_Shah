# Artificial Intelligence Project 3: AI Recommendation Logic

## 1. Project Goal
The goal of this project is to create a simple recommendation system based on user preferences. It steps into the role of an AI Engineer by focusing on "Pattern Alignment" to bridge the gap between raw user data and relevant content through algorithmic logic.

## 2. Key Requirements
According to the project guidelines, the following requirements must be met:
* **Take User Input:** Gather user choices or interests (e.g., asking users to rate their preference for different movie genres from 1 to 5).
* **Match Preferences:** Use logic and mathematical similarity (e.g., calculating a similarity score) to match user profiles with item attributes.
* **Display Recommendations:** Output a curated list of recommended items based on the similarity logic.
* **Key Skills Targeted:** Logic building, pattern matching, and fundamental recommendation concepts.

## 3. Procedure and Implementation Steps
The implementation follows these procedural steps to successfully align user patterns with item attributes:

### Step 1: Initialize the Dataset
* Create a hardcoded sample dataset of items. For example, a list of movies where each movie has specific "genre weights" representing its attributes (e.g., Action: 1.0, Sci-Fi: 0.8).

### Step 2: Gather User Preferences
* Present the user with a list of available categories (genres).
* Prompt the user to rate their interest in each category on a scale (e.g., 1 to 5). Users can skip categories they have no preference for.
* Build a **User Profile** dictionary/vector based on these input ratings.

### Step 3: Calculate Similarity Scores
* Iterate through each item (movie) in the dataset.
* Calculate the **Cosine Similarity** between the User Profile and the Item Profile.
  * **Formula:** The dot product of the two vectors divided by the product of their magnitudes.
  * This score effectively measures how closely the user's preferences align with the movie's genre distribution.

### Step 4: Rank the Items
* Store the similarity score for each item.
* Filter out items with a score of 0 (no match).
* Sort the remaining items in descending order based on their similarity score.

### Step 5: Display Results
* Select the top `N` items from the sorted list (e.g., top 3 or 4 recommendations).
* Display the recommendations to the user, optionally converting the similarity score into a percentage to show how strong the match is.
