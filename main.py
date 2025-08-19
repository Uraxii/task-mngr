import argparse
import csv
from escpos.printer import Usb
from typing import List, Dict

from src.printers import MODELS, VENDORS


class TaskManager:
    def __init__(self, filename):
        self.tasks = []
        self.load_from_csv(filename)

    def load_from_csv(self, filename):
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                # Convert importance/urgency to integers
                row['importance'] = int(row['importance'])
                row['urgency'] = int(row['urgency'])
                self.tasks.append(row)

    def get_by_importance(self, level: int) -> List[Dict]:
        return [task for task in self.tasks if task['importance'] == level]

    def get_by_urgency(self, level: int) -> List[Dict]:
        return [task for task in self.tasks if task['urgency'] == level]

    def get_high_priority(self) -> List[Dict]:
        """Get tasks with importance=1 OR urgency=1"""
        return [task for task in self.tasks if task['importance'] == 1 or task['urgency'] == 1]

    def print_summary(self):
        print(f"Total tasks: {len(self.tasks)}")
        print(f"High importance: {len(self.get_by_importance(1))}")
        print(f"High urgency: {len(self.get_by_urgency(1))}")
        print(f"High priority overall: {len(self.get_high_priority())}")


def print_receipt(printer: Usb, msg: str) -> None:
    printer.set(align='center', bold=True)
    printer.print_and_feed(3)
    printer.text(msg)
    printer.print_and_feed(3)
    printer.cut()
    printer.close()


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='Task Manager',
        description='Print receipt tasks to printer.',
        epilog='')

    parser.add_argument(
        '-f', '--file', required=True, help='CSV file with tasks.')

    parser.add_argument(
        '-d', '--deliminator',
        default=';',
        help='Character to split CSV columns by (default=";")')

    parser.add_argument(
        '-t', '--test', action='store_true', help='Run printer test')

    parser.add_argument(
        "--whatif", action="store_true", help="See what taks will be printed."
    )

    parser.add_argument(
        '-v', '--verbose', action='store_true', help='Verbose output')

    args = parser.parse_args()
    return args


def main() -> None:
    args = parse_arguments()

    if args.test:
        test(VENDORS.EPSON, MODELS.TM_T20III)
        return

    tm = TaskManager(args.file)
    tm.print_summary()

    vendor = VENDORS.EPSON
    model = MODELS.TM_T20III
    printer = Usb(vendor, model)

    for tsk in tm.tasks:
        title = tsk['title']
        desc = tsk['description']
        importance = tsk['importance']
        urgency = tsk['urgency']

        message = f"{title}\n\nI:({importance}) U:({urgency})\n\n{desc}"
        print(message + "\n" + "=" * 10)

        if not args.whatif:
            print_receipt(printer, message)


if __name__ == "__main__":
    main()
