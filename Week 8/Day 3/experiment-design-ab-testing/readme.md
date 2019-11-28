# Sample Lesson Plan

0. (strongly recommended) Pair problem
1. [Hypothesis testing review and power](./Hypothesis_test_review_and_power.ipynb) (45 mins)
2. [AB Testing issues](./AB_Testing_Issues.ipynb) (25 mins)

Would strongly recommend doing the pair problem on factory failures the morning of this lecture. This pair problem allows students to see via simulation the idea of preparing a large enough sample.

# Learning Objectives

Students should come away with the following ideas:
* How to plan a hypothesis test, and why this should be done _before_ the experiment starts.
* What a power calculation is, and how the sample size depends on the power.
* The problems with 'early peeking' / 'early stopping', and hence why doing a power calculation is important.
* How to do a post hoc analysis of a hypothesis test (i.e. make a decision). This should be review from the hypothesis test lecture.
* Understanding of buisness cycles, and the 'novelty effect' in A/B tests (e.g. neglecting first week of results).
	These are generally hard problems, and there is no one-size fits all analysis. Be prepared to do some analysis to determine
	whether there is a novelty effect, and what its duration is.
* Have a qualitative understanding of the strengths and weaknesses of MAB vs hypothesis testing.

# Depends On


# Additional Resources

Some subset of these topics can be covered based on the interests of the instructor. If we expand A/B testing to be a larger part of the
course, these would be a good place to start developing material.

## Bonferroni correction

How to adjust for multiple comparisons. For the interested instructor, this would be easy to add, because we almost cover the
[Bonferroni correction](https://en.wikipedia.org/wiki/Bonferroni_correction) when looking at multiple comparisons. If there are
$N$ alternatives to the control, the BC is to take $\alpha \rightarrow \alpha/N$. This will control the probability of making a
Type I error (i.e. accepting an incorrect hypothesis).

Note if going down this route, the statement of how the BC interacts with statistical power is non-trivial.

## Simpson's Paradox

This would be a good lesson to introduce Simpson's Paradox, if time permits. This is important because in A/B testing the question of whether to
do the tests pre-segmentation or post-segmentation can have a significant impact.

Briefly Simpson's Paradox is the statement that we can have two variations A and B where B is preferred when looking at the population as a whole,
but when we partition the population into segments it is possible that every segment prefers A. This seems like a contradiction (if every segment prefers variation A, shouldn't the whole population?) but if the rates of interaction and approval are different across segments, it is possible for B to have a higher weighted average.