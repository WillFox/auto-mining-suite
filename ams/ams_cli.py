
"""
Main function for ams software

@Author: William Fox
@Created: 03-13-2017
@Modified: 03-13-2017


"""
from core.driver import build_database
#Code to analyze Supervised learning

import argparse

import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import os
import sys
import yaml


from ams import data_retrieve
from ams import supervised_learning
from ams import unsupervised_learning
from ams import random_optimization


import logging

# create logger
logger = logging.getLogger('ams_cli')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
#logger.debug('debug message')
#logger.info('info message')
#logger.warn('warn message')
#logger.error('error message')
#logger.critical('critical message')


#FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
#logging.basicConfig(format=FORMAT)
#d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
#logger = logging.getLogger('tcpserver')
#logger.warning('Protocol problem: %s', 'connection reset', extra=d)

#FORMAT = ""
#logging.basicConfig(format=FORMAT)
#logger=logging.getLogger("ams_cli")
#logger.setLevel(logging.DEBUG)

"""
PRIMARY FUNCTIONS
"""
def download_data(args):
    logger.info("Download Data")
    data_retrieve(args.name)


"""
PARSERS
"""    
def setup_parser():
    parser = argparse.ArgumentParser(description="Machine Learning Suite",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="A FoxiDev Software in coordination with Deviant Wave")
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    subparsers = parser.add_subparsers(dest="ml_methods")

    #Top Level
    _addGetData(subparsers)

    return parser.parse_args()


"""
GET DATA
"""
def _addGetData(subparsers):
    gd_configuration = subparsers.add_parser("gd", 
        help="Download Data Sets for Study",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    gd_configuration.set_defaults(func=download_data)
    gd_configuration.add_argument(
        '-n',
        "--name",
        type=str,
        metavar="data_name",
        required=False,
        help="Label in data configuration file (yaml file)")


    #sub_gd=gd_configuration.add_subparsers(dest="gd_methods")

    #_addDataGrab(sub_gd)


"""
SUPERVISED LEARNING
"""
"""
def _addSupervisedLearning(subparsers):
    sl_configuration = subparsers.add_parser("sl", help="supervised learning methods",
                                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    sl_configuration.set_defaults(func=supervised_learning_in)
    sub_sl=sl_configuration.add_subparsers(dest="sl_methods")
    
    _addDecisionTrees(sub_sl)
    _addNeuralNetwork(sub_sl)
    _addBoosting(sub_sl)
    _addSVM(sub_sl)
    _addKNN(sub_sl)

def _addDecisionTrees(sub_sl):
    dt_configuration = sub_sl.add_parser("dt", help="decision tree",
                                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    dt_configuration.set_defaults(func2=dt)
    dt_configuration.add_argument(
        '-d',
        "--data-file", 
        type=str,
        metavar="data_file",
        required=False,
        help="data file")
"""

def main():
    args=setup_parser()
    args.func(args)
    #parser = argparse.ArgumentParser(description="Machine Learning Suite")

if __name__=="__main__":
    main()
    #test_code()
 
