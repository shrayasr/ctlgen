"""

Usage:
    ctlgen --schema <schema_name> --table <table_name> --csv <csv_file> --record <record_delimiter> --field <field_delimiter> --error <error_log> --output_file <output_file>

Arguments:
    schema_name name of the schema to insert the CSV into
    table_name name of the table under schema to load into
    csv_file path of the csv file to load
    record_delimiter character to delimit each record by
    field_delimiter character to delimit each field by
    error_log the file to log errors to
    output_file the file to write the ctl info into


Options:
    -h --help Display all the options.
"""

import sys
from docopt import docopt

def create_ctl_file(schema_name, table_name, csv_file, record_delimiter, 
        field_delimiter, error_log):

    return """
    import data
    into table %s."%s"
    from '%s'
    record delimited by '%s'
    fields delimited by '%s'
    error log '%s'
    """ % (schema_name, table_name, csv_file, record_delimiter, field_delimiter, error_log)

def main():

    arguments = docopt(__doc__, argv=sys.argv[1:], help=True, version="0.0.1")

    schema_name = arguments.get("<schema_name>")
    table_name = arguments.get("<table_name>")
    csv_file = arguments.get("<csv_file>")
    record_delimiter = arguments.get("<record_delimiter>")
    field_delimiter = arguments.get("<field_delimiter>")
    error_log = arguments.get("<error_log>")
    output_file = arguments.get("<output_file>")

    ctl_contents = create_ctl_file(schema_name, table_name, csv_file, 
            record_delimiter, field_delimiter, error_log)

    with open(output_file, 'w') as f:
        f.write(ctl_contents)

if __name__ == "__main__":
    main()
