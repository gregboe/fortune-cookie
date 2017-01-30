#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
    #make list of possible fortunes
    fortunes = [
        "Today it's up to you to create the peacefulness you long for.",
        "A friend asks only for your time not your money.",
        "If you refuse to accept anything but the best, you very often get it.",
        "A smile is your passport into the hearts of others."
    ]

    #randomly select one of the fortunes
    index = random.randint(0,3)
    #return one that is selected
    return fortunes[index]


class MainHandler(webapp2.RequestHandler):
    def get(self):

        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fortune_paragraph  = "<p>" + "Your fortune is: " + fortune + "</p>"

        lucky_number = random.randint(1,1000)
        lucky_number_sentece = "Your lucky number is: " + "<strong>" + str(lucky_number)+ "</strong>"
        lucky_number_paragraph = "<p>" + lucky_number_sentece + "</p>"

        cookie_again_button = """<a href="."><button>Another cookie please!</button></a>"""

        content = header + fortune_paragraph + lucky_number_paragraph + cookie_again_button

        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
