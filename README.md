![logo](https://i.imgur.com/4lRkZw4.png)



Manim is an animation engine for explanatory math videos. It's used to create precise animations programmatically, as seen in the videos at [3Blue1Brown](https://www.3blue1brown.com/).

This repository contains the version of manim used by 3Blue1Brown. There is also a community maintained version at https://github.com/ManimCommunity/manim/.

## Installation
Manim runs on Python 3.7. You can install it from PyPI via pip:

```sh
pip3 install manimlib
```

System requirements are [cairo](https://www.cairographics.org), [ffmpeg](https://www.ffmpeg.org), [sox](http://sox.sourceforge.net), [latex](https://www.latex-project.org) (optional, if you want to use LaTeX).

You can now use it via the `manim` command. For example:

```sh
manim my_project.py MyScene
```

For more options, take a look at [documentation](https://manimce.readthedocs.io/en/latest/installation.html)and follow the instructions according to your operating system.


## Using manim
Try running the following:
```sh
python3 -m  manim BlochSphere_Example.py -pl
```
The `-p` flag in the command above is for previewing, meaning the video file will automatically open when it is done rendering. The `-l` flag is for a faster rendering at a lower quality.

Some other useful flags include:
* `-s` to skip to the end and just show the final frame.
* `-n <number>` to skip ahead to the `n`'th animation of a scene.
* `-f` to show the file in finder (for OSX).

Set `MEDIA_DIR` environment variable to specify where the image and animation files will be written.

Look through the `old_projects` folder to see the code for previous 3b1b videos. Note, however, that developments are often made to the library without considering backwards compatibility with those old projects. To run an old project with a guarantee that it will work, you will have to go back to the commit which completed that project.

While developing a scene, the `-sp` flags are helpful to just see what things look like at the end without having to generate the full animation. It can also be helpful to use the `-n` flag to skip over some number of animations.

### Documentation
Documentation is in progress at [eulertour.com/docs](https://www.eulertour.com/docs/).

## Quantum Animation Examples
### Bloch Sphere(Hadamard Gate)
![](https://i.imgur.com/0S6jLaH.gif)

## Contributing
Pull requests to this repository are welcomed.
Any improvement in manim should be directed to the [community version](https://github.com/ManimCommunity/manim/).

## License

The general purpose animation code found in the the repository is under the MIT license.
