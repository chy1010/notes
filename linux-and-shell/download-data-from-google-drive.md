
# Use gdrive

- Download the binary executive file on [https://github.com/prasmussen/gdrive/releases](https://github.com/prasmussen/gdrive/releases)
    - The two file `i_386` and `amd64` seems to be swapped.

- First launch:
    - `./gdrive about`: request authentication of a google account, use browser and log in, then copy the authentification code.

- Download a folder
    ```sh
        ./gdrive download --recursive <FOLDER ID>
    ```
