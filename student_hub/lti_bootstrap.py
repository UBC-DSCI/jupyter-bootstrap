"""LTI Jupyterhub Boostrap Script

This script runs a number of shell commands to set up a basic TLJH
(The Littlest Jupyterhub) instance. It is to be run from from the 
command line of the remote machine instance on which the hub is 
to be hosted.
"""

import os
from typing import *

def install_docker() -> None:
    """Installs Docker on the instance.

    This is required in order for the Jupyterhub to spawn containers with a specific
    Docker image.

    Commands:
        apt-get update
        apt-get remove docker docker-engine docker.io
        apt-install docker.io

    Raises: 
        Exception if Docker is not able to be installed successfully.
    """
    exit_codes = []
    exit_codes.append(os.system('apt-get update'))
    exit_codes.append(os.system('apt-get remove docker docker-engine docker.io'))
    exit_codes.append(os.system('apt-install docker.io'))
    if not _all_clear(exit_codes):
        raise Exception("Docker installation has failed with a non-zero exit code")

def pull_image(image_name: str) -> None:
    """Pulls the specified image from the registry, and builds it on the instance.

    Commands:
        systemctl start docker
        docker pull <image_name>

    Args:
        image_name: Use this to specify the image you want to use.

    Raises:
        Exception if the image fails to be pulled from the registry.
    """
    exit_codes = []
    exit_codes.append(os.system('systemctl start docker'))
    pull_command = f"docker pull {image_name}"
    exit_codes.append(os.system(pull_command))
    if not _all_clear(exit_codes):
        raise Exception(f"Pulling: {image_name} failed")

def install_dockerspawner() -> None:
    """Installs the DockerSpawner pip package.

    This is required to spawn single-user containers.

    Commands:
        /opt/tljh/hub/bin/python3 -m pip install dockerspawner

    Raises:
        Exception if the package is not able to be installed.
    """
    exit_codes = []
    exit_codes.append(os.system('/opt/tljh/hub/bin/python3 -m pip install dockerspawner'))
    if not _all_clear(exit_codes):
        raise Exception("DockerSpawner was not able to be pip installed")

def install_jupyterlab() -> None:
    """Installs the jupyterlab pip package

    This is required to spawn single-user containers as Jupyterlab instances.

    Commands:
        /opt/tljh/hub/bin/python3 -m pip install jupyterlab
        /opt/tljh/hub/bin/jupyter serverextension enable --py jupyterlab --sys-prefix

    Raises:
        Exception if the package is not able to be installed.
    """
    exit_codes = []
    exit_codes.append(os.system('/opt/tljh/hub/bin/python3 -m pip install jupyterlab'))
    exit_codes.append(os.system('/opt/tljh/hub/bin/jupyter serverextension enable --py jupyterlab --sys-prefix'))
    if not _all_clear(exit_codes):
        raise Exception("Jupyterlab was not able to be pip installed")

def install_jupyterlab_git() -> None:
    """Installs the jupyterlab-git extension: https://github.com/jupyterlab/jupyterlab-git

    Note: 
        This may not work, since the lab environments are installed in the container, and 
        this commands installs it locally.

    Commands:
        /opt/tljh/hub/bin/python3 -m pip install jupyterlab

    Raises:
        Exception if the extension is not able to be installed.
    """
    exit_codes = []
    exit_codes.append(os.system('/opt/tljh/hub/bin/python3 -m pip install jupyterlab'))
    if not _all_clear(exit_codes):
        raise Exception("The jupyterlab-git extension was not able to be pip installed")

def install_jupytext() -> None:
    """Installs the jupytext extension: https://github.com/mwouts/jupytext

    Note: 
        This may not work, since the lab environments are installed in the container, and 
        this commands installs it locally.

    Commands:
        /opt/tljh/hub/bin/python3 -m pip install jupytext --upgrade

    Raises:
        Exception if the extension is not able to be installed.
    """
    exit_codes = []
    exit_codes.append(os.system('/opt/tljh/hub/bin/python3 -m pip install jupytext --upgrade'))
    if not _all_clear(exit_codes):
        raise Exception("The jupytext extension was not able to be pip installed")

def build_jupyterlab() -> None:
    """Rebuilds the local Jupyterlab

    Note:
        The --minimize=False flag is needed, otherwise the build will not complete, this appears
        to be an ongoing issue. See this for more details: https://github.com/jupyterlab/jupyterlab/issues/4276

    Commands:
        /opt/tljh/hub/bin/jupyter lab build --minimize=False

    Raises:
        Exception if the build is not complete.
    """
    exit_codes = []
    exit_codes.append(os.system('/opt/tljh/hub/bin/jupyter lab build --minimize=False'))
    if not _all_clear(exit_codes):
        raise Exception("Jupyterlab was not able to be built")

def set_config() -> None:
    """Copies over the config file in the configuration directory of the remote instance.

    Commands:
        mkdir -p /opt/tljh/config/jupyterhub_config.d/jupyterhub_config.py
        cp jupyterhub_config.py /opt/tljh/config/jupyterhub_config.d/jupyterhub_config.py

    Raises:
        Exception if the configuration file is not able to be copied over.
    """
    exit_codes = []
    exit_codes.append(os.system('mkdir -p /opt/tljh/config/jupyterhub_config.d/jupyterhub_config.py'))
    exit_codes.append(os.system('cp jupyterhub_config.py /opt/tljh/config/jupyterhub_config.d/jupyterhub_config.py'))
    if not _all_clear(exit_codes):
        raise Exception("jupyterhub_config.py was not able to be copied over to the configuration directory")

def _all_clear(exit_codes: List[int]) -> bool:
    """Utility function for verifying exit codes from commands.

    Args:
        exit_codes: A list of exit codes from shell operations.

    Return:
        True iff all exit codes are zero, i.e. all operations were successful.
    """
    return all(code == 0 for code in exit_codes)

def main() -> None:
    install_docker()
    pull_image('ubcdsci/r-dsci-100:latest')
    install_dockerspawner()
    install_jupyterlab()
    # optionally try to install the Jupyterlab extensions here
    set_config()

if __name__ == "__main__":
    main()
