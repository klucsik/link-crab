Feature: reporting and determining exit value
As a tester I want to generate human readable reports
and I want to determine failing conditions for CI,
for example return red if there is a link with status code 500

Rule: If the '-b' or '--broken' argument is provided, return 1 if there is a broken link
#TODO: Define broken links: status code 500 for sure but what else?

Rule: The application makes a CSV report from the collected data