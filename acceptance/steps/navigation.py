from behave import *
from selenium import webdriver

from acceptance.page_model.login_page import LoginPage

use_step_matcher('re')


@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = LoginPage(context.driver)
    context.driver.get(page.url)


# @given('I am on the blog page')
# def step_impl(context):
#     context.driver = webdriver.Chrome()
#     page = BlogPage(context.driver)
#     context.driver.get(page.url)
#
#
# @given('I am on the new post page')
# def step_impl(context):
#     context.driver = webdriver.Chrome()
#     page = NewPostPage(context.driver)
#     context.driver.get(page.url)
#
#
# @then('I am on the blog page')
# def step_impl(context):
#     expected_url = BlogPage(context.driver).url
#     assert context.driver.current_url == expected_url
#
#
# @then('I am on the homepage')
# def step_impl(context):
#     expected_url = HomePage(context.driver).url
#     assert context.driver.current_url == expected_url
