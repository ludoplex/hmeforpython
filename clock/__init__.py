# Unlike the hme module, this is a straight port of the version in 
# TiVo's Java SDK. (I've even kept the original comments.) As such, it's 
# a derivative work, released under the Common Public License.
#
# Original version credited authors: Adam Doppelt, Arthur van Hoff, 
# Brigham Stevens, Jonathan Payne, Steven Samorodin
# Copyright 2004, 2005 TiVo Inc.
#
# This version: William McBrine, 2008-2012

import thread
import time

import hme

"""This sample illustrates animation in a separate thread."""

class Clock(hme.Application):
    def startup(self):
        self.root.set_color()
        self.time_views = [hme.View(self, 0, 100, height=280)]
                           for i in xrange(2)]

        hme.Font(self, size=96, style=hme.FONT_BOLD)
        hme.Color(self, 0)

        # start a separate thread to update the time
        thread.start_new_thread(self.update, ())

    def update(self):
        fade = hme.Animation(self, 0.75)
        tm = time.time()
        n = 0

        while self.active:
            # fade out the old time
            self.time_views[n].set_transparency(1, fade)

            # switch to the other view
            n = (n + 1) % 2

            # show the current time
            self.time_views[n].set_text(time.strftime('%H:%M:%S'))
            self.time_views[n].set_transparency(0, fade)

            # now sleep
            tm += 1
            self.sleep(tm - time.time())
