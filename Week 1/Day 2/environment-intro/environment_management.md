# Environment management

## Setup

To start off week 1, run the following bash command from this directory:

```bash
environment-intro$ conda env create -f metis_env.yml
```

This will

- Create a new environment (metis). This name is defined in the YAML file
- Install all the packages needed for week one in one step.

The `nb_conda` package will automatically connect your conda environment to jupytyer.

## First time usage

The metis environment is _activated_ by typing

```bash
$ conda activate metis
```

If this is the first time you have used an environment, you may get told that you need to
set your shell up for conda environments. If this is the case, conda will give you some
instructions, telling you to run `conda init <SHELL_NAME>`.

If you are new to the command line, you are probably using the default shell `bash`. Run

```bash
$ conda init bash
```

and then open a new terminal once this is done. You can follow the "Usage" section from here.

## Usage

When coming in, run (from any directory)

```bash
$ conda activate metis
(metis) $   # prompt should show the environment being used
```

If successful, the prompt will contain the environment name. To launch Jupyter for example:

```bash
(metis) ~$ juypter notebook
```

When you are done, exit the environment with

```bash
(metis) ~$ conda deactivate
~$  # no longer in environment
```

When starting a new notebook, students should select "Kernel -> Change Kernel -> metis" before running.

## New notebooks

When creating a new notebook, select "metis" rather than "Python 3" ("Python 3" is the default or base environment). Selecting "metis" starts your notebook with Python 3 and all the packages installed in the metis environment.
