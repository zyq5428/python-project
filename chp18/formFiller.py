#! python3
# formFiller.py - Automatically fills in the form.

import pyautogui, time

# Set these to the correct coordinates for your particular computer.
nameField = (625, 375)
submitButton = (586, 1109)
submitButtonColor = (119, 119, 180)
submitAnotherLink = (619, 241)

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
            ]

pyautogui.PAUSE = 0.5

for person in formData:
    # Give the user a chance to kill the script.
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)
    
    positionStr = 'Submit Button color '
    pixelColor = pyautogui.screenshot().getpixel((submitButton[0], submitButton[1]))
    positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
    positionStr += ', ' + str(pixelColor[1]).rjust(3)
    positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
    print(positionStr)

    # Wait until the form page has loaded.
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        time.sleep(0.5)

    print('Entering %s info...' % (person['name']))
    pyautogui.click(nameField[0], nameField[1])

    # Fill out the Name field.
    pyautogui.typewrite(person['name'] + '\t')

    # Fill out the Greatest Fear(s) field.
    pyautogui.typewrite(person['fear'] + '\t')

    # Fill out the Source of Wizard Powers field.
    if person['source'] == 'wand':
        #pyautogui.typewrite(['down', 'enter', '\t'])
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.press('\t')
    elif person['source'] == 'amulet':
        #pyautogui.typewrite(['down', 'down', 'enter', '\t'])
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.press('\t')
    elif person['source'] == 'crystal ball':
        #pyautogui.typewrite(['down', 'down', 'down', 'enter', '\t'])
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.press('\t')
    elif person['source'] == 'money':
        #pyautogui.typewrite(['down', 'down', 'down', 'down', 'enter', '\t'])
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.press('\t')

    # Fill out the Robocop field.
    if person['robocop'] == 1:
        #pyautogui.typewrite([' ', '\t'])
        pyautogui.press(' ')
        pyautogui.press('\t')
    elif person['robocop'] == 2:
        #pyautogui.typewrite(['right', '\t'])
        pyautogui.press('right')
        pyautogui.press('\t')
    elif person['robocop'] == 3:
        #pyautogui.typewrite(['right', 'right', '\t'])
        pyautogui.press('right')
        pyautogui.press('right')
        pyautogui.press('\t')
    elif person['robocop'] == 4:
        #pyautogui.typewrite(['right', 'right', 'right', '\t'])
        pyautogui.press('right')
        pyautogui.press('right')
        pyautogui.press('right')
        pyautogui.press('\t')
    elif person['robocop'] == 5:
        #pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])
        pyautogui.press('right')
        pyautogui.press('right')
        pyautogui.press('right')
        pyautogui.press('right')
        pyautogui.press('\t')

    # Fill out the Additional comments field.
    pyautogui.typewrite(person['comments'] + '\t')

    # Click Submit.
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Clicked Submit.')
    time.sleep(5)

    # Click the Submit another response link.
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
