#! /bin/bash

# source this file and use top_history to show this
# since history does not work in non-interactive shell.
top_history() {
    history | awk '{ print $2 }' | sort | uniq -c | sort -nr | head -10
}


# refer: https://stackoverflow.com/questions/21762356/history-command-works-in-a-terminal-but-doesnt-when-written-as-a-bash-script

# History expansion is only on by default in an interactive shell,
# but it can be enabled in a non-interactive shell with set -o history.
# The contents of .bash_history may need to be explicitly added to
# the history list of the current shell with history -r ~/.bash_history
