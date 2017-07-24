from pages.basepage import LoginPage
from hamcrest import assert_that, equal_to

@given(u'I am on Login Page')
def step_impl(context):
    context.page_object = LoginPage(context.driver) #Informs who is the page_object (used feature)

@when(u'I click on Facebook button') #case sentitive
def step_impl(context):
    context.page_object.click_on_face_button() #called the function from page_object
