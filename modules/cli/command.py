import argparse
import sys

from modules import image, image_to_csv_converter as csv_converter

commands = ["image_compress", "csv_export"]

def main():
    # print(sys.argv)
    # if sys.argv[1] == "scaffold":
    #     cmd_args = get_help_scaffold()
    # else:
    #     cmd_args = get_help_export_saas()
    # # image.compress("/home/odoo/Desktop/python/odootools/images")
    # csv_converter.convert("/home/odoo/Desktop/python/product.template.csv")
    # TODO: allow commands and arguments instead of hardcoding

    # image.compress("/home/odoo/Desktop/python/odootools/images")
    csv_converter.convert("/home/odoo/Downloads/product.template.csv")
