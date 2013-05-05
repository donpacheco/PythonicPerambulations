Title: Minesweeper in Matplotlib
date: 2012-12-06 18:23
comments: true

<!-- PELICAN_BEGIN_SUMMARY -->
Lately I've been playing around with interactivity in matplotlib.  A couple
weeks ago, I discussed briefly how to use event callbacks to implement
[simple 3D visualization](/blog/2012/11/24/simple-3d-visualization-in-matplotlib/)
and later used this as a base for creating a
[working 3D Rubik's cube](/blog/2012/11/26/3d-interactive-rubiks-cube-in-python)
entirely in matplotlib.

Today I have a different goal: re-create
[minesweeper](http://en.wikipedia.org/wiki/Minesweeper_%28computer_game%29),
that ubiquitous single-player puzzle game that most of us will admit to
having binged on at least once or twice in their lives.  In minesweeper, the
goal is to discover and avoid hidden mines within a gridded minefield, and
the process takes some logic and quick thinking.

{% img /downloads/images/minesweeper_2.gif 800 %}

<!-- PELICAN_END_SUMMARY -->

To implement this in matplotlib, at its most stripped-down level, simply
requires us to register mouse clicks on the plot window, and to have the
window respond in the appropriate way.  The rest is just the logic underneath.

## Event Callbacks ##
Matplotlib contains several built-in event callbacks.  You can register
key presses (with ``'key_press_event'`` and ``'key_release_event'``),
mouse clicks (with ``'button_press_event'`` and ``'button_release_event'``),
mouse movement (with ``'motion_notify_event'``), and much more.  For
a full listing of the events that can be bound to functionality, see the
documentation of the function ``'matplotlib.pyplot.connect'``.

As a simple example, here we'll create a polygon and a function which is called
each time the axis is clicked.  The function ``on_click`` checks if the click
occured within the polygon, and if so changes the polygon to a random
color:

``` python
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, xlim=(-1, 2), ylim=(-1, 2))
polygon = plt.Polygon([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
ax.add_patch(polygon)

# Function to be called when mouse is clicked
def on_click(event):
    if polygon.contains_point((event.x, event.y)):
        polygon.set_facecolor(np.random.random(3))
        fig.canvas.draw()

# Connect the click function to the button press event
fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()
```
The result will look something like this:

{% img /downloads/images/poly_color.gif  400 %}

Checking whether a click event is within a polygon or any other artist is
a very common pattern.  For this reason, matplotlib provides a built-in
 ``pick`` event.  You can think of this as an event similar to a mouse click,
but specifically generated by a plot artist when it is clicked.
Furthermore, a ``pick`` event is associated back to that particular plot
element, which can be easily referenced within the callback.
Here is a code snippet which gives is equivalent to the code above,
but uses pick events rather than button press events:

``` python
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, xlim=(-1, 2), ylim=(-1, 2))
polygon = plt.Polygon([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
ax.add_patch(polygon)

# set the picker to True, so that pick events are registered
polygon.set_picker(True)

# create a function to be bound to pick events: here the event has an
# attribute `artist` which points to the object which was clicked
def on_pick(event):
    event.artist.set_facecolor(np.random.random(3))
    fig.canvas.draw()

# bind pick events to our on_pick function
fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()
```

Here we have used just a single polygon, but there's nothing to stop us
from using multiple interactive polygons in a single window.  Add some
logic beneath it all, and the results can be extremely flexible.  We'll
go through one in-depth example below.

## Minesweeper ##
Using this simple machinery, let's create a basic implementation of the game
Minesweeper.  This involves creating a grid of polygons, with a certain number
of them "containing" mines.  Clicking the left mouse button will "uncover"
the square, ending the game if a mine is underneath.  If (as we'd hope)
an uncovered square does not contain a mine, it will reveal a number
reporting how many of the eight adjacent squares contain mines.
The right mouse button is used to mark where we believe mines are.

There are some other more sophisticated features in the below code --
for example, clicking
an already uncovered square with the correct number of adjacent mines marked
will automatically clear the surrounding squares -- but rather than enumerating
every programming decision, I'll just show you the code.  It's less than
200 lines, but the results are pretty nice:

{% img /downloads/images/minesweeper.gif 440 440 %}

{% include_code  minesweeper.py Minesweeper %}

There are still some things missing from this which are present in any good
minesweeper implementation: a timer, the ability to reset the game without
restarting the program, the ability to keep track of fastest times, and
likely some more things I haven't thought of.

Regardless, this little script shows how incredibly powerful a framework
matplotlib is.
It can create an interactive Rubik's cube one day, publication-quality plots
the next, and round out the season with a blast back to a classic Windows 3.1
time-sink.  And for some reason, I find I have much more fun playing the
minesweeper I built from scratch than the one that came with my system.

Enjoy!