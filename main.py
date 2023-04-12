
import argparse
import json

from domainrecon import DomainRecon


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='domainrecon',
        description='Identifies active services on a given domain',
    )

    parser.add_argument('domain', help="The domain to identify services for")
    parser.add_argument('--extra-dkim-selectors', nargs='+', help="Extra DKIM selectors to include in the report output.")

    args = parser.parse_args()

    recon = DomainRecon(args.domain, args.extra_dkim_selectors)

    report = {
        "domain": args.domain,
        "identified_services": recon.identified_services,
        "dkim_selectors": recon.dkim_selectors,
        "errors": recon.errors,
    }

    print(json.dumps(report, indent=4))