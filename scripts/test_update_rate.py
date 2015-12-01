#!/usr/bin/env python
"""
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import sys
import remi.gui as gui
from remi import start, App
import rospy
from std_msgs.msg import Header


class MyApp(App):

    def __init__(self, *args):
        super(MyApp, self).__init__(*args)
        # This appears 6 times, exactly 6!
        print "Called MyApp __init__"

    def sub_cb(self, msg):
        rospy.loginfo("Cb: " + str(msg.seq))
        self.lbl.set_text(str(msg.seq))

    def main(self, name='world'):
        # the arguments are	width - height - layoutOrientationOrizontal
        wid = gui.Widget(240, 120, False, 10)
        self.lbl = gui.Label(200, 60, 'Hello %s!' % name)

        # appending a widget to another, the first argument is a string key
        wid.append('1', self.lbl)

        self.sub = rospy.Subscriber('/test', Header, self.sub_cb, queue_size=1)

        print "Initialized app"

        # returning the root widget
        return wid


if __name__ == "__main__":
    if len(sys.argv) > 1:
        rate = float(sys.argv[1])
    else:
        rate = 0.1
    # Initialize ROS
    rospy.init_node('test')
    # starts the webserver
    # optional parameters
    start(MyApp,
          address='127.0.0.1',
          port=8081,
          multiple_instance=False,
          enable_file_cache=True,
          update_interval=rate,
          start_browser=True)

    #start(MyApp, debug=False)
