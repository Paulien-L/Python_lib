from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import json
import seaborn as sb

'''
Educational code to explore some of the features of matplotlib's pyplot, seaborn and pandas.
Starts from dummy dataset on student test scores (example_scores.json) with following columns:
Gender, Name, Score_test1, Score_test2, Score_test3

Generates five plots:
- Figure 1: Spaghetti plot of the score evolution over all tests
- Figure 2: Three barplots of the score distribution on each test
- Figure 3: Three boxplots of the scores in male vs. female students for three tests
- Figure 4: Three violinplots of the scores in make vs. female students for three tests
- Figure 5: Three piecharts of the percentage of students passed and failed for three tests
'''

def read(inputData):
	'''
	Reads json file as dictionary.
	
	Keyword arguments:
	input -- input file in json format (json)
	
	Returns:
	data -- dictionary containing json file contents (dictionary)
	'''
	with open(inputData) as f:
		data = json.load(f)
	return data

inputData = r'example_scores.json'
data = read(inputData)

scores = pd.DataFrame(data)

# Figure 1: class score evolution over tests
plt.figure()

def calcClassMean(scores, numTests):
	'''
	Calculates class mean over a number of tests
	
	Keyword arguments:
	scores		--	input dataframe (python dictionary or pandas-style dataframe)
					caveat: test scores should start at third column of dataframe
	numTests	-- 	number of tests the class mean should be calculated over (int)

	Returns:
	class_mean	--	mean of test scores over all students in the dataframe (float)
	'''
	class_mean = []
	for i in range(numTests):
		test_class_mean = np.mean(scores["Score_test" + str(i+1)])
		class_mean.append(test_class_mean)
	return class_mean

class_mean = calcClassMean(scores,3)
test_class_mean_labels = ["Test 1", "Test 2", "Test 3"]

plt.plot(range(len(test_class_mean_labels)), class_mean, color="black", linewidth=2)

for i,j,k in zip(scores["Score_test1"], scores["Score_test2"], scores["Score_test3"]):
	plt.plot(range(len(test_class_mean_labels)), [i,j,k], color = "gray", alpha=0.6)

fig1_ax = plt.subplot()
fig1_ax.set_xticks(range(len(test_class_mean_labels)))
fig1_ax.set_xticklabels(test_class_mean_labels)
fig1_ax.set_yticks([0,25,50,75,100])

plt.legend(["Class average score", "Individual scores"])

plt.xlabel("Tests")
plt.ylabel("Score")
plt.title("Score evolution over tests January")

plt.savefig("1_score_evolution_jan.png")
plt.close("all")

# Figure 2: barplot scores per test
plt.figure(figsize=(10,8))

# subplot 1
fig2_1_ax = plt.subplot(3,1,1)
sb.barplot(data=scores, x="Name", y="Score_test1")
plt.title("Scores of student per test (January)")
plt.xlabel("Student")
plt.ylabel("Test 1")
fig2_1_ax.set_yticks([0,25,50,75,100])

# subplot 2
fig2_2_ax = plt.subplot(3,1,2)
sb.barplot(data=scores, x="Name", y="Score_test2")
plt.xlabel("Student")
plt.ylabel("Test 2")
fig2_2_ax.set_yticks([0,25,50,75,100])

# subplot 3
fig2_3_ax = plt.subplot(3,1,3)
sb.barplot(data=scores, x="Name", y="Score_test3")
plt.xlabel("Student")
plt.ylabel("Test 3")
fig2_3_ax.set_yticks([0,25,50,75,100])

plt.subplots_adjust(wspace=0.35, hspace=0.55, bottom=0.2)
plt.savefig("2_scores_per_student_jan.png")
plt.close("all")

## Figure 3: boxplot scores male vs female
plt.figure(figsize=(10,8))
plt.suptitle("Test scores january males vs females", fontsize=16)
sb.set_palette("pastel")

# subplot 1
fig3_1_ax = plt.subplot(1,3,1)
sb.boxplot(data=scores, x="Gender", y="Score_test1")
fig3_1_ax.set_yticks([0,25,50,75,100])
plt.ylabel("Score")
plt.title("Test 1")

# subplot 2
fig3_2_ax = plt.subplot(1,3,2)
sb.boxplot(data=scores, x="Gender", y="Score_test2")
fig3_2_ax.set_yticks([0,25,50,75,100])
plt.ylabel("Score")
plt.title("Test 2")

# subplot 3
fig3_3_ax = plt.subplot(1,3,3)
sb.boxplot(data=scores, x="Gender", y="Score_test3")
fig3_3_ax.set_yticks([0,25,50,75,100])
plt.ylabel("Score")
plt.title("Test 3")

plt.subplots_adjust(wspace=0.35, hspace=0.55, bottom=0.2)
plt.savefig("3_boxplot_testscores_male_vs_female_jan.png")
plt.close("all")

# Figure 4: violin plots scores male vs female
plt.figure(figsize=(10,8))
plt.suptitle("Test scores january males vs females", fontsize=16)
sb.set_palette("pastel")

# subplot 1
fig4_1_ax = plt.subplot(1,3,1)
sb.violinplot(data=scores, x="Gender", y="Score_test1")
fig4_1_ax.set_yticks([0,25,50,75,100])
plt.ylabel("Score")
plt.title("Test 1")

# subplot 2
fig4_2_ax = plt.subplot(1,3,2)
sb.violinplot(data=scores, x="Gender", y="Score_test2")
fig4_2_ax.set_yticks([0,25,50,75,100])
plt.ylabel("Score")
plt.title("Test 2")

# subplot 3
fig4_3_ax = plt.subplot(1,3,3)
sb.violinplot(data=scores, x="Gender", y="Score_test3")
fig4_3_ax.set_yticks([0,25,50,75,100])
plt.ylabel("Score")
plt.title("Test 3")

plt.subplots_adjust(wspace=0.35, hspace=0.55, bottom=0.2)
plt.savefig("4_violinplot_testscores_male_vs_female_jan.png")
plt.close("all")

# Figure 5: pie charts passed per test
num_passed_test1 = len(scores[scores.Score_test1 >= 50])
num_failed_test1 = len(scores) - num_passed_test1 

num_passed_test2 = len(scores[scores.Score_test2 >= 50])
num_failed_test2 = len(scores) - num_passed_test2

num_passed_test3 = len(scores[scores.Score_test3 >= 50])
num_failed_test3 = len(scores) - num_passed_test3

plt.figure(figsize=(10,4))
plt.suptitle("Percentage of students passed tests January", fontsize=16)
sb.set_palette("colorblind")

# subplot 1
fig5_1_ax = plt.subplot(1,3,1)
plt.pie([num_passed_test1, num_failed_test1], autopct="%0.1f%%")
plt.axis('equal')
plt.legend(["Passed", "Failed"])
plt.title("Test 1")

# subplot 2
fig5_2_ax = plt.subplot(1,3,2)
plt.pie([num_passed_test2, num_failed_test2], autopct="%0.1f%%")
plt.axis('equal')
plt.legend(["Passed", "Failed"])
plt.title("Test 2")

# subplot 3
fig5_3_ax = plt.subplot(1,3,3)
plt.pie([num_passed_test3, num_failed_test3], autopct="%0.1f%%")
plt.axis('equal')
plt.legend(["Passed", "Failed"])
plt.title("Test 3")

plt.subplots_adjust(wspace=0.35, hspace=0.55)
plt.savefig("5_percentage_passed_tests_jan.png")
plt.close("all")
