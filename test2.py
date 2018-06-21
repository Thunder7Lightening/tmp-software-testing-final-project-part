# -*- coding: utf-8 -*-
import os
import glob
import unittest
import time

# from selenium import webdriver
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestMyApp(unittest.TestCase):

    def setUp(self):
        app = os.path.abspath(glob.glob(os.path.dirname(__file__)
                                        + './*.apk')[0])
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '4.3.1',
            'deviceName': 'emulator-5554',
            'app': app,
            'noReset': False,
            'app-package': 'it.feio.android.omninotes',
            'app-activity': 'it.feio.android.omninotes.*',
            'appWaitActivity': 'it.feio.android.omninotes.*'
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                       desired_caps)

    # def test01_inputing_empty_category_title(self):
    #     driver = self.driver
    #     # at welcome page
    #     nextButton = driver.find_element_by_id("it.feio.android.omninotes:id/next")
    #     nextButton.click()
    #     nextButton.click()
    #     nextButton.click()
    #     nextButton.click()
    #     nextButton.click()
    #     doneButton = driver.find_element_by_id("it.feio.android.omninotes:id/done")
    #     doneButton.click()
    #     # # at version change log
    #     # okButton = driver.find_element_by_id("it.feio.android.omninotes:id/buttonDefaultPositive")
    #     # okButton.click()
    #     # entering edit note page
    #     addButton = driver.find_element_by_id("it.feio.android.omninotes:id/fab_expand_menu_button")
    #     addButton.click()
    #     textNoteButton = driver.find_element_by_id("it.feio.android.omninotes:id/fab_note")
    #     textNoteButton.click()
    #     # press category icon
    #     categoryIcon = driver.find_element_by_id("it.feio.android.omninotes:id/menu_category")
    #     categoryIcon.click()
    #     # add a new category with empty title
    #     addCategoryButton = driver.find_element_by_id("it.feio.android.omninotes:id/buttonDefaultPositive")
    #     addCategoryButton.click()
    #     okButton = driver.find_element_by_id("it.feio.android.omninotes:id/save")
    #     okButton.click()

    # def test02_creating_a_note_and_move_it_to_cat_1(self):
    #     driver = self.driver
    #     # at welcome page
    #     nextButton = driver.find_element_by_id("it.feio.android.omninotes:id/next")
    #     nextButton.click()
    #     nextButton.click()
    #     nextButton.click()
    #     nextButton.click()
    #     nextButton.click()
    #     doneButton = driver.find_element_by_id("it.feio.android.omninotes:id/done")
    #     doneButton.click()
    #     # # at version change log
    #     # okButton = driver.find_element_by_id("it.feio.android.omninotes:id/buttonDefaultPositive")
    #     # okButton.click()
    #     # entering edit note page
    #     # at index page
    #     addButton = driver.find_element_by_id("it.feio.android.omninotes:id/fab_expand_menu_button")
    #     addButton.click()
    #     textNoteButton = driver.find_element_by_id("it.feio.android.omninotes:id/fab_note")
    #     textNoteButton.click()
    #     # at edit note page
    #     titleTextfield = driver.find_element_by_id("it.feio.android.omninotes:id/detail_title")
    #     titleTextfield.send_keys("new note")
    #     contentTextfield = driver.find_element_by_id("it.feio.android.omninotes:id/detail_content")
    #     contentTextfield.send_keys("content")
    #     # press category icon
    #     categoryIcon = driver.find_element_by_id("it.feio.android.omninotes:id/menu_category")
    #     categoryIcon.click()
    #     # add a new category
    #     addCategoryButton = driver.find_element_by_id("it.feio.android.omninotes:id/buttonDefaultPositive")
    #     addCategoryButton.click()
    #     categoryTitleTextfield = driver.find_element_by_id("it.feio.android.omninotes:id/category_title")
    #     categoryTitleTextfield.send_keys("cat 1")
    #     colorIcon = driver.find_element_by_id("it.feio.android.omninotes:id/color_chooser")
    #     colorIcon.click()
    #     aColorIcon = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.GridView/android.widget.FrameLayout[10]")
    #     aColorIcon.click()
    #     aShadowColorIcon = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.GridView/android.widget.FrameLayout[1]")
    #     aShadowColorIcon.click()
    #     doneButton = driver.find_element_by_id("it.feio.android.omninotes:id/buttonDefaultPositive")
    #     doneButton.click()
    #     okButton = driver.find_element_by_id("it.feio.android.omninotes:id/save")
    #     okButton.click()
    #     # back to index page
    #     backToInedexButton = driver.find_element_by_accessibility_id("drawer open")
    #     backToInedexButton.click()
    #     # call side bar
    #     sideBarButton = driver.find_element_by_accessibility_id("drawer open")
    #     sideBarButton.click()
    #     # press cat 1
    #     time.sleep(2)
    #     cat1Button = driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'cat 1')]")
    #     cat1Button.click()


    # def test03_select_note_and_remove_its_category(self):
    #     driver = self.driver
    #     # at welcome page
    #     nextButton = driver.find_element_by_id("it.feio.android.omninotes:id/next")
    #     nextButton.click()
    #     nextButton.click()
    #     nextButton.click()
    #     nextButton.click()
    #     nextButton.click()
    #     doneButton = driver.find_element_by_id("it.feio.android.omninotes:id/done")
    #     doneButton.click()
    #     # # at version change log
    #     # okButton = driver.find_element_by_id("it.feio.android.omninotes:id/buttonDefaultPositive")
    #     # okButton.click()
    #     # entering edit note page
    #     # at index page
    #     addButton = driver.find_element_by_id("it.feio.android.omninotes:id/fab_expand_menu_button")
    #     addButton.click()
    #     textNoteButton = driver.find_element_by_id("it.feio.android.omninotes:id/fab_note")
    #     textNoteButton.click()
    #     # at edit note page
    #     titleTextfield = driver.find_element_by_id("it.feio.android.omninotes:id/detail_title")
    #     titleTextfield.send_keys("new note")
    #     contentTextfield = driver.find_element_by_id("it.feio.android.omninotes:id/detail_content")
    #     contentTextfield.send_keys("content")
    #     # press category icon
    #     categoryIcon = driver.find_element_by_id("it.feio.android.omninotes:id/menu_category")
    #     categoryIcon.click()
    #     # add a new category
    #     addCategoryButton = driver.find_element_by_id("it.feio.android.omninotes:id/buttonDefaultPositive")
    #     addCategoryButton.click()
    #     categoryTitleTextfield = driver.find_element_by_id("it.feio.android.omninotes:id/category_title")
    #     categoryTitleTextfield.send_keys("cat 1")
    #     colorIcon = driver.find_element_by_id("it.feio.android.omninotes:id/color_chooser")
    #     colorIcon.click()
    #     aColorIcon = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.GridView/android.widget.FrameLayout[10]")
    #     aColorIcon.click()
    #     aShadowColorIcon = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.GridView/android.widget.FrameLayout[1]")
    #     aShadowColorIcon.click()
    #     doneButton = driver.find_element_by_id("it.feio.android.omninotes:id/buttonDefaultPositive")
    #     doneButton.click()
    #     okButton = driver.find_element_by_id("it.feio.android.omninotes:id/save")
    #     okButton.click()
    #     # back to index page
    #     backToInedexButton = driver.find_element_by_accessibility_id("drawer open")
    #     backToInedexButton.click()
    #     # call side bar
    #     sideBarButton = driver.find_element_by_accessibility_id("drawer open")
    #     sideBarButton.click()
    #     # press cat 1
    #     time.sleep(2)
    #     cat1Button = driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'cat 1')]")
    #     cat1Button.click()

    #     # at cat 1, select note
    #     time.sleep(2)
    #     note = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout")
    #     TouchAction(driver).long_press(note).wait(3000).perform()
    #     # press category icon
    #     categoryIcon = driver.find_element_by_id("it.feio.android.omninotes:id/menu_category")
    #     categoryIcon.click()
    #     # remove its category
    #     removeCategoryButton = driver.find_element_by_id("it.feio.android.omninotes:id/buttonDefaultNegative")
    #     removeCategoryButton.click()
    #     # call side bar
    #     sideBarButton = driver.find_element_by_accessibility_id("drawer open")
    #     sideBarButton.click()
    #     # press Notes
    #     time.sleep(2)
    #     NotesButton = driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'it.feio.android.omninotes:id/title') and @text='Notes']")
    #     NotesButton.click()








    def test_managing_notes_using_category(self):
        driver = self.driver
        # scenario1: create a new note, edit it by adding a new category, and final check if move to category successfully
        # at welcome page
        nextButton = driver.find_element_by_id("it.feio.android.omninotes:id/next")
        nextButton.click()
        nextButton.click()
        nextButton.click()
        nextButton.click()
        nextButton.click()
        doneButton = driver.find_element_by_id("it.feio.android.omninotes:id/done")
        doneButton.click()
        # at version change log
        okButton = driver.find_element_by_id("it.feio.android.omninotes:id/buttonDefaultPositive")
        okButton.click()
        # create a note
        addButton = driver.find_element_by_id("it.feio.android.omninotes:id/fab_expand_menu_button")
        addButton.click()
        textNoteButton = driver.find_element_by_id("it.feio.android.omninotes:id/fab_note")
        textNoteButton.click()
        titleTextfield = driver.find_element_by_id("it.feio.android.omninotes:id/detail_title")
        titleTextfield.send_keys("new note")
        contentTextfield = driver.find_element_by_id("it.feio.android.omninotes:id/detail_content")
        contentTextfield.send_keys("content")
        backToInedexButton = driver.find_element_by_accessibility_id("drawer open")
        backToInedexButton.click()
        # click a note
        selectedNote = driver.find_element_by_id("it.feio.android.omninotes:id/note_content")
        selectedNote.click()
        # press categoryIcon
        categoryIcon = driver.find_element_by_id("it.feio.android.omninotes:id/menu_category")
        categoryIcon.click()
        # add a new category
        addCategoryButton = driver.find_element_by_id("it.feio.android.omninotes:id/buttonDefaultPositive")
        addCategoryButton.click()
        categoryTitleTextfield = driver.find_element_by_id("it.feio.android.omninotes:id/category_title")
        categoryTitleTextfield.send_keys("cat 1")
        colorIcon = driver.find_element_by_id("it.feio.android.omninotes:id/color_chooser")
        colorIcon.click()
        aColorIcon = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.GridView/android.widget.FrameLayout[10]")
        aColorIcon.click()
        aShadowColorIcon = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.GridView/android.widget.FrameLayout[1]")
        aShadowColorIcon.click()
        doneButton = driver.find_element_by_id("it.feio.android.omninotes:id/buttonDefaultPositive")
        doneButton.click()
        okButton = driver.find_element_by_id("it.feio.android.omninotes:id/save")
        okButton.click()
        # backToInedexButton
        TouchAction(driver).tap(x=43, y=892).perform()
        backToInedexButton = driver.find_element_by_accessibility_id("drawer open")
        backToInedexButton.click()
        TouchAction(driver).tap(x=43, y=892).perform()
        # call side bar
        sideBarButton = driver.find_element_by_accessibility_id("drawer open")
        sideBarButton.click()
        # press cat 1
        time.sleep(2)
        cat1Button = driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'cat 1')]")
        cat1Button.click()

        # scenario2: now at cat 1 page, create an another note, check if the new one is at cat 1 page
        # create a note
        addButton = driver.find_element_by_id("it.feio.android.omninotes:id/fab_expand_menu_button")
        addButton.click()
        textNoteButton = driver.find_element_by_id("it.feio.android.omninotes:id/fab_note")
        textNoteButton.click()
        titleTextfield = driver.find_element_by_id("it.feio.android.omninotes:id/detail_title")
        titleTextfield.send_keys("another new note")
        contentTextfield = driver.find_element_by_id("it.feio.android.omninotes:id/detail_content")
        contentTextfield.send_keys("another content")
        backToInedexButton = driver.find_element_by_accessibility_id("drawer open")
        backToInedexButton.click()

        # scenario3: now at cat 1 page, move anotherNewNote from cat1 to cat2, check by going to cat2
        # click anotherNewNote
        anotherNewNote = driver.find_element_by_id("it.feio.android.omninotes:id/note_content")
        anotherNewNote.click()
        # press categoryIcon
        categoryIcon = driver.find_element_by_id("it.feio.android.omninotes:id/menu_category")
        categoryIcon.click()
        # add a new category named cat 2
        addCategoryButton = driver.find_element_by_id("it.feio.android.omninotes:id/buttonDefaultPositive")
        addCategoryButton.click()
        categoryTitleTextfield = driver.find_element_by_id("it.feio.android.omninotes:id/category_title")
        categoryTitleTextfield.send_keys("cat 2")
        colorIcon = driver.find_element_by_id("it.feio.android.omninotes:id/color_chooser")
        colorIcon.click()
        aColorIcon = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.GridView/android.widget.FrameLayout[1]")
        aColorIcon.click()
        aShadowColorIcon = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.GridView/android.widget.FrameLayout[1]")
        aShadowColorIcon.click()
        doneButton = driver.find_element_by_id("it.feio.android.omninotes:id/buttonDefaultPositive")
        doneButton.click()
        okButton = driver.find_element_by_id("it.feio.android.omninotes:id/save")
        okButton.click()
        # backToInedexButton
        TouchAction(driver).tap(x=43, y=892).perform()
        backToInedexButton = driver.find_element_by_accessibility_id("drawer open")
        backToInedexButton.click()
        TouchAction(driver).tap(x=43, y=892).perform()
        # call side bar
        sideBarButton = driver.find_element_by_accessibility_id("drawer open")
        sideBarButton.click()
        # press cat 2
        time.sleep(2)
        cat2Button = driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'cat 2')]")
        cat2Button.click()
        
        # scenario4: now at cat 2 page, remove category of anotherNewNote, check by going to cat2 and then going to Notes page
        # click anotherNewNote
        anotherNewNote = driver.find_element_by_id("it.feio.android.omninotes:id/note_content")
        anotherNewNote.click()
        # press categoryIcon
        categoryIcon = driver.find_element_by_id("it.feio.android.omninotes:id/menu_category")
        categoryIcon.click()
        # remove category of anotherNewNote
        removeCategoryButton = driver.find_element_by_id("it.feio.android.omninotes:id/buttonDefaultNegative")
        removeCategoryButton.click()
        # backToInedexButton
        TouchAction(driver).tap(x=43, y=892).perform()
        backToInedexButton = driver.find_element_by_accessibility_id("drawer open")
        backToInedexButton.click()
        TouchAction(driver).tap(x=43, y=892).perform()
        # call side bar
        sideBarButton = driver.find_element_by_accessibility_id("drawer open")
        sideBarButton.click()
        # press Notes
        time.sleep(2)
        NotesButton = driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'it.feio.android.omninotes:id/title') and @text='Notes']")
        NotesButton.click()

        

    # def tearDown(self):
    #     self.driver.quit()

if __name__ == '__main__':
    unittest.main()


    #android.widget.ImageButton