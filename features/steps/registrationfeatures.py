from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from Utilities.configreader import ConfigReader
from features.pageobjects.loginpage import flipkart
import time
import logging
from Utilities import configreader
from Utilities.LogUtil import Logger
log = Logger(__name__, logging.INFO)

@given(u'we navigate to the Flipkart url')
def step_impl(context):
    #context.driver=webdriver.Chrome(ChromeDriverManager().install())
    context.reg = flipkart.fliphome(context)
    log.logger.info("Flipkart home page Navigated")

@given(u'close the login window')
def step_impl(context):
    context.reg = flipkart(context.driver)
    context.reg.clickclose()
    log.logger.info("Closed the login window")

@when(u'we hover over Login Button')
def step_impl(context):
    context.reg = flipkart(context.driver)
    context.reg.clickloginLink()
    log.logger.info("hovered over Login button")


@when(u'Click on SignUp Link')
def step_impl(context):
    context.reg.clickSignUpLink()
    time.sleep(5)
    log.logger.info("Clicked on Signup")


@then(u'we validate the new user text')
def step_impl(context):
    context.reg.validateText("Looks like you're new here!")
    log.logger.info("Validated to new user")


@then(u'we type in the "{number}" field')
def step_impl(context,number):
    context.reg.entermob(number)
    log.logger.info("Enter the number")


@then(u'Click on Continue button')
def step_impl(context):
    context.reg.continuebutton()
    log.logger.info("Clicked on Continue button")

@then(u'we type in "{password}" field')
def step_impl(context,password):
    context.reg.enterpass(password)
    log.logger.info("Entered Password")


@then(u'we click on the login button')
def step_impl(context):
    context.reg.clickSignUpbutton()
    log.logger.info("Clicked on login button")

