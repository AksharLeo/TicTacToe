# TicTacToe
Play TicTacToe in the console (currently only supports local player vs player)




# Install

## Windows

Download the Exe file from the [releases](https://github.com/AksharLeo/TicTacToe/releases/latest)


## Linux

Download the AppImage depending on your PC ARCH from the [releases](https://github.com/AksharLeo/TicTacToe/releases/latest)

open the folder you downloaded the appimage to in Terminal

```
chmod +x TicTacToe-*.AppImage
``` 


## Run with python
prerequisuites:

[git](https://git-scm.com/downloads)

[python](https://www.python.org/downloads/)

```
git clone https://github.com/AksharLeo/TicTacToe
cd TicTacToe
python main.py
```


# Building from Source

## Windows
prerequisuites:

[git](https://git-scm.com/downloads)

[python](https://www.python.org/downloads/)

[pyinstaller](https://pypi.org/project/pyinstaller/)

[Pillow](https://pypi.org/project/Pillow/)

```
git clone https://github.com/AksharLeo/TicTacToe
cd TicTacToe
pyinstaller --onefile --console tictactoe.py
```

the application will be in `TicTacToe/dist/`


## Linux

prerequisuites:

[git](https://git-scm.com/downloads)

[python](https://www.python.org/downloads/)

[pyinstaller](https://pypi.org/project/pyinstaller/)

[AppImageTool](https://github.com/AppImage/AppImageKit)

```
git clone https://github.com/AksharLeo/TicTacToe
cd TicTacToe
*copy the appimagetool to this folder*
chmod +x /path/to/appimagetool
cd resources/tictactoe.AppDir
chmod +x AppRun && chmod +x tictactoe.desktop && chmod +x usr/bin/tictactoe
cd ../..
```

*for amd64*
```ARCH=x86_64 /path/to/appimagetool resources/tictactoe.AppDir```

*for arm64*
```ARCH=aarch64 /path/to/appimagetool resources/tictactoe.AppDir```

*for i686*
```ARCH=i686 /path/to/appimagetool resources/tictactoe.AppDir```


# Known Issues

The AppImages aren't working

workaround: open the appimage through a terminal

# credits
icon: Tic Tac Toe by Prerak Patel from <a href="https://thenounproject.com/browse/icons/term/tic-tac-toe/" target="_blank" title="Tic Tac Toe Icons">Noun Project</a>
