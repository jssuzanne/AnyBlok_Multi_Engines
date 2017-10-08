# This file is a part of the AnyBlok Multi Engines project
#
#    Copyright (C) 2016 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
# flake8: noqa
from anyblok import Declarations


@Declarations.register(Declarations.Core)
class Session:

    def test_the_session_is_updated(self):
        return True


@Declarations.register(Declarations.Core)
class Query:

    def all_name(self):
        return self.all().name
