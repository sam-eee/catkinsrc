#!/usr/bin/env python
import rospy
import random

#include all message types required
from CR_week6_test.msg import object_info
from CR_week6_test.msg import human_info
from CR_week6_test.msg import perceived_info



def interaction_generator():

    ##initialise publisher topics
    PubObject = rospy.Publisher("IntTopicObject", object_info, queue_size=10)
    PubHuman = rospy.Publisher("IntTopicHuman", human_info, queue_size=10)
    PubOverall = rospy.Publisher("IntTopicGenerate", perceived_info, queue_size=10)  ##used as I couldnt get two subscribers to synchronise in the following part

    #initialise node
    rospy.init_node('interaction_generator', anonymous=True)
    rate = rospy.Rate(0.1) # 0.1hz ie 10 seconds
    idnumber = 0   ##initialise interaction ID counter

    #initialise message containers
    obj = object_info()
    human = human_info()
    overallinfo= perceived_info()


    while not rospy.is_shutdown():

        idnumber+=1

        ##object values assignment and publishing
        obj.object_size = random.randint(1,2) #generates random object size between 1(small) and 2 (big)
        obj.id = idnumber
        PubObject.publish(obj) #publish object to topic IntTopicObject
        rospy.loginfo(obj)

        ##Human values assignment and publishing
        human.id = idnumber
        human.human_expression = random.randint(1,3)  #generates random human expression 1 (happy), 2(sad), 3(neutral)
        human.human_action = random.randint(1,3) #generates random human action 1(looking at robot face), 2(looking at colored toy), 3(looking away)7
        PubHuman.publish(human) #publish human to topic IntTopicHuman
        rospy.loginfo(human)


        ## values assignment and publishing
        overallinfo.id = idnumber
        overallinfo.object_size = obj.object_size
        overallinfo.human_action = human.human_action
        overallinfo.human_expression = human.human_expression

        PubOverall.publish(overallinfo) #publish object to topic IntTopicObject

        rate.sleep()


if __name__ == '__main__':
    try:
        interaction_generator()
    except rospy.ROSInterruptException:
        pass