#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2015 Jakob Luettgau
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import datetime

import tapesim.components.Component


class Switch(tapesim.components.Component.Component):
    """
    Switches are used to connect network components.
    To keep the model simple a switch is required between components.
    """

    def __init__(self, simulation, throughput=100):
        super().__init__(simulation=simulation)

        self.throughput = throughput
        self.active = []

        pass

	
    def update_allocations(self):
	# recalculate finish times to find next step
        pass


    def serve(self, request):
        """Starts serving the request. And sets busy until accordingly."""
        print("Serve:", request)
        duration = request.attr["len"]/float(self.throughput)
        print("Duration:", duration)
        delta = datetime.timedelta(seconds=0, microseconds=10) * duration
        print("Delta:", delta)
        self.busy_until = self.simulation.now() + delta
        print("Busy until:", self.busy_until)

        return self.busy_until



    #TODO: busy until is flawed here as that depends on the badnwidth

