import logging

from pygerrit2 import GerritRestAPI, HTTPBasicAuth


def get_repositories(username, password, gerrit_url):
    auth = HTTPBasicAuth(username, password)
    rest = GerritRestAPI(url=gerrit_url, auth=auth)

    # get server information to derive clone commands
    logging.debug("getting server information..")
    server_info = rest.get("/config/server/info")
    clone_command = server_info["download"]["schemes"]["ssh"]["clone_commands"]
    clone_command = clone_command["Clone with commit-msg hook"]

    # get all projects
    logging.debug("getting project information..")
    repositories = rest.get("/projects/")

    result = []
    for repository_name in repositories.keys():
        project_clone_command = clone_command \
            .replace("${project}", repository_name) \
            .replace("${project-base-name}", repository_name)

        result.append({
            "name": repository_name,
            "scm": "git",
            "source": "gerrit",
            "source_username": username,
            "clone_command": project_clone_command
        })
    return result
