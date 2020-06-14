# jupyter-bootstrap

This repository contains installation scripts/config files for hosting remote Jupyterhub instances. These were tested on
AWS EC2 instances, but ideally should be agnostic of the cloud provider. This means that running these scripts on instances
hosted by other cloud providers, e.g. Azure, GCP, should be very simple (filepath changes may be neccessary).

## Requirements
* Remote instance should be on Ubuntu 18.04 LTS (or greater)
* Python 3.6+

## Usage

You should execute the scripts in sudo mode, run `sudo -sH` to obtain access to a superuser shell.
  * LTI hub: `python3 lti_bootstrap.py`
  * Grading hub: `python3 grading_bootstrap.py`

These commands should succeed in setting up a basic hub for each respective instance. Each function run in the script is 
documented, so there should be little ambiguity in what they do.

## Contact

In case of confusion or support, feel free to contact the original developer of these scripts
* [James Yoo](https://github.com/jyoo980)
