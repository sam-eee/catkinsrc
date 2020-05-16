#!/usr/bin/env python

import rospy
from CR_week6_test.msg import perceived_info
from CR_week6_test.msg import robot_info
from CR_week6_test.srv import predict_robot_expression, predict_robot_expressionResponse
import random

import imp
try:
    imp.find_module('bayesian_belief_networks')
except:
    import roslib; roslib.load_manifest('bayesian_belief_networks')


from bayesian_belief_networks.ros_utils import *

##called with the percieved info recieved by the service, builds the Neural network and (Ideally) returns the response
def handlerPredictor(req):
    print ("Returning")
    testboy = robot_info()
    #g = ros_build_bbn(
    #    f_human_expression,
     #   f_human_action,
     #   f_robot_infoH, f_robot_infoS,f_robot_infoN)

    #print ("afterg")  #debug check

    ##couldnt get the bnn working so returning random values
    #testboy.id = req.id
    testboy.p_happy = 0.2
    testboy.p_sad = 0.6
    testboy.p_neutral = 0.2
    return predict_robot_expressionResponse(testboy)

def expression_prediction_server():
    rospy.init_node('robot_expression_prediction')  #node initialised
    s = rospy.Service('RobotExpressionPrediction', predict_robot_expression, handlerPredictor)  #service started
    print "Service up."
    rospy.spin()

#probability of inout
def f_human_expression(human_expression):
    return 0.33333333
def f_human_action(human_action):
    return 0.33333333
def f_object_size(object_size):
    return 0.5
## IMPLEMENTATION OF THE TABLE for robot reaction
def f_robot_infoS(human_expression, human_action, object_size):  ##bayesian values for Sad given the input values, returns probability
    table = dict()

    table['HRS'] = 0.2
    table['HRB'] = 0
    table['HOS'] = 0.2
    table['HOB'] = 0
    table['HAS'] = 0.2
    table['HAB'] = 0.2
    table['SRS'] = 0
    table['SRB'] = 0
    table['SOS'] = 0.1
    table['SOB'] = 0.1
    table['SAS'] = 0.2
    table['SAB'] = 0.2
    table['NRS'] = 0.3
    table['NRB'] = 0.2
    table['NOS'] = 0.2
    table['NOB'] = 0.1
    table['NAS'] = 0.2
    table['NAB'] = 0.2

    key = ''
    if human_expression==1:
        key = key + 'H'
    elif human_expression==2:
        key = key + 'S'
    else:
        key = key + 'N'
    if human_action==1:
        key = key + 'R'
    elif human_action==2:
        key = key + 'O'
    else :
        key = key + 'A'
    if object_size==1:
        key = key + 'S'
    else:
        key = key + 'B'
    return table[key]


def f_robot_infoH(human_expression, human_action, object_size): ##bayesian values for Happy given the input values, returns probability
    table = dict()

    table['HRS'] = 0.8
    table['HRB'] = 1.0
    table['HOS'] = 0.8
    table['HOB'] = 1.0
    table['HAS'] = 0.6
    table['HAB'] = 0.8
    table['SRS'] = 0
    table['SRB'] = 0
    table['SOS'] = 0
    table['SOB'] = 0.1
    table['SAS'] = 0
    table['SAB'] = 0.2
    table['NRS'] = 0.7
    table['NRB'] = 0.8
    table['NOS'] = 0.8
    table['NOB'] = 0.9
    table['NAS'] = 0.6
    table['NAB'] = 0.7

    key = ''
    if human_expression==1:
        key = key + 'H'
    elif human_expression==2:
        key = key + 'S'
    else:
        key = key + 'N'
    if human_action==1:
        key = key + 'R'
    elif human_action==2:
        key = key + 'O'
    else :
        key = key + 'A'
    if object_size==1:
        key = key + 'S'
    else:
        key = key + 'B'
    return table[key]


def f_robot_infoN(human_expression, human_action, object_size): ##bayesian values for neutral given the input values, returns probability
    table = dict()

    table['HRS'] = 0
    table['HRB'] = 0
    table['HOS'] = 0
    table['HOB'] = 0
    table['HAS'] = 0.2
    table['HAB'] = 0
    table['SRS'] = 1
    table['SRB'] = 1
    table['SOS'] = 0.9
    table['SOB'] = 0.8
    table['SAS'] = 0.8
    table['SAB'] = 0.6
    table['NRS'] = 0
    table['NRB'] = 0
    table['NOS'] = 0
    table['NOB'] = 0
    table['NAS'] = 0.2
    table['NAB'] = 0.1

    key = ''
    if human_expression==1:
        key = key + 'H'
    elif human_expression==2:
        key = key + 'S'
    else:
        key = key + 'N'
    if human_action==1:
        key = key + 'R'
    elif human_action==2:
        key = key + 'O'
    else :
        key = key + 'A'
    if object_size==1:
        key = key + 'S'
    else:
        key = key + 'B'
    return table[key]

if __name__ == "__main__":
    expression_prediction_server()
