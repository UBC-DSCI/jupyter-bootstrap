"""LTI Jupyterhub configuration file

This file contains the bare-bones configurations for the grading Jupyterhub.
"""

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = 'ubcdsci/r-dsci-grading:latest'
c.JupyterHub.hub_ip = '172.17.0.1'
c.DockerSpawner.host_ip = '0.0.0.0'
