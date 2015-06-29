Introduction
============

This is a slide deck created with the IPython notebook and rendered with
Reveal.js for the ISB TGCS 2015 conference.

Dependencies
============

Install Anaconda from:

http://continuum.io/downloads

Now install IPython in a terminal\ [#]_ with::

   conda install ipython-notebook

If IPython is already installed make sure to upgrade to the latest version::

   conda update ipython-notebook

.. [#] Either BASH on Unix or cmd.exe on Windows.

Editing
=======

Clone the repository to your computer with Git at the command line or whatever
GUI tool you use and navigate to the directory presentation directory in the
repository, e.g.::

   git clone git@github.com:csu-hmc/ISBTGCS2015.git
   cd ISBTGCS2015/presentation

Now start the IPython notebook::

   ipython notebook

At this point you can edit the cells of the notebook. Each cell is either a
slide, sub-slide, or notes. The cell type should be "markdown", and all of the
content is written in markdown syntax or raw HTML. The mathematics are written
in LaTeX and rendered with MathJax.

Save the notebook once you make your edits. Either close and halt the notebook
(menu option) and the IPython notebook server (CTRL-C at the command line) OR
just open a second terminal. To view the rendered slide desk, in the terminal
issue::

   ipython nbconvert human_control_param_id.ipynb --to slides --post serve

This will open the slides in your default web browser. It is best to use an
up-to-date web browser. You will need to be connected to the internet for slide
deck to render properly.

Make sure to commit your changes and push them back to the main repository.
