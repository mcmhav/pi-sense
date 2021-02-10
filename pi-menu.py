from sense_hat import SenseHat

SENSE = SenseHat()


def color_lol():
  def red():
    SENSE.clear(255, 0, 0)
  def blue():
    SENSE.clear(0, 0, 255)
  def green():
    SENSE.clear(0, 255, 0)
  def yellow():
    SENSE.clear(255, 255, 0)

  in_menu = True
  while in_menu:
      for event in SENSE.stick.get_events():
          # Check if the joystick was pressed
          if event.action == "pressed":
              if event.direction == "up": # Up arrow
                  red()
              elif event.direction == "down": # Down arrow
                  blue()
              elif event.direction == "left": # Left arrow
                  green()
              elif event.direction == "right": # Right arrow
                  yellow()
              elif event.direction == "middle": # Enter key
                  in_menu = False
                  break

def up_action():
    SENSE.show_letter("U")
def down_action():
    SENSE.show_letter("D")
def left_action():
    SENSE.show_letter("L")
def right_action():
    SENSE.show_letter("R")
    color_lol()
    
def middle_action():
    SENSE.show_letter("M")

def main():
    while True:
        for event in SENSE.stick.get_events():
            # Check if the joystick was pressed
            if event.action == "pressed":
                if event.direction == "up": # Up arrow
                    up_action()
                elif event.direction == "down": # Down arrow
                    down_action()
                elif event.direction == "left": # Left arrow
                    left_action()
                elif event.direction == "right": # Right arrow
                    right_action()
                elif event.direction == "middle": # Enter key
                    middle_action()


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        SENSE.clear()
