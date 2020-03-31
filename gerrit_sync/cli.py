import argparse
import logging
import os
from getpass import getpass


def get_parser():
    parser = argparse.ArgumentParser(description="gerrit-sync")

    parser.add_argument("--gerrit-user",
                        help="Username for access to gerrit API."
                             " If not provided via this argument or the"
                             " environment variable GERRIT_USER,"
                             " it will be asked via the command prompt.",
                        default=os.environ.get("GERRIT_USER"))

    parser.add_argument("--gerrit-password",
                        help="** Password for access to gerrit API."
                             " If not provided via this argument or the"
                             " environment variable GERRIT_PASSWORD,"
                             " it will be asked via the command prompt."
                             " ** WARNING **: Providing the password via the"
                             " command line argument is not recommended "
                             " due to the risk of your password being"
                             " recorded in your shell history.",
                        default=os.environ.get("GERRIT_PASSWORD"))

    parser.add_argument("--gerrit-url",
                        help="Base URL of the gerrit API."
                             " If not provided via this argument or the"
                             " environment variable GERRIT_URL,"
                             " it will be asked via the command prompt."
                             " example: https://gerrit.mydomain.com",
                        default=os.environ.get("GERRIT_URL"))

    parser.add_argument("--filter",
                        help="A regular expression to filter project names."
                             " If not provided, projects are not filtered.")

    parser.add_argument("--dry-run",
                        help="If specified, just display the operations to be"
                             " done but do not perform them.",
                        action="store_true")

    parser.add_argument("--log-level",
                        choices=["error", "info", "debug"],
                        default="info")

    return parser


def parse_args(args):
    argument_parser = get_parser()
    args = argument_parser.parse_args(args)
    valid = validate_args(args)
    if valid:
        return args
    else:
        argument_parser.print_help()
        return None


def validate_args(args):
    if args.gerrit_url is None:
        logging.error("gerrit_url is not provided.")
        return False

    if args.gerrit_user is None:
        logging.error("gerrit_user is not provided.")
        return False

    return True


def prompt_for_missing_args(args):
    if args.gerrit_password is None:
        args.gerrit_password = getpass("password: ")
    return args
