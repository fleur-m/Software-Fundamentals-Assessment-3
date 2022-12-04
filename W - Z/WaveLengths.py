# WaveLengths.py
#
# @ author: A. N. Other
# date: September 2016

# program that displays colour of wavelength chosen by user.

print("Welcome to wavelength to colour converter\n")
waveLength = int(input("Please enter a number of wavelength between 380 and 750\n"))
print("Thank you, the wavelength that you entered in nanometres is", waveLength, "\n")
print("The colour for this wavelength is...", end="")

if waveLength > 750:
    print("The wavelength entered is higher than the visible spectrum! This is infrared.")
elif waveLength >= 620:
    print("Red")
elif waveLength >= 590:
    print("Orange")
elif waveLength >= 570:
    print("Yellow")
elif waveLength >= 495:
    print("Green")
elif waveLength >= 450:
    print("Blue")
elif waveLength >= 380:
    print("Violet")
else:
    print("Indeterminate, :-(, the number entered is "
          "outside the visible spectrum!")

# Test case assertion 1:
'''
waveLength = 385
colour is violet
'''

# Test case assertion 2:
'''
waveLength = 6
else: "Indeterminate"
'''