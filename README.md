# USB Mouse Artist - sparkly Heart Drawer 

<img width="647" height="615" alt="image" src="https://github.com/user-attachments/assets/39be765d-b3a8-40cf-ba01-f578e1b47a0f" />

Vidoe of What the code does :
[![Video](https://img.icons8.com/fluency/48/video-playlist.png)](https://hackclub.slack.com/files/U092H9HRZDE/F09Q1CA7BD3/screen_recording_2025-11-01_170926.mp4)

**Theme** HID Mouse + Keyboard Control 


## What the script does 

This project turns to use the PICO Ducky to do some thing lovely : 
1. It automatically opens the MS paint on windows
2. draws a sparkly heart with particles 
3. Adds a signature for the drawing 
4. and a uate that will motivate if you are down :)

## requirements 

### Hardware 
- **Raspberry Pi Pico** (or Pico W)
- USB cable to connect to your computer

## Files 

boot.py
code.py 
paint_artist_test.py  (this is coded to test directly in my PC to check if any errors ect...)

## Drawing the Heart 
uses parametric eautions for the heart shape 
```python
x = 16 * sin^3(t)
y = -(13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))
```

# Sparkly Effect 
- Draws 300+ particles around the heart outline
- Adds random noise / offset to each point 
- 30% chance for extra sparkle particles
- create the glittery effect on the heart 

## Problems encountered from the project and how I overcame them 

paint didnt open for the first try so added a increased wait time 

## What I learned 
-USB HID protocol ( Keyboard + mouse)
- parametric euations from drawing shapes
- random particle effects
-windows automation 
- smooth mouse movement algorithms



This was  real game changer on learning on automation on how good and bad this can be used to I like how ppl would react to like an automation like painting a full picture just by pluggin a PICO device :)
(Note in the code add signature I generalised and leaved it to any one intrested to add a there own letters ect )


