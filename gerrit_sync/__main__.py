import logging
import os
import re
import sys
import traceback
from requests.exceptions import HTTPError, ConnectionError

from . import util_gerrit, util_logging, cli


def clone_repositories(repositories, name_filter, dry_run):
    dirs = [d for d in os.listdir(".") if os.path.isdir(d)]

    count = 0

    for repository in repositories:
        if name_filter is not None \
                and re.match(name_filter, repository["name"]) is None:
            logging.debug("skipping filtered repository \"%s\"...",
                          repository["name"])
        elif repository["name"] in dirs:
            logging.info("skipping existing repository \"%s\"...",
                         repository["name"])
        else:
            logging.info("cloning repository \"%s\"...\n"
                         "clone command: %s\n",
                         repository["name"], repository["clone_command"])
            count += 1

            if not dry_run:
                os.system(repository["clone_command"])

    logging.info("finished cloning (%d) repositories.", count)


def run(args):
    logger = util_logging.adjust_logger()

    args = cli.parse_args(args)
    if not args:
        return

    logger.setLevel(util_logging.get_log_level(args.log_level))
    args = cli.prompt_for_missing_args(args)

    repositories = util_gerrit.get_repositories(
        args.gerrit_user, args.gerrit_password, args.gerrit_url)

    clone_repositories(repositories, args.filter, args.dry_run)


def main():
    args = sys.argv[1:]
    try:
        run(args)
    except KeyboardInterrupt:
        logging.error("Terminated on user input.")
        exit()
    except (HTTPError, ConnectionError):
        logging.error("Error connecting to server."
                      " Use '--log-level debug' to see details.")
        logging.debug(traceback.format_exc())
    except Exception:
        logging.error("An unknown error have occurred."
                      " Use '--log-level debug' to see details.")
        logging.debug(traceback.format_exc())
    sys.stdout.flush()


if __name__ == "__main__":
    main()
