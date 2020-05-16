#!/usr/bin/env python
import rospy
import random
from CR_week6_test.msg import object_info
from CR_week6_test.msg import human_info
from CR_week6_test.msg import perceived_info
global Pubfilter

def callback(data):
    randomfilter = random.randint(1,8)
    rospy.loginfo(randomfilter)
     #generates random value and filters accordingly
    if randomfilter==1:
        data.object_size = 0
    elif randomfilter==2:
        data.human_action=0
    elif randomfilter==3:
        data.human_expression=0
    elif randomfilter == 4:
        data.object_size = 0
        data.human_action=0
    elif randomfilter==5:
        data.object_size = 0
        data.human_expression=0
    elif randomfilter==6:
        data.human_action=0
        data.human_expression=0
    elif randomfilter==7:
        data.object_size = 0
        data.human_action=0
        data.human_expression=0
    rospy.loginfo(data)
    Pubfilter.publish(data)  # publish object to topic Percieved


def callbackobj(data):
    pass
def callbackhuman(data):
    pass

def listener():
    rospy.init_node('Perception_Filter', anonymous=True)

    rospy.Subscriber("IntTopicGenerate", perceived_info, callback)  ##using this as I couldn't get both subscribers to synchronise without issues

    rospy.Subscriber("IntTopicObject", object_info, callbackobj)
    rospy.Subscriber("IntTopicHuman", human_info, callbackhuman)

    rospy.spin()


if __name__ == '__main__':
    Pubfilter = rospy.Publisher("Perceived", perceived_info, queue_size=10)
    listener()