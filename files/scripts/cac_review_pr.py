#!/usr/bin/python3

"""
This script creates a local branch with the code from an Upstream PR.
It is useful for Upstream maintainers who quite often need to download the code
to review and test proposed changes in a local environment.

It must be called from the repository to which the PR belongs.

Author: Marcus Burghardt <maburgha@redhat.com>
"""

import argparse
import subprocess


def fetch_pr(remote, pr, review_branch):
    return subprocess.run(['git', 'fetch', remote, f'pull/{pr}/head:{review_branch}'])


def update_pr(remote, pr, review_branch):
    return subprocess.run(['git', 'pull', remote, f'pull/{pr}/head:{review_branch}', '--force'])


def checkout_branch(branch_name):
    subprocess.run(['git', 'checkout', branch_name])


def parse_arguments():
    parser = argparse.ArgumentParser(
        description=("Script to optimize the PR review process in local environment. "
                    "It must be called from the repository to which the PR belongs."),
        epilog="Usage example: cac_review_pr.py 12090",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('pr', help="Upstream PR number")
    parser.add_argument(
        '--remote', default='upstream',
        help="Remote name linked to the Upstream repository")
    parser.add_argument(
        '--main-branch', default='master',
        help="Main branch name in Upstream repository")
    parser.add_argument(
        '--no-checkout', action='store_true',
        help="Do not checkout the just created branch")
    return parser.parse_args()


def main():
    args = parse_arguments()
    remote = f'{args.remote}'
    pr = f'{args.pr}'
    review_branch = f'REVIEW_PR_{pr}'

    fetch_pr_cmd = fetch_pr(remote, pr, review_branch)

    if fetch_pr_cmd.returncode != 0:
        print(f'PR {pr} was likely already fetched. Checking if it is updated.')
        update_pr_cmd = update_pr(remote, pr, review_branch)

        if update_pr_cmd.returncode != 0:
            raise('Failed to fetch or update the PR. Check the error messages.')

    if not args.no_checkout:
        checkout_branch(review_branch)


if __name__ == "__main__":
    main()
