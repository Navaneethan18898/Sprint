from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from Utilities.configreader import ConfigReader
from features.pageobjects.loginpage import flipkart
import time

@given(u'we navigate to the Flipkart url')
def step_impl(context):
    #context.driver=webdriver.Chrome(ChromeDriverManager().install())
    context.reg = flipkart.fliphome(context)

@given(u'close the login window')
def step_impl(context):
    context.reg = flipkart(context.driver)
    context.reg.clickclose()

@when(u'we hover over Login Button')
def step_impl(context):
    context.reg = flipkart(context.driver)
    context.reg.clickloginLink()


@when(u'Click on SignUp Link')
def step_impl(context):
    context.reg.clickSignUpLink()
    time.sleep(5)


@then(u'we validate the new user text')
def step_impl(context):
    context.reg.validateText("Looks like you're new here!")


@then(u'we type in the "{number}" field')
def step_impl(context,number):
    context.reg.entermob(number)

@then(u'Click on Continue button')
def step_impl(context):
    context.reg.continuebutton()

@then(u'we type in "{password}" field')
def step_impl(context,password):
    context.reg.enterpass(password)


@then(u'we click on the login button')
def step_impl(context):
    context.reg.clickSignUpbutton()

