#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import argparse
import sys


def api_get_zones(base_url='', api_key=''):
    headers = {'X-API-Key': api_key}
    url = '{}/api/v1/servers/localhost/zones'.format(base_url)
    try:
        r = requests.get(url, headers=headers)
    except Exception as exc:
        print('Error occurred: {}({})'.format(type(exc).__name__, exc))
        return False
    else:
        if r.status_code == 200:
            return r.json()
        else:
            print('Error occurred: Can not get a list of zones')
            return False


def api_remove_zone(base_url='', api_key='', zone_name=''):
    headers = {'X-API-Key': api_key}
    url = '{}/api/v1/servers/localhost/zones/{}'.format(base_url, zone_name)
    try:
        r = requests.delete(url, headers=headers)
    except Exception as exc:
        print('Error occurred: {}({})'.format(type(exc).__name__, exc))
        return False
    else:
        if r.status_code == 204:
            return True
        else:
            print('Error occurred: Can not delete zone "{}"'.format(zone_name))
            return False


def check_master_zone_exist(name, zones):
    for zone in zones:
        if zone['name'] == name:
            return True


def create_cli():
    parser = argparse.ArgumentParser(description='Script for removing slave zones')
    parser.add_argument('-a', '--host', type=str, required=True,
                        help='powerdns slave server api address')
    parser.add_argument('-p', '--port', type=int, default=8081,
                        help='powerdns slave server api port (defaults to %(default)i)')
    parser.add_argument('-k', '--api-key', type=str, required=True,
                        help='powerdns slave server api key')
    parser.add_argument('--use-ssl', action='store_true',
                        help='use https instead http')
    parser.add_argument('--dry-run', action='store_true',
                        help='read-only mode. just show changes')

    return parser


def main():
    parser = create_cli()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()

    base_proto = 'https' if args.use_ssl else 'http'

    slave_zones = api_get_zones(base_url='{}://{}:{}'.format(base_proto, args.host, args.port), api_key=args.api_key)
    if not slave_zones:
        sys.exit()

    all_master_zones = {}

    for zone in slave_zones:
        if zone['kind'] == 'Slave':
            for master in zone['masters']:
                if master not in all_master_zones:
                    master_zones = api_get_zones(base_url='{}://{}:{}'.format(base_proto, master, args.port), api_key=args.api_key)
                    if master_zones or type(master_zones) is list:
                        all_master_zones.update({master: master_zones})

    for zone in slave_zones:
        if zone['kind'] == 'Slave':
            remove_flag = True
            for master in zone['masters']:
                if check_master_zone_exist(zone['name'], all_master_zones[master]):
                    remove_flag = False
                    break
            if remove_flag:
                if args.dry_run:
                    print('Zone "{}" will be removed'.format(zone['name']))
                else:
                    if api_remove_zone(base_url='{}://{}:{}'.format(base_proto, args.host, args.port), api_key=args.api_key, zone_name=zone['name']):
                        print('Zone "{}" was removed'.format(zone['name']))


if __name__ == '__main__':
    main()
