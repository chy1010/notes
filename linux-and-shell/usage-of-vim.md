# vim modes

## normal mode

By default, vim starts in normal mode. In normal mode, some key presses can move the cursor, manipulate the contents and enter other modes.

### basic movements

- `h`: move one char left
- `j`: move one row down
- `k`: move one row up
- `l`: move one char right

The row movement can be prefixed by a number:

- `4j`: move 4 rows down
- `5k`: move 5 rows up

### word movements

- `w`: move to the beginning of the next word
- `b`: move to the previous beginning of word
- `e`: move to the end of the word
- `W`: move to beginning of next word after a whitespace
- `B`: move to the previous beginning of word before a whitespace
- `E`: move to the end of the word before a white space

### line

- `0`, `^`: move to the beginning of the line
- `$`: move to the end of the line


## enter insert mode

- `i`: insert mode
- `a`: move the cursor after the current charater and enter insert mode
- `o`: inserts a new line below the current line and enters inert mode on the new line

- `I`: moves the cursor to the beginning of the line and enters insert mode
- `A`: moves the cursor to the end of the line and enters insert mode
- `O`: inserts a new line above the current one and enters insert mode on the new line

## enter search mode

- `/`: use regular expression and enter into the search mode
    * `n`: in search mode, go to the next target
    * `N`: in serach mode, go back to the previous


### enter visual mode
- `v`: visual mode

### enter command mode

- `:`: enter command mode



### delete mode

- `d`: enter delete mode, and press the following key:
    - `d`: delete the line that the cursor at.
    - `$`: delete the rest part after the cursor of the same line.
    - `0` or `^`: delete the part from the beginning of the line to the position at which the cursor is.