"""LTI Jupyterhub configuration file

This file contains the bare-bones configurations for the student-facing Jupyterhub.
Note that LTI Authentication will NOT work until you have generated the appropriate
keys. More information can be read here: https://github.com/jupyterhub/ltiauthenticator
"""

import os

c.JupyterHub.authenticator_class = 'ltiauthenticator.LTIAuthenticator'
c.LTIAuthenticator.consumers = {
   os.environ['LTI_CLIENT_KEY']: os.environ['LTI_CLIENT_SECRET']
}

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = 'ubcdsci/r-dsci-100:latest'
c.Spawner.default_url = '/lab'
c.JupyterHub.hub_ip = '172.17.0.1'
c.DockerSpawner.host_ip = '0.0.0.0'
