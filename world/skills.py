import icontract

@icontract.ensure(lambda result: result > = 1.0)
def proficiency (experience):
    """
    Calculate a charcater's skill proficency level based on experience points.

    The result is 1 plus one tenth of the cube root of the experience points.

    For example: 1000 experience points gives a proficency of 2.0.
    """
    if experience <= 0:
        return 1.0
    return 1.0 + 0.1 * round(experience ** 0.33333, 1)

