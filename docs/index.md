# Welcome to OCVID
## OpenCV Integrated Development Environment

OCVID was born from a desire to make learning with OpenCV a lot easier; instead of having to go through the effort and pain of finding and installing a version of python and opencv as well as some test files and look up some basic tutorial code, I wanted to bundle it all so you could do one download/install and get straight into it.

Furthermore, I hope this can grow into a handy prototyping tool and code reference, an easy way to quickly hammer out an opencv frame filter.

# Release 

Currently there's just a basic shell of an interface which can be installed on Windows or run on Linux.  But you can't actually do anything with it.  More to come! :)

## Current features
GUI with a text input field, an input frame and an output frame.  No major GUI additions planned - this should be what the final one looks like; the only thing that might need to be captured is a "record" button / filename, as well as a way to report runtime errors (output frame overlay?)

## Planned features
### Stream
* Open any image file
* Open any camera accessible by the computer
* Open any video file
* For any video stream, pause/step or play.
* Save any processed frame to disk.
* Record a processed video to disk.
* Fishtank resource files (it's how I learned, after all).

### Editor
* Add the ability to actually run code on a frame (lol)
* Report compile-time errors before trying to run it
* Gracefully catch and report runtime errors.
* Code structure - preamble and postamble.
* Save and load python code as standalone runnable .py's 
* Code examples (commented & easy to understand/change) which work on the resource media files.
* Learning exercises - function stubs with comments and instructions to teach people how to do a variety of vision tasks.
* Syntax highlighting
* Intellisense
* List of OpenCV Functions
* Link to relevant API references

### Vision Builder
Note: This is currently just a v2.0 pipedream -- expect in a deep future release.
* Sub-tool for easily creating python code, similar to existing COTS solutions
* Pipeline common opencv functions
* Parameter preview -- sliders with live updates for thresholding, e.g.

# How can I help?

I truly hope this system helps you in your learning, teaching or development. 

If there are any features you want or bugs you found, feel free to [raise an issue](https://github.com/frewes/OCVID/issues).

Otherwise, you can also [contact me directly](mailto:fredrik.westling@gmail.com)

Finally, if you want to help support development, or just show your thanks, buy me a coffee below :).  If you include a message with a bug or feature request I'll make sure to prioritise it!

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](paypal.me/fwestling)
