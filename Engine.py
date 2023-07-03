import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset from CSV
data = pd.read_csv('data.csv')

# Content-Based Filtering
# Prepare data for content-based filtering
tfidf_attributes = TfidfVectorizer(stop_words='english')
attribute_matrix = tfidf_attributes.fit_transform(data[['Skill', 'region', 'year', 'technology']].astype(str).values.flatten())

# Calculate similarity matrix based on attributes
attribute_similarity = cosine_similarity(attribute_matrix)

# Hybrid Recommendation
def get_recommendations(user_id, age_group, skill, region, technology, course_choices, top_n=5):
    # Content-Based Filtering
    user_courses = data[(data['ID'] == user_id) & (data['year'] == age_group) & (data['Skill'] == skill) & (data['region'] == region) & (data['technology'] == technology)]['ID'].values
    user_courses = set(user_courses) - set(course_choices)  # Exclude user's previous course choices
    
    # Merge and deduplicate recommendations
    recommendations = list(user_courses)
    
    return recommendations[:top_n]

# Test the recommendation engine
user_id = 'df7c29db-bd46-47fe-963e-09db434bf19a'  # Example user ID
age_group = '0 to 3 years'  # Example age group
skill = 'Beginner'  # Example skill level
region = 'Americas'  # Example region
technology = 'Automation.NET/C#C++'  # Example technology
course_choices = ['a4af6aca-817d-4f2c-b74b-3f45ee33191c']  # Example user's previous course choices
recommendations = get_recommendations(user_id, age_group, skill, region, technology, course_choices, top_n=5)
print("Recommendations for User", user_id, ":")
for course_id in recommendations:
    print(course_id)
