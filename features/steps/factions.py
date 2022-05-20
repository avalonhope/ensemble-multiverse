from behave import given, when, then

@given(u'we have a faction A')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we have a faction A')


@given(u'we have a character C')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we have a character C')


@given(u'C is a member of faction A')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given C is a member of faction A')


@given(u'we have another faction B')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we have another faction B')


@given(u'faction B is not a subfaction of A')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given faction B is not a subfaction of A')


@given(u'faction A is not a subfaction of B')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given faction A is not a subfaction of B')


@when(u'C asks to join faction B')
def step_impl(context):
    raise NotImplementedError(u'STEP: When C asks to join faction B')


@then(u'C is not allowed to join faction B')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then C is not allowed to join faction B')
