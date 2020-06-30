"""
Copyright 2020 - Present Okta, Inc.

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

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION


class GroupRule:
    def __init__(self, config=None):
        if config:
            self.actions = config["actions"]\
                if "actions" in config else None
            self.conditions = config["conditions"]\
                if "conditions" in config else None
            self.created = config["created"]\
                if "created" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.status = config["status"]\
                if "status" in config else None
            self.type = config["type"]\
                if "type" in config else None
        else:
            self.actions = None
            self.conditions = None
            self.created = None
            self.id = None
            self.last_updated = None
            self.name = None
            self.status = None
            self.type = None

# End of File Generation
