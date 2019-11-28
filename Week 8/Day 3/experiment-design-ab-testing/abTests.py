from collections import namedtuple
from scipy.stats import norm
import numpy as np

variation = namedtuple('variation', 'clicks impressions')


def draw_clicks_from_n_samples(impressions, prob_click, num_trials):
    """
    Simulate a binomial process where `impressions` people view a link,
    and have a probability `prob_click` of clicking on it. Repeat this
    process `num_trials` times, returning the number of clicks in each
    trial.

    Can be viewed as repeated Bernoulli trials.

    Parameters:
    -----------
    impressions: the "N" of a single Bernoulli trial
    prob_click: the probability of success in a single trial (click or not)
    num_trials: the number of times the Bernoulli trails are repeated

    Returns:
    --------
    An array of integers of length `num_trials`, representing the number of
    times the link was clicked on each trial
    """
    return np.random.binomial(impressions, prob_click, size=(num_trials, ))


def draw_p_sample_from_n_samples(impressions, prob_click, num_trials):
    """
    Simulate a binomial process where `impressions` people view a link,
    and have a probability `prob_click` of clicking on it. Repeat this
    process `num_trials` times, returning the fraction of clicks in each
    trial. The fraction should be peaked around `prob_click`.

    Can be viewed as repeated Bernoulli trials.

    Parameters:
    -----------
    impressions: the "N" of a single Bernoulli trial
    prob_click: the probability of success in a single trial (click or not)
    num_trials: the number of times the Bernoulli trails are repeated

    Returns:
    --------
    An array of floats of length `num_trials`, representing the fraction of
    times the link was clicked on each trial
    """
    return draw_clicks_from_n_samples(impressions, prob_click,
                                      num_trials)/impressions


def get_p_value_from_simulation(num_simulations, variation_A, variation_B):
    """
    Simulates random processes under the assumption treatment A and treatment B
    are equally effective (the null hypothesis).

    Simulation for A runs `A.impressions` times, simulation for B runs `B.impressions` times.
    The simulation is repeated num_simulations times. Returns the fraction of simulations
    which have a difference in proportion as large as the one actually observed. This
    is a simulation measurement of the p-value.

    Parameters:
    -----------
    num_simulations: the number of simulations to run
    variation_A: a variation namedtuple. Contains the actual result of variation_A
    variation_B: a variation namedtuple. Contains the actual result of variation_B

    Returns:
    --------
    The p-value (that is, the fraction of random trials that saw an effect as large as
    the one observed)
    """
    imp_A, imp_B = variation_A.impressions, variation_B.impressions
    click_A, click_B = variation_A.clicks, variation_B.clicks

    p = (click_A + click_B)/(imp_A + imp_B)

    difference_in_rate = abs(click_A/imp_A - click_B/imp_B)

    p_A_array = draw_p_sample_from_n_samples(imp_A, p, num_simulations)
    p_B_array = draw_p_sample_from_n_samples(imp_B, p, num_simulations)
    result_by_chance = (abs(p_B_array - p_A_array) > difference_in_rate)
    return sum(result_by_chance)/len(result_by_chance)


def get_p_value_analytic(variationA, variationB):
    """
    Calculates the p-value for the difference in rates between variationA and variationB.

    Parameters:
    -----------
    variation_A: a variation namedtuple. Contains the actual result of variation_A
    variation_B: a variation namedtuple. Contains the actual result of variation_B

    Returns:
    --------
    The p-value (float)
    """
    p_A, p_B = (variationA.clicks/variationA.impressions,
                variationB.clicks/variationB.impressions)
    p = (variationA.clicks + variationB.clicks)/(
        variationA.impressions + variationB.impressions)
    variance = p*(1 - p)/variationA.impressions + p*(
        1 - p)/variationB.impressions

    abs_z = abs(p_A - p_B)/np.sqrt(variance)

    p_value = 2*(1 - norm.cdf(abs_z))
    return p_value


def power_function(p_A_base, DeltaPi, alpha=0.05, beta=0.8):
    """
    Calculates the number of subjects needed for each of two variations for a valid
    A/B test.

    Parameters:
    -----------
    p_A_base: the lower of the two rates (usually the control). Between 0 and 1.
    DeltaPi: the "minimum difference" used to determine beta.
    alpha: The type-I error rate. This is the percentage of times a result would be
        detected if there was no difference.
    beta: The type-II error rate. This is the percentage of times a result would not
        be detected if it was the size of DeltaPi.

    Returns:
    --------
    The number of subjects needed for each variation.
    """
    p_B = p_A_base + DeltaPi
    p = 0.5*(p_A_base + p_B)

    z2 = abs(norm.ppf(1 - beta))
    z_crit = norm.ppf(1 - alpha/2)
    root_N = (z2*np.sqrt(p_A_base*(1 - p_A_base) + p_B*
                         (1 - p_B)) + z_crit*np.sqrt(2*p*(1 - p)))/DeltaPi
    return int(np.ceil(root_N**2))


# Runs a test, if executed from the command line
# Ignored if imported
if __name__ == '__main__':
    test_case = {'p_A_base': 0.02, 'DeltaPi': 0.01, 'alpha': 0.05, 'beta': 0.8}

    num_subjects = power_function(**test_case)

    print("""
    The number of subjects needed to detect a different of {DeltaPi} percentage points
    is {num_subjects} (alpha = {alpha}, beta={beta})
    """.format(num_subjects=num_subjects, **test_case))
