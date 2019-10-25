#### Pair Problem

**Practice LASSO regularization technique in five steps**:

1. Load the diabetes dataset from sklearn (sklearn.datasets.load_diabetes()). Note that the data is already scaled. Or, try and make your own randomly generated data!

2. Use the KFold function from sklearn's cross validation module to divide the data into 5 training/test sets. Randomize the KFolds (via the shuffle parameter with a random state you seed).

3. Tune the lambda (or per sklearn, alpha) parameter in the LASSO model by looping over a grid of possible lambdas.

        * For each candidate lambda, loop over the 5 training/test sets.
        * On each training/test set run the LASSO model on the training set and then compute and record the prediction errors on the train/test sets.
        * Finally, total the prediction error for the 5 training/test sets.
4. Set lambda to be the value that minimizes prediction error. Run the LASSO model again with the optimal lambda determined in step 3. Which variables would you consider excluding on the basis of these results?

5. What next steps would you take from here? Extra credit: try feature engineering, other models, plotting, etc. Compare your results.