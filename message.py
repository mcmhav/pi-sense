from sense_hat import SenseHat
import argparse

parser = argparse.ArgumentParser(description='Sending a message.')
parser.add_argument(
    'message',
    # metavar='N',
    type=str,
    # nargs='+',
    default='Hello world',
    help='The message to be shown'
)

args = parser.parse_args()

sense = SenseHat()
sense.show_message(args.message)
