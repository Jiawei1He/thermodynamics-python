# Setting up your programming environment

This notes describes how to set up a productive programming environment in Windows.

# Command Line Interface (CLI)
- A command-line interface is a text-based user interface used to run programs, manage computer files and interact with the computer.

## Git Bash
- [Git Bash](https://gitforwindows.org/) is an application for Microsoft Windows environments which provides an emulation for the Bash shell.
- Git is automatically installed along with Git Bash.
- Once Git Bash is installed, you can use the bash terminal to interact with Git repositories.
- The appearance of Git Bash can be modified [changing the settings file](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-customize-Git-Bash-Shell-prompt-settings):
   `$HOME\\AppData\\Local\\Programs\\Git\\etc\\profile.d\\git-prompt.sh`

## Windows Terminal
- [Windows Terminal](https://docs.microsoft.com/en-us/windows/terminal/) is a multi-tabbed terminal emulator developed by Microsoft that can be used to run any command-line app installed on your computer.
- The Windows Terminal is preconfigured to run several command-line tools:
  - Command Prompt.
  - PowerShell.
  - Azure Cloud Shell.
  - Windows Sybsystem for Linux (WSL).
- In addition, you can add other command-line tools to manage your entire system from a single place, including:
  - [Git Bash.](https://www.timschaeps.be/post/adding-git-bash-to-windows-terminal/)
  - [Cygwin.](https://www.commandlinewizardry.com/post/how-to-add-git-bash-to-windows-terminal)
  - [Anaconda Prompt.](https://dev.to/azure/easily-add-anaconda-prompt-in-windows-terminal-to-make-life-better-3p6j)
- More info:
  - [What is the Windows Terminal?](https://docs.microsoft.com/en-us/windows/terminal/)
  - [Windows Terminal Installation instructions.](https://docs.microsoft.com/en-us/windows/terminal/install)
  - [This question](https://stackoverflow.com/questions/56362161/on-windows-what-is-the-difference-between-git-bash-vs-windows-power-shell-vs-com) discusses the differences between Command Prompt, PowerShell, and Git Bash.
  - [This question](https://superuser.com/questions/1191805/can-git-bash-and-cygwin-shell-do-the-same-things) discusses the differences between Git Bash and Cygwin.
  - [This question](https://stackoverflow.com/questions/52905844/git-bash-on-windows-vs-wsl) discusses the differences between Git Bash and WSL.

## Terminal customization
- You can customize the appearance of your terminal with [Oh My Posh](https://github.com/JanDeDobbeleer/oh-my-posh)
- Many [themes available](https://ohmyposh.dev/docs/themes)
- Easy to customize your own theme
- [Blog post](https://www.hanselman.com/blog/my-ultimate-powershell-prompt-with-oh-my-posh-and-the-windows-terminal) about using `oh-my-posh`
- Great [windows installation instructions](https://gglas.ninja/blog/2022/07/how-to-setup-oh-my-posh-in-windows-terminal):
	- Install Windows terminal and Git Bash
	- Install font MesloLGM NF (Settings>Personalization>Fonts)
	- Set the font in the Window Terminal settings file:
	```json
	"defaults": {
		"font":
		{
		"face": "MesloLGM NF"
		}
	},
	```
	- Install `oh-my-posh` using the following Bash command:
	```bash
	winget install oh-my-posh
	```
	- Set the `oh-my-posh` theme by adding the following line to you `.bashrc` file:
	``` bash
	eval "$(oh-my-posh --init --shell bash --config {$POSH_THEMES_PATH}/theme.omp.json)"
	```
- Set `"terminal.integrated.fontFamily": "MesloLGS NF"` in VS Code to properly display `oh-my-posh` icons in the VS Code integrated terminal.
- Add the following lines to your `oh-my-posh` theme file to [display the Python version](https://stackoverflow.com/questions/68649314/how-to-display-current-virtual-environtment-in-python-in-oh-my-posh):
``` json
{
  "type": "python",
  "style": "powerline",
  "powerline_symbol": "\uE0B0",
  "foreground": "#100e23",
  "background": "#906cff",
  "template": " \uE235 {{ .Full }} {{ if .Venv }}{{ .Venv }}{{ end }}",
  "properties": {
	  "fetch_virtual_env": true
}
```
- Add the following lines to your `.bashrc` file to [prevent Conda errors](https://github.com/conda/conda/issues/7445#issuecomment-774579800) when encoding special characters and symbols:
``` bash
export PYTHONIOENCODING="UTF-8"
export PYTHONLEGACYWINDOWSSTDIO="UTF-8"
```

# Version Control System (VCS)
## Git
- [Git](https://git-scm.com/) is an open source distributed version control system to keep track of different file versions.
- Git is the version control system that powers GitHub, GitLab, and BitBucket.
- Git is automatically installed along with Git Bash.

## Mercurial
- [Mercurial](https://www.mercurial-scm.org/) is an open source distributed version control system

## Subversion
- [Apache Subversion](https://subversion.apache.org/) (often abbreviated SVN) is an open source centralized version control system.





# Integrated Development Environment (IDE)
- An integrated development environment is an application that combines several developer tools into a single graphical user interface (GUI).
- An IDE typically consists of:
  - Source code editor: A text editor that can assist in writing software code with features such as syntax highlighting with visual cues, providing language specific auto-completion, and checking for bugs as code is being written.
  - Debugger: A program used for testing other programs that can graphically display variable values at any step of the program's execution.
  - Interpreter selector: An utility to select which intepreter (including the interpreters of virtual environments) is used to execute the program.
- Visual Studio Code and Pycharm are two of the most popular IDEs for Python development
-  [This article](https://opendatascience.com/pycharm-vs-vscode-which-is-the-better-python-ide/) compares the advantages and drawbacks of PyCharm and Visual Studio Code.

## Pycharm
- PyCharm is a cross-platform (Windows, macOS, and Linux) Python Integrated Development Environment (IDE) providing a wide range of essential tools for Python developers.
- In other words, PyCharm is graphical user interface (GUI) to edit, execute, and debug run Python programs.
- You can download the Community Version (free) of the PyCharm IDE from the [Official webpage](https://www.jetbrains.com/pycharm/). Make sure to check the box to add the Pycharm `bin` folder to the `PATH`.
- Once the installation is complete, you can check [this tutorial](https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html) to create your first project.
- Do not forget to define the virtual environment when you create the project!
- If you forget to set your virtual environment when you created the project, you can configure it at any later time following [these instructions](https://docs.anaconda.com/anaconda/user-guide/tasks/pycharm/).
- When using PyCharm in Windows, you have to open PyCharm from the Git Bash terminal in order to have access the environment variables defined in the `.bashrc` file.
- Setting up an [alias](https://askubuntu.com/questions/17536/how-do-i-create-a-permanent-bash-alias) is convenient to open PyCharm from the terminal. Add the following line t oyou `.bashrc` file to add and alias for PyCharm
  ```
  alias pycharm="<path to the PyCharm executable>"
  ```
- PyCharm will not have access to the environment variables defined in your `.bashrc` file unless you open PyCharm from your Git Bash terminal. This is very invoncenient and made me switch to VS Code!

## VS Code

https://code.visualstudio.com/docs/python/python-quick-start

- [Visual Studio Code](https://code.visualstudio.com/) is a lightweight, yet powerful, open source code editor which runs on your desktop and is available for Windows, macOS and Linux.
- It comes with built-in support for JavaScript, TypeScript and Node.js and has a rich ecosystem of extensions for other languages and runtimes (such as C++, C#, Java, Python, PHP, Go, .NET).

### Installation
- The main program is a small executable that can be downloaded from [here](https://code.visualstudio.com/docs/setup/setup-overview).
- The extension plugins can be automatically installed from the main program.
- Some useful extensions:
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
  - [Remote Development Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
  - [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
  - [GitHub Markdown Preview Pack](https://marketplace.visualstudio.com/items?itemName=bierner.github-markdown-preview)
  - [Markdown Shortcuts](https://marketplace.visualstudio.com/items?itemName=mdickin.markdown-shortcuts)

### Workspaces
- A [Visual Studio Code Workspace](https://code.visualstudio.com/docs/editor/workspaces) is a collection of one or more folders that are opened in a Visual Studio Code instance.
- In many cases, you will have a single folder opened as the workspace but you can include more than one folder using multi-root workspaces.
- The workspaces enables Visual Studio Code to:
  - Configure settings that only apply to a specific folder or folders but not others.
  - Persist task and debugger launch configurations that are only valid in the context of that workspace.
  - Store and restore UI state associated with that workspace (for example, the files that are opened).
  - Selectively enable or disable extensions only for that workspace.
- This can be helpful when you are working on several related projects at one time.
- For example, you might have a repository with a product's documentation that you like to keep current when you update the product source code.
- [This article](https://www.ryanchapin.com/vscode-change-indent-for-file-explorer-tree/) explains how to change the identing in the VSCode file explorer.
- More information:
  - This [documentation entry](https://code.visualstudio.com/docs/editor/multi-root-workspaces) contains more information about how to work with workspaces.
  - This [question](https://stackoverflow.com/questions/44629890/what-is-a-workspace-in-visual-studio-code) discusses many aspects about workspaces.
  - This [question](https://stackoverflow.com/questions/52056826/how-to-move-a-visual-studio-code-workspace-to-a-new-location-painlessly) describes how to move workspaces to different directories.
  - This [video](https://www.youtube.com/watch?v=k6mJwIQ6lO8) shows how to create and use workspaces.


### Terminal environment
- Visual Studio Code includes a fully-featured integrated terminal that conveniently starts at the root of your workspace.
- You can interact with the Visual Studio Code terminal as if it were an ordinary terminal.
- The integrated terminal can use various shells installed on your machine.
- The default terminal can be defined with the `Terminal › Integrated › Default Profile: Windows` setting.
- This [documentation page](https://code.visualstudio.com/docs/terminal/basics) contains more information about the integrated terminal.

### Python
- Visual Studio Code has an [extension for Python development](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
- The [getting starting page](https://code.visualstudio.com/docs/python/python-tutorial) contains a comprehensive tutorial about how to:
  - Install a Python interpreter.
  - Install Visual Studio Code and the Python extension.
  - Write, run, and debug a "Hello World" program in Python.
  - Create virtual environments and install packages.
  - Write a Python program to plot a figure using Matplotlib.
- Configuring Python:
  - This [question](https://stackoverflow.com/questions/67785598/how-to-change-vs-code-working-directory-to-the-running-file-directory) explains how to configure Visual Studio Code to execute the Python interpreter in the directory where the active Python file is located (similar user experience as Pycharm). TL;DR: Set the `Execute In File Dir` to true.
  - This [question](https://stackoverflow.com/questions/38623138/vscode-how-to-set-working-directory-for-debugging-a-python-program) explains how to configure Visual Studio Code to execute the Python debugger in the directory where the active Python file is located (similar user experience as Pycharm). TL;DR: Add the parameter `"cwd": "${fileDirname}"` to the `launch.json` file.
  - Make sure that you set the option to automatically recognize Conda in VSCode when installing conda. Otherwise VSCode will not be able to automatically detect Conda environments
  - Use the option `Terminal: Select Default Profile` to set `bash` as the default profile
  - Change the keybind to `Python: Run Python File in Terminal` to `Ctrl+Enter`
  - Sometimes VSCode does not find Conda virtual environments propertly. One workaround is to modify the `python.venvPath` setting. [More information here](https://code.visualstudio.com/docs/python/environments#_where-the-extension-looks-for-environments). This is not a clean solution, but I could not figure out why some VSCode installations cannot detect Conda properly
- This [documentation page](https://code.visualstudio.com/docs/python/environments) contains more information about how to:
  - Use Conda to create and manage environments.
  - Use venv to create and manage environments.
  - Select environments within Visual Studio Code.
  - Define environment variable files.
- This [article](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1) describes what are environment variable files and why they are useful for app development (.env file).
- This [documentation page](https://code.visualstudio.com/docs/languages/python) contains more information about Python development:
  - Autocomplete and IntelliSense
  - Linting
  - Debugging
  - Managing environments
  - Installing packages
  - Jupyter notebooks
  - Automatic testing

**2023-08-19**
- I experiences some problems with Conda and VS Code in which Conda was not detected
- A possible workaround for such problems is to set  `"python.venvPath": "{$HOME}\\AppData\\Local\\miniconda3\\envs"` in the VS Code settings file
- It is convenient to set the option `"python.terminal.activateEnvironment": true` to activate the current virtual environment in any new terminal opened within VS Code. For instance, to type Conda commands from the terminal from used to run your Python file.

### Markdown
- Markdown is a lightweight markup language for creating formatted text using a plain-text editor.
- Visual Studio Code offers basic Markdown functionality by default
- In addition, there are several Markdown extensions:
  - [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
  - [GitHub Markdown Preview Pack](https://marketplace.visualstudio.com/items?itemName=bierner.github-markdown-preview)
  - [Markdown Shortcusts](https://marketplace.visualstudio.com/items?itemName=mdickin.markdown-shortcuts)
- Markdown preview:
  - There is a preview window that is syncrhonized with the editor.
  - The preview window can be diplayed side-to-side with the editor.
  - However, the user cannot directly edit the text in the preview window (no WYSIWYG experience).
  - To improve the user experience I configured the command to open/close to preview window to the same keybind.
  - There is a [WYSIWYG extension](https://marketplace.visualstudio.com/items?itemName=zaaack.markdown-editor), but it works as a independent editor that does not integrate with the other extensions.


### Extensions
- [Excel Viewer](https://marketplace.visualstudio.com/items?itemName=GrapeCity.gc-excelviewer) to visualize .csv files
- [Insert Date String](https://marketplace.visualstudio.com/items?itemName=jsynowiec.vscode-insertdatestring) to create diary entries (configure keybind)

### Docker containers
- [Docker containers in Visual Studio Code](https://code.visualstudio.com/docs/containers/overview)
- [Create Python containers with Visual Studio Code](https://code.visualstudio.com/docs/containers/quickstart-python)
- [Deploy containers to Azure with Visual Studio Code](https://code.visualstudio.com/docs/containers/app-service)
- [Deploy containers to Azure with Visual Studio Code](https://docs.microsoft.com/en-us/azure/developer/python/tutorial-deploy-containers-01)


# Python virtual environments
- A Python environment is the context in which a Python program runs.
- A Python environment is composed of:
  - An interpreter.
  - Any number of installed packages.
- Environments are classified as:
  - The _global environment_ is the enviroment associated with the Python interpreter installed in your operative system.
  - _Virtual environments_ are separate environment associated with one or more Python projects.
- It is a good practice to have separate virtual environments for each Python project to avoid conflicts between packages.
- In addition, virtual environments allow you to have different python versions installed in the same computer. This can be useful to develop Python packages that support multiple Python versions.
- Virtual environments are created and managed using environment managers such as `venv` and `Conda`.
- Useful references:
  - [Creating and managing Python virtual environments](https://realpython.com/effective-python-environment/)
  - [Using virtual environments in Visual Studio Code](https://code.visualstudio.com/docs/python/environments)

## venv
- [venv](https://docs.python.org/3/library/venv.html) is the native Python virtual environment management tool.
- [venv](https://realpython.com/python-virtual-environments-a-primer/) uses the base Python installation of your computer and creates lightweight virtual environments in which you can install their own independent set of Python packages.
- `Conda` is more comprehensive than `venv` because it provides ways to specify the Python version of virtual environments.
- The package `virtualenv` is a superset of `venv` with some additional functionality:
  - Can be upgraded via `pip`
  - Can create virtual environments for arbitrarily created Python versions

### Creating a virtual environment with venv 
- Since `venv` is builtin into Python you do not have to install anything to start using it.
- Create your  first virtual environment (named `my_env`) running the `venv` module from the terminal: 
  ``` shell
  python -m venv my_env
  ```
  This command will execute Python with the `-m` option, which will run the `venv` module using the string `my_env` as input argument. The command will create a new folder (`my_env`) with several sub-folders to store all the files of the virtual environment.
- Activate the virtual environment executing the `activate` script. When using the Git Bash terminal in Windows you have to [source](https://superuser.com/questions/46139/what-does-source-do) the `activate` script:
  ``` shell
  source my_env/Script/activate
  ```
- Install individual packages using pip. [It is recommended](https://snarky.ca/why-you-should-use-python-m-pip/) to use:
  ``` shell
  python -m pip install numpy
  ```
  instead of:
  ```shell
  pip install numpy
  ```
  to ensure that the `pip` executable of the active Python version is being used.
- Alternatively, you can install several packages at once using a `requirements.txt file`
  ``` shell
  python -m pip install -r requirements.txt
  ```
- To deactivate the virtual environment simply type:
  ```
  deactivate
  ```
  You may wonder how does the terminal know where to find the `deactivate` function. According to one of the replies to [this answer](https://stackoverflow.com/a/29586756), the `deactivate` function is created in the current shell session when the `activate` script is sourced.
- If you want to uninstall packages without deleting the virtual environment you can do so with pip:
  ```
  source .venv/Scripts/activate
  python -m pip uninstall numpy
  ```
- Note that the `uninstall` will not uninstall pacakge dependencies as `pip` does not have a dependency solver for automatic cleanup.
- It is also possible to [create virtual environments directly from vscode](https://code.visualstudio.com/docs/python/environments):
  - Run the command `Python: Create Environment`
  - Select the venv environment
  - Select the base python installation
  - Select the `requirements.txt` file (if relevant)
  - Run the command `Python: Select Interpreter` and choose the new virtual environment


## Conda
[Miniconda](https://docs.conda.io/en/latest/miniconda.html) is a environment manager and package installer for Python. [This tutorial](https://realpython.com/python-windows-machine-learning-setup/) is a great reference to start using Conda in Windows.

### Installation
- [Download the installer](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html) and follow the instructions until the installation is completed.
- Conda activation:
  - In order to use the Conda from  Git Bash, you have to activate it.
  - The easiest way to achieve this in a permanent way is to modify your `.bashrc` file to initialize conda each time that bash is started.
  - Open your bash terminal and type the following command:
    ``` bash
    echo ". \${HOME}/AppData/Local/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    ```
  - This will add a new line to your `.bashrc` file that will execute `conda.sh` each time that you open the bash terminal.
  - To check if the command worked, you can open your `.bashrc` file:
    ```bash
    notepad ~/.bashrc 
    ```
  - Note that you may see your actual Windows username instead of the `${HOME}` variable.

### Creating a virtual environment with Conda
- The next step is to create a [Conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) to install and manage your Python packages.
- It is recommended to use an `environment.yaml` file that specifies all the Python packages that you need to install.
  - Using `environment.yaml` files is a great way to keep track of what Python packages you are using in a project.
  - Keeping `environment.yaml` files under Git version control is useful to go back in time and reproduce an old environment.
- The following `environment.yaml` file specifies a virtual environment based on Python 3.9 with some useful packages for scientific computing. Note that the `conda-forge` channel is added as it is required to install `Coolprop`.
  ``` yaml
  name: my_env
  channels:
    - conda-forge
  dependencies:
    - python=3.9
    - pip
    - numpy
    - scipy
    - matplotlib
    - coolprop
  ```
- To create the environment and install the packages, simply type the following command in your terminal:
  ```
  conda env create --file environment.yaml
  ```
- This will create the `my_env` virtual environment and install all the packages in the specified in the YAML file.
- If you want to install additional packages you can use the following commands:
  ```
  conda activate my_env
  conda install <name of the package>
  ```
- You can also use the [pip package manager](https://realpython.com/what-is-pip/) to install additional packages:
  ```
  conda activate my_env
  pip install <name of the package>
  ```
- Alternatively, you can install new packages by adding their names to the `environment.yaml` file and updating the environment:
  ```
  conda env update --file environment.yaml --prune
  ```
  The `--prune` option is not mandatory, but it is useful because it removes any dependencies that are no longer required.
- You can automatically activate an environment when you open a new terminal by adding the `conda activate` command to your `.bashrc` file. This can be achieved with the following command:
  ```
  echo "conda activate my_env" >> ~/.bashrc
  ```
- Check out the [Conda documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for more information about how to manage virtual environments.


## Poetry
- Python package and environment manager to:
  - Manage your virtual environments (no need to create them manually with venv)
  - Installing Python packages (replacement for pip install)
  - Manage your dependencies (dependency solver)
  - Build and publish your project as a Python package
- Poetry bundles together
  - `virtualenv` to manage virtual environments
  - `pip` to manage packages packages
  - A dependency solver to avoid package conflics
  - A dependency cleaner to uninstall unused dependencies
- Poetry handles the production and development environments in the same configuration file.
- Works with just one Python version (working with several Python versions handled externaly). The Python version can be installed manually or with Conda.
- Poetry is convenient to build and publish packages because uses a single `pyproject.toml` that bundles the functionality of:
  - `setup.py`
  - `requirements.txt`
  - `setup.cfg`
  - `MANIFEST.in`
- Getting started guides
  - [Poetry docs](https://python-poetry.org/docs/)
  - [Real Python](https://realpython.com/dependency-management-python-poetry/)
  - [Python Land](https://python.land/virtual-environments/python-poetry)


### Installation
- Install poetry as a package using the officient `install.poetry` script:
  ```shell
  curl https://install.python-poetry.org | POETRY_HOME=${HOME}/poetry python3 -
  ```
  With curl, you’re outputting the content of a requested URL to the standard output stream (stdout). By using a Unix pipeline with the pipe character (|), you’re handing over the output to the standard input stream (stdin) of python. In this case, you’re piping the content of install-poetry.py to your Python interpreter.
- In case you want to uninstall `poetry`, you can do so with the `--uninstall` option:
  ```shell
  curl -sSL https://install.python-poetry.org | POETRY_HOME=${HOME}/poetry python - --uninstall
  ```
- In order to use `poetry` from the terminal, append the `poetry/bin` directory to the `$PATH` environment variable in your `.bashrc` file:
  ```shell
  echo export PATH=\$PATH:"\${HOME}/poetry/bin" >> ~/.bashrc
  source ~/.bashrc
  ```
- Now `poetry` is installed and in your path. You can verify that the installation was successful with the following command:
  ```
  poetry --version
  ```

### Creating a project with Poetry
- Create a new Poetry project and move into the newly created directory:
  ```shell
  poetry new demo_poetry || cd demo_poetry
  ```
  This will create the project folder structure and the `pyproject.toml` file.
- Working with virtual environments is one of Poetry’s core features. However, Poetry doesn’t create a virtual environment right away when you start a project.
- You can confirm that Poetry hasn’t created a virtual environment by having Poetry list all virtual environments connected to the current project:
  ```shell
  poetry env list
  ```
  No virtual environments are displayed yet.
- By default VS Code will not detect the virtual environments used by Poetry. [To fix this issue](https://stackoverflow.com/questions/59882884/vscode-doesnt-show-poetry-virtualenvs-in-select-interpreter-option), you can configure Poetry to create the virtual envirnments inside the project path:
  ```shell
  poetry config virtualenvs.in-project true
  ```
- You can specify which Python version should be used to create the virtual environment used by `poetry`:
  ```shell
  poetry env use python
  ```
- With the `install` command, Poetry checks your `pyproject.toml` file for dependencies then resolves and installs them:
  ``` shell
  poetry install
  ```
- If you want to add an external package like `numpy` to your project, then you can run the `add` command:
  ```shell
  poetry add numpy
  ```
- You can add development dependencies with the `--dev` option:
  ```shell
  poetry add pytest --dev
  ```
- These commands added the `numpy` and `pytest` packages to the `pyproject.toml` and `poetry.lock` files. You can check what packages are included in your project with the `show` command:
  ``` shell
  poetry show
  ```
- You can also add dependencies by manually adding them to the `pyproject.toml` file. For instance, you can add the `scipy` package as:
  ```
  [tool.poetry.dependencies]
  python = "^3.10"
  numpy = "^1.24.2"
  scipy = "^1.10"
  ```
  Running `poetry install` now return an error because the `pyproject.toml` and `poetry.lock` files are out of sync.
- To pin manually added dependencies to the `poetry.lock` file you must first run the `lock` command:
  ``` shell
  poetry lock
  ```
- After locking dependencies with the poetry lock command, you have to run the poetry install command so that you can actually use them in your project:
  ``` shell
  poetry install
  ```
- Using the `poetry add` command more convenient and effective than editing the `pyproject.toml` file manually because automatically performs several actions:
  - Looks for a suitable version that does not conflict with other dependencies.
  - Installs the package in the accompanying virtual environment.
  - Creates or updates a lock file called poetry.lock.
- To uninstall a package from your project, use the `remove` command:
  ```shell
  poetry remove numpy
  ```
  This will remove the package and all of its dependencies (unless those dependencies are also required by another package listed in your `pyproject.toml` file).
- Similarly to adding dev dependencies, we can also remove them with the extra `--dev` option:
  ```shell
  poetry remove --dev pytest
  ```
- You can run a script in your project’s virtual environment by using the `poetry run` command. If you created a file called main.py, for example, you can run it with:
  ```shell
  poetry run python main.py
  ```
- Dependencies can be updated with the `poetry update` command:
  ```shell
  poetry update
  ```
  This command updates the dependencies in the virtual environment and then updates the poetry.lock file. In other words, using `poetry update` is equivalent to removing the `poetry.lock` file and running poetry install again.
- Poetry also offers functionality to convert the `pyproject.toml` file into a conventional `requirements.txt` file. To export your dependencies to a `requirements.txt` file, use the following command:
  ```shell
  poetry export --format requirements.txt --output project_requirements.txt --without-hashes
  ```

# Python package managers
- A package manager is a tool to install packages and manage the dependencies of your project.
- Dependencies are the Python packages that your project needs to function properly.
- Managing dependencies manually is very cumbersome because packages usually have their own dependencies as well.
- The main advantage of a package manager is that it will automatically install the correct version of all dependencies.
- Package managers can also be used to update or uninstall packages.
- The most common package managers for Python are:_Installation
  - [Pip](https://realpython.com/what-is-pip/)
  - [Conda](https://realpython.com/python-windows-machine-learning-setup/)
  - [Poetry](https://realpython.com/dependency-management-python-poetry/)

## Comparison of package managers
The differences between package manages are summarized in the table below:


| Field                    | Pip                   | Poetry                | Conda                                          |
|--------------------------|-----------------------|-----------------------|------------------------------------------------|
| Installation             | Native                | External              | External                                       |
| Operative system         | Cross-platform        | Cross-platform        | Cross-platform                                 |
| Languages supported      | Python                | Python                | Agnostic                                       |
| Python versions          | Single                | Single                | Multiple                                       |
| Virtual environments     | External              | Built-in or external  | Built-in                                       |
| Dependency checks        | Serial installation   | Dependency solver     | Dependency solver                              |
| Dependency cleanup       | No                    | Yes                   | Yes                                            |
| Package builder          | External              | Built-in              | Built-in                                       |
| Package repositories     | PyPI<br>Private repos | PyPI<br>Private repos | PyPI (via pip)<br>Conda repos<br>Private repos |


## Explanation of the fields
- **Installation.** Whether the package manager is built into Python (native) or has to be installed (external)
- **Operative system.** Cross-platform indicates that the package manager is available for Windows, MacOS, and Linux.
- **Languages supported.** Whether the pacakge manager supports packages in multiple programming languages or only Python.
- **Python versions.** Whether the package manager supports working multiple Python versions or just a single Python version. In case the package manager only supports one Python version, the Python version being used is configured externally.
- **Virtual environments.** Whether the package manager has built-in functionality to manage Python virtual environments or if they have to be externally managed via `venv` or `virtualenv`.
- **Dependency checks.** Whether or not the package manager has a dependency solver to verify that all requirements of all packages installed in an environment are met. Not having a dependency solver (serial installation) can lead to broken environents if the dependencies between al packages are not satisified simultaneously. Having a dependency solver ensures environment predictability and reproducibility, at the cost of longer installation times.
- **Dependency cleanup.** Whether of not the package manager can remove unused dependencies when a package is uninstalled.
- **Package builder**. Whether or not the package manager has functionality to package and publish Python packages.
- **Package repositories.** The type of repositories to download/publish packages.
  - [Python Package Index (PyPI)](https://pypi.org/)
  - The [anaconda](https://anaconda.org/anaconda/repo) and [conda-forge](https://anaconda.org/conda-forge/repo) repositories
  - Your own private repositories

## What package manager should I use?
- `pip`+`venv` if you just want to work with a single Python version and do not plan to publish your project.
- `poetry` if you want to work with a single Python version and you plan to publish your project as a Python package.
- `conda` if you have to work with virtual environments using different Python versions, or if want to create and publish a package that uses Python and other languages.

## Additional remarks
- `pip`+`venv` is lightweight and simple, but it is less powerful than `conda`.
- `pip`+`env` and `poetry` can achieve similar things, but package building and publishing is easier with `poetry`.
- `virtualenv` and `venv` use the Python versions already installed on your computer.
- `conda` is more powerful because it enables you to create an environment with a specific Python version.
- You can use `conda` to install the different Python versions that you intend to use with `pip`+`venv` or `poetry`.
- `conda` can publish packages to `conda-forge` or to private repositories.
- Conda can publish to `conda-forge`, but PyPI has higher visibility (more people use `pip` than `conda`).



# File comparison
## Meld
- Meld is a tool to visually compare and merge the content of several files
- For instance, you may want to use it to compare the content of two different versions of one of the configuration files used to create the asset hierarchy in CDF.
- Meld is specially relevant if you going to develop new code, because you can use Meld together with Git to compare and merge different versions of your files.
- You can download meld for Windows from [here](https://meldmerge.org/). 
- To set Meld as your `difftool` and `mergetool` you just have to type the [following commands](https://stackoverflow.com/questions/34119866/setting-up-and-using-meld-as-your-git-difftool-and-mergetool) in your bash terminal:
  ```bash
  git config --global merge.tool meld
  git config --global mergetool.meld.path "$(where meld)"
  git config --global diff.tool meld
  git config --global diff.meld.path "$(where meld)"
  ```


