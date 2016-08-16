# Lesson 3.2: Use Functions
# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!
# Get Python to do it for you!

# Use this space to describe your approach to the problem.
#
#
#
#

# Your code here.

import os


def rename_files():
    file_list = os.listdir(r"C:\Users\Cynikal\Google Drive\Udacity Nanodegree\Intro to Programming\udacity\Stage 3\lesson_3.2_using_functions\secret_message\prank")
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\Cynikal\Google Drive\Udacity Nanodegree\Intro to Programming\udacity\Stage 3\lesson_3.2_using_functions\secret_message\prank")
    for file_name in file_list:
        new_name = file_name.translate(None, "0123456789")
        os.rename(file_name, new_name)
        print "Old name: " + file_name+"\nNew name: " + new_name
    os.chdir(saved_path)
print rename_files()
