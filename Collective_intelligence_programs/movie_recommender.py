# Movie recommender implementation 
from math import sqrt
# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

# Similarity functions

# Euclidian scores - This is used to implement a function to find the euclidian score between the two critics
# Arguments - critic - Current dictionary with the details of the critics
# 			  person1,person2 - Name of the persons whose euclidian distance has to be calculated

def euclidian_score(critic,person1,person2):


	# Find sum of squares of scores for movies which are rater by both the persons
	sum_of_scores=sum(pow(critic[person1][item]-critic[person2][item],2) for item in critic[person1] if item in critic[person2])

	return 1/(1+sqrt(sum_of_scores)) # Add 1 to denominator and take reciprocal. The higher the number the similar the people

# Pearson score - This function is used to find the pearson score between two variables. The pearson score is used when the data is not normalized. 
# Euclidian on the other hand is used to find relation between data that is much more normalized. It returns value between -1 to 1
def pearson_score(critic,person1,person2):

	common_movies={}
	# Find the common movies rated by both the critics
	for item in critic[person1]:
		if item in critic[person2]:
			common_movies[item]=1

	# Find the length of the common movies dictionary
	n=len(common_movies)

	# Find the expectation E[XY]
	E_XY=sum(critic[person1][item]*critic[person2][item] for item in common_movies)

	# Calculate the expectation E[X]
	E_X=sum(critic[person1][item] for item in common_movies)

	# Calculate the expectation E[Y]
	E_Y=sum(critic[person2][item] for item in common_movies)

	# Calculate expectation E[X^2]
	E_X2=sum(pow(critic[person1][item],2) for item in common_movies)

	# Calculate expectation E[Y^2]
	E_Y2=sum(pow(critic[person2][item],2) for item in common_movies)

	num=E_XY-(E_X*E_Y/n) # Numerator for pearson score
	den=sqrt((E_X2-pow(E_X,2)/n)*(E_Y2-pow(E_Y,2)/n)) # Denominator for pearson score

	if den != 0:
		return num/den # Pearson score

# This function is used to recommend a movie to the user specified. The input is the person and the similarity metric to use.
# To find the recommendation, we find the movies that the person has not seen and multiply the similarity of the critic to movie rating then divide the total by the similarity sum
def recommend_movie(critic,person,score_metric=pearson_score):

	# Dictionary to store the similarity of critics to the person
	simSums={}
	simxmovie_score={} # Dictionary to store similarity*rating score

	# Iterate through the critics list
	for critics in critic:
		if person == critics:continue  # Do not compare the same person
		sim=score_metric(critic,person,critics) # Get the similaity score for the two persons

		if sim <=0: continue # If score less than 0 then continue

		# Iterate through the movies not seen by the person
		for movie in critic[critics]:
			if movie in critic[person] or critic[critics][movie] <=0: continue # Skip the movies already reviwed by the person and also the movies which other critics have not reviewed
			# Set the defaults for dixtionary to 0
			simSums.setdefault(movie,0)
			simxmovie_score.setdefault(movie,0)
			simxmovie_score[movie]+=critic[critics][movie]*sim
			simSums[movie]+=sim # Sum of similarity for the movies


	# Create the rankings
	rankings=[(simxmovie_score[movie]/simSums[movie],movie) for movie in simSums]

	rankings.sort()
	rankings.reverse()
	return rankings





print(recommend_movie(critics,'Toby'))


	








