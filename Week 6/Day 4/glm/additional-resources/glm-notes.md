## The amazing, all-encompassing generalized linear models

#### Takeaways:

 * Choosing the right regression model for your data is simpler than it seems, if you have a basic understanding of the generalized linear model
 * GLMs have 3 components: stochastic, systematic, link function.
 * The systematic component never changes (it means: add the parts together). Otherwise, it's not a "linear" model.
 * The stochastic component should be chosen to represent the distribution of the observations.
     * for linear regression (GLM), the stochastic component is a normal distribution (continuous outcome variable, like height)
     * for logistic regression, the stochastic component is a Bernoulli distribution (binary outcome variable, like hired/not hired)
     * for poisson regression, the stochastic component is a Poisson distribution (count outcome, like number of parking tickets, or attendees)
 * the link function makes it possible to represent the outcome variables as continuous probability distributions.
     * linear regression uses the identity function (the outcome mean == the linear predictor)
     * logstic regression uses the logistic function
     * poisson regression uses log function


**More & Special cases:**

The Probit link allows extension of binary outcome variables to categorical (# categories > 2), and ordinal categorical (ranked categories).

The Gamma distribution can be used for  for proportional count response variable (like election results).

Funky models tobit, censored, and truncated regression are for data that are continuous but do not meet the stochastic assumption for normal distribution due to restrictions on the range of the response variable.
